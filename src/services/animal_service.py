from repositories.animal_repository import AnimalRepository


class AnimalService:

    def __init__(self):
        self.repository = AnimalRepository()

    def get_all(self):
        return self.repository.get_all()

    def add_animal(self, animal):
        if not animal.name or not animal.species:
            raise ValueError("Введите имя и вид животного")

        if not animal.arrival_date:
            raise ValueError("Укажите дату поступления")

        if animal.age is not None and animal.age < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.repository.create(animal)

    def update_animal(self, animal):
        old_animal = self.repository.get_by_id(animal.animal_id)

        if old_animal is None:
            raise ValueError("Животное не найдено")

        if not animal.name or not animal.species:
            raise ValueError("Введите имя и вид животного")

        if not animal.arrival_date:
            raise ValueError("Укажите дату поступления")

        if animal.age is not None and animal.age < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.repository.update(animal)

    def delete_animal(self, animal_id):
        animal = self.repository.get_by_id(animal_id)

        if animal is None:
            raise ValueError("Животное не найдено")

        self.repository.delete(animal_id)