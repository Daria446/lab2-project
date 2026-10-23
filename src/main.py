from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "shelter.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def main():
    DB_PATH.parent.mkdir(exist_ok=True)

    if not DB_PATH.exists():
        with sqlite3.connect(DB_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            connection.executescript(schema)

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        print("Система учета животных в приюте")
        print("База данных SQLite подключена.")

        tables = ["employees", "animals", "adopters", "adoptions"]

        for table in tables:
            result = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            )
            count = result.fetchone()[0]
            print(f"{table}: {count} записей")


if __name__ == "__main__":
    main()