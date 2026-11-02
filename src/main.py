from pathlib import Path
import sqlite3

from services.auth_service import AuthService
from init_users import init_users
from models.animal import Animal
from services.animal_service import AnimalService
from models.adopter import Adopter
from services.adopter_service import AdopterService
from models.adoption import Adoption
from services.adoption_service import AdoptionService
from models.employee import Employee
from services.employee_service import EmployeeService

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "shelter.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def init_database():
    DB_PATH.parent.mkdir(exist_ok=True)

    if not DB_PATH.exists():
        with sqlite3.connect(DB_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            connection.executescript(schema)

    init_users()


def employee_menu():
    while True:
        print("\nМеню сотрудника")
        print("1. Работа с животными")
        print("2. Просмотр будущих владельцев")
        print("3. Просмотр записей о пристройстве")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            animal_menu()
        elif choice == "2":
            adopter_service = AdopterService()

            for adopter in adopter_service.get_all():
                print(
                    adopter.adopter_id,
                    adopter.surname,
                    adopter.name,
                    adopter.patronymic,
                    adopter.phone,
                    adopter.address
                )

        elif choice == "3":
            adoption_service = AdoptionService()

            for adoption in adoption_service.get_all():
                print(
                    adoption.adoption_id,
                    adoption.animal_id,
                    adoption.adopter_id,
                    adoption.employee_id,
                    adoption.adoption_date
                )

        elif choice == "0":
            break
        else:
            print("Неверный пункт меню")

def animal_menu():
    service = AnimalService()

    while True:
        print("\nРабота с животными")
        print("1. Просмотреть всех животных")
        print("2. Добавить животное")
        print("3. Изменить животное")
        print("4. Удалить животное")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            animals = service.get_all()

            for animal in animals:
                print(
                    animal.animal_id,
                    animal.name,
                    animal.species,
                    animal.age,
                    animal.health_status,
                    animal.arrival_date
                )

        elif choice == "2":
            name = input("Имя животного: ")
            species = input("Вид животного: ")
            age_text = input("Возраст: ")
            health = input("Состояние здоровья: ")
            date = input("Дата поступления: ")

            try:
                age = int(age_text) if age_text else None

                animal = Animal(
                    0, name, species, age, health, date
                )

                service.add_animal(animal)
                print("Животное добавлено!")

            except ValueError as error:
                print(error)

        elif choice == "3":
            animal_id = int(input("Введите ID животного: "))
            old_animal = service.repository.get_by_id(animal_id)

            if old_animal is None:
                print("Животное не найдено")
                continue

            name = input("Новое имя: ")
            species = input("Новый вид: ")
            age_text = input("Новый возраст: ")
            health = input("Новое состояние здоровья: ")
            date = input("Новая дата поступления: ")

            try:
                age = int(age_text) if age_text else None

                animal = Animal(
                    animal_id, name, species, age, health, date
                )

                service.update_animal(animal)
                print("Данные обновлены!")

            except ValueError as error:
                print(error)

        elif choice == "4":
            try:
                animal_id = int(input("Введите ID животного: "))
                service.delete_animal(animal_id)
                print("Животное удалено!")

            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")

def adopter_menu():
    service = AdopterService()

    while True:
        print("\nРабота с будущими владельцами")
        print("1. Просмотреть всех владельцев")
        print("2. Добавить владельца")
        print("3. Изменить владельца")
        print("4. Удалить владельца")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            adopters = service.get_all()

            for adopter in adopters:
                print(
                    adopter.adopter_id,
                    adopter.surname,
                    adopter.name,
                    adopter.patronymic,
                    adopter.phone,
                    adopter.address
                )

        elif choice == "2":
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            phone = input("Телефон: ")
            address = input("Адрес: ")

            adopter = Adopter(
                0, surname, name, patronymic or None, phone, address or None
            )

            try:
                service.add_adopter(adopter)
                print("Владелец добавлен!")
            except ValueError as error:
                print(error)

        elif choice == "3":
            try:
                adopter_id = int(input("Введите ID владельца: "))
                old_adopter = service.repository.get_by_id(adopter_id)

                if old_adopter is None:
                    print("Владелец не найден")
                    continue

                surname = input("Новая фамилия: ")
                name = input("Новое имя: ")
                patronymic = input("Новое отчество: ")
                phone = input("Новый телефон: ")
                address = input("Новый адрес: ")

                adopter = Adopter(
                    adopter_id, surname, name,
                    patronymic or None, phone, address or None
                )

                service.update_adopter(adopter)
                print("Данные обновлены!")

            except ValueError as error:
                print(error)

        elif choice == "4":
            try:
                adopter_id = int(input("Введите ID владельца: "))
                service.delete_adopter(adopter_id)
                print("Владелец удалён!")
            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")

def read_int(prompt):
    value = input(prompt).strip()

    if not value:
        raise ValueError("Это поле обязательно для заполнения")

    try:
        return int(value)
    except ValueError:
        raise ValueError("Введите целое число")


def adoption_menu():
    service = AdoptionService()

    while True:
        print("\nУчет пристройства животных")
        print("1. Просмотреть все записи")
        print("2. Добавить запись")
        print("3. Изменить запись")
        print("4. Удалить запись")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            adoptions = service.get_all()

            for adoption in adoptions:
                print(
                    adoption.adoption_id,
                    adoption.animal_id,
                    adoption.adopter_id,
                    adoption.employee_id,
                    adoption.adoption_date
                )

        elif choice == "2":
            try:
                animal_id = read_int("ID животного: ")
                adopter_id = read_int("ID владельца: ")
                employee_id = read_int("ID сотрудника: ")
                adoption_date = input("Дата пристройства: ").strip()

                if not adoption_date:
                    raise ValueError("Укажите дату пристройства")

                adoption = Adoption(
                    0, animal_id, adopter_id, employee_id, adoption_date
                )

                service.add_adoption(adoption)
                print("Запись добавлена!")

            except ValueError as error:
                print(error)

        elif choice == "3":
            try:
                adoption_id = read_int("ID записи: ")
                animal_id = read_int("Новый ID животного: ")
                adopter_id = read_int("Новый ID владельца: ")
                employee_id = read_int("Новый ID сотрудника: ")
                adoption_date = input("Новая дата: ").strip()

                if not adoption_date:
                    raise ValueError("Укажите дату пристройства")

                adoption = Adoption(
                    adoption_id, animal_id, adopter_id,
                    employee_id, adoption_date
                )

                service.update_adoption(adoption)
                print("Запись обновлена!")

            except ValueError as error:
                print(error)

        elif choice == "4":
            try:
                adoption_id = read_int("ID записи: ")
                service.delete_adoption(adoption_id)
                print("Запись удалена!")

            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")

def employee_menu_admin():
    service = EmployeeService()

    while True:
        print("\nРабота с сотрудниками")
        print("1. Просмотреть всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Изменить сотрудника")
        print("4. Удалить сотрудника")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            employees = service.get_all()

            for employee in employees:
                print(
                    employee.employee_id,
                    employee.surname,
                    employee.name,
                    employee.patronymic,
                    employee.position,
                    employee.phone
                )

        elif choice == "2":
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            position = input("Должность: ")
            phone = input("Телефон: ")

            employee = Employee(
                0, surname, name, patronymic or None,
                position, phone or None
            )

            try:
                service.add_employee(employee)
                print("Сотрудник добавлен!")
            except ValueError as error:
                print(error)

        elif choice == "3":
            try:
                employee_id = int(input("ID сотрудника: "))
                old_employee = service.repository.get_by_id(employee_id)

                if old_employee is None:
                    print("Сотрудник не найден")
                    continue

                surname = input("Новая фамилия: ")
                name = input("Новое имя: ")
                patronymic = input("Новое отчество: ")
                position = input("Новая должность: ")
                phone = input("Новый телефон: ")

                employee = Employee(
                    employee_id, surname, name, patronymic or None,
                    position, phone or None
                )

                service.update_employee(employee)
                print("Данные обновлены!")

            except ValueError as error:
                print(error)

        elif choice == "4":
            try:
                employee_id = int(input("ID сотрудника: "))
                service.delete_employee(employee_id)
                print("Сотрудник удалён!")
            except ValueError as error:
                print(error)

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")

def admin_menu():
    while True:
        print("\nМеню администратора")
        print("1. Работа с сотрудниками")
        print("2. Работа с животными")
        print("3. Работа с будущими владельцами")
        print("4. Работа с пристройством")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "2":
            animal_menu()
        elif choice == "0":
            break
        elif choice == "3":
            adopter_menu()
        elif choice == "4":
            adoption_menu()
        elif choice == "1":
            employee_menu_admin()
        else:
            print("Неверный пункт меню")


def main():
    init_database()

    auth_service = AuthService()

    while True:
        print("\nСистема учета животных в приюте")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            login = input("Логин: ")
            password = input("Пароль: ")

            try:
                user = auth_service.authenticate(login, password)
                print("Вход выполнен успешно!")

                if user["role"] == "admin":
                    admin_menu()
                else:
                    employee_menu()

            except ValueError as error:
                print(error)

        elif choice == "2":
            login = input("Придумайте логин: ")
            password = input("Придумайте пароль: ")

            try:
                auth_service.register(login, password, "employee")
                print("Регистрация прошла успешно!")
            except ValueError as error:
                print(error)

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()