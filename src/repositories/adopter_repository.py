from repositories.database import get_connection
from models.adopter import Adopter


class AdopterRepository:

    def get_all(self):
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM adopters"
        ).fetchall()

        adopters = []

        for row in rows:
            adopter = Adopter(
                row["adopter_id"],
                row["surname"],
                row["name"],
                row["patronymic"],
                row["phone"],
                row["address"]
            )

            adopters.append(adopter)

        connection.close()
        return adopters

    def get_by_id(self, adopter_id):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM adopters WHERE adopter_id = ?",
            (adopter_id,)
        ).fetchone()

        connection.close()

        if row is None:
            return None

        adopter = Adopter(
            row["adopter_id"],
            row["surname"],
            row["name"],
            row["patronymic"],
            row["phone"],
            row["address"]
        )

        return adopter

    def create(self, adopter):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO adopters
            (surname, name, patronymic, phone, address)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                adopter.surname,
                adopter.name,
                adopter.patronymic,
                adopter.phone,
                adopter.address
            )
        )

        connection.commit()
        connection.close()

    def update(self, adopter):
        connection = get_connection()

        connection.execute(
            """
            UPDATE adopters
            SET surname = ?, name = ?, patronymic = ?,
                phone = ?, address = ?
            WHERE adopter_id = ?
            """,
            (
                adopter.surname,
                adopter.name,
                adopter.patronymic,
                adopter.phone,
                adopter.address,
                adopter.adopter_id
            )
        )

        connection.commit()
        connection.close()

    def delete(self, adopter_id):
        connection = get_connection()

        connection.execute(
            "DELETE FROM adopters WHERE adopter_id = ?",
            (adopter_id,)
        )

        connection.commit()
        connection.close()