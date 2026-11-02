from repositories.auth_repository import AuthRepository


class AuthService:

    def __init__(self):
        self.repository = AuthRepository()

    def register(self, login, password, role):
        if not login.strip() or not password.strip():
            raise ValueError("Введите логин и пароль")

        if role not in ("admin", "employee"):
            raise ValueError("Неверная роль")

        user = self.repository.get_by_login(login)

        if user is not None:
            raise ValueError("Такой логин уже существует")

        self.repository.create(login, password, role)

    def authenticate(self, login, password):
        user = self.repository.get_by_login(login)

        if user is None or user["password"] != password:
            raise ValueError("Неверный логин или пароль")

        return user