from repositories.adoption_repository import AdoptionRepository
from repositories.animal_repository import AnimalRepository
from repositories.adopter_repository import AdopterRepository
from repositories.employee_repository import EmployeeRepository


class AdoptionService:

    def __init__(self):
        self.repository = AdoptionRepository()
        self.animal_repository = AnimalRepository()
        self.adopter_repository = AdopterRepository()
        self.employee_repository = EmployeeRepository()

    def get_all(self):
        return self.repository.get_all()

    def add_adoption(self, adoption):
        animal = self.animal_repository.get_by_id(adoption.animal_id)
        adopter = self.adopter_repository.get_by_id(adoption.adopter_id)
        employee = self.employee_repository.get_by_id(adoption.employee_id)

        if animal is None:
            raise ValueError("Животное не найдено")

        if adopter is None:
            raise ValueError("Будущий владелец не найден")

        if employee is None:
            raise ValueError("Сотрудник не найден")

        adoptions = self.repository.get_all()

        for item in adoptions:
            if item.animal_id == adoption.animal_id:
                raise ValueError("Это животное уже пристроено")

        self.repository.create(adoption)

    def update_adoption(self, adoption):
        old_adoption = self.repository.get_by_id(adoption.adoption_id)

        if old_adoption is None:
            raise ValueError("Запись об усыновлении не найдена")

        if self.animal_repository.get_by_id(adoption.animal_id) is None:
            raise ValueError("Животное не найдено")

        if self.adopter_repository.get_by_id(adoption.adopter_id) is None:
            raise ValueError("Будущий владелец не найден")

        if self.employee_repository.get_by_id(adoption.employee_id) is None:
            raise ValueError("Сотрудник не найден")

        adoptions = self.repository.get_all()

        for item in adoptions:
            if item.animal_id == adoption.animal_id and item.adoption_id != adoption.adoption_id:
                raise ValueError("Это животное уже пристроено")

        self.repository.update(adoption)

    def delete_adoption(self, adoption_id):
        adoption = self.repository.get_by_id(adoption_id)

        if adoption is None:
            raise ValueError("Запись об усыновлении не найдена")

        self.repository.delete(adoption_id)