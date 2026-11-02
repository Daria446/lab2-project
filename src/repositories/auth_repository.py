from repositories.database import get_connection


class AuthRepository:

    def get_by_login(self, login):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM users WHERE login = ?",
            (login,)
        ).fetchone()

        connection.close()
        return row

    def create(self, login, password, role):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO users (login, password, role)
            VALUES (?, ?, ?)
            """,
            (login, password, role)
        )

        connection.commit()
        connection.close()