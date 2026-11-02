from repositories.adopter_repository import AdopterRepository


class AdopterService:

    def __init__(self):
        self.repository = AdopterRepository()

    def get_all(self):
        return self.repository.get_all()

    def add_adopter(self, adopter):
        if not adopter.surname or not adopter.name:
            raise ValueError("Введите фамилию и имя")

        if not adopter.phone:
            raise ValueError("Введите номер телефона")

        adopters = self.repository.get_all()

        for item in adopters:
            if item.phone == adopter.phone:
                raise ValueError("Такой номер телефона уже существует")

        self.repository.create(adopter)

    def update_adopter(self, adopter):
        old_adopter = self.repository.get_by_id(adopter.adopter_id)

        if old_adopter is None:
            raise ValueError("Человек не найден")

        if not adopter.surname or not adopter.name:
            raise ValueError("Введите фамилию и имя")

        if not adopter.phone:
            raise ValueError("Введите номер телефона")

        adopters = self.repository.get_all()

        for item in adopters:
            if item.phone == adopter.phone and item.adopter_id != adopter.adopter_id:
                raise ValueError("Такой номер телефона уже существует")

        self.repository.update(adopter)

    def delete_adopter(self, adopter_id):
        adopter = self.repository.get_by_id(adopter_id)

        if adopter is None:
            raise ValueError("Человек не найден")

        self.repository.delete(adopter_id)