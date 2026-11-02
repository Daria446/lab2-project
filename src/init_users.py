from repositories.database import get_connection


def init_users():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Таблица users создана")


if __name__ == "__main__":
    init_users()