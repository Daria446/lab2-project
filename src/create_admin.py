from services.auth_service import AuthService


def main():
    auth_service = AuthService()

    login = input("Придумайте логин администратора: ")
    password = input("Придумайте пароль администратора: ")

    try:
        auth_service.register(login, password, "admin")
        print("Администратор успешно создан!")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()