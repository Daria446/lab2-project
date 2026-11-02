from repositories.database import get_connection
from models.adoption import Adoption


class AdoptionRepository:

    def get_all(self):
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM adoptions"
        ).fetchall()

        adoptions = []

        for row in rows:
            adoption = Adoption(
                row["adoption_id"],
                row["animal_id"],
                row["adopter_id"],
                row["employee_id"],
                row["adoption_date"]
            )

            adoptions.append(adoption)

        connection.close()
        return adoptions

    def get_by_id(self, adoption_id):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM adoptions WHERE adoption_id = ?",
            (adoption_id,)
        ).fetchone()

        connection.close()

        if row is None:
            return None

        adoption = Adoption(
            row["adoption_id"],
            row["animal_id"],
            row["adopter_id"],
            row["employee_id"],
            row["adoption_date"]
        )

        return adoption

    def create(self, adoption):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO adoptions
            (animal_id, adopter_id, employee_id, adoption_date)
            VALUES (?, ?, ?, ?)
            """,
            (
                adoption.animal_id,
                adoption.adopter_id,
                adoption.employee_id,
                adoption.adoption_date
            )
        )

        connection.commit()
        connection.close()

    def update(self, adoption):
        connection = get_connection()

        connection.execute(
            """
            UPDATE adoptions
            SET animal_id = ?, adopter_id = ?,
                employee_id = ?, adoption_date = ?
            WHERE adoption_id = ?
            """,
            (
                adoption.animal_id,
                adoption.adopter_id,
                adoption.employee_id,
                adoption.adoption_date,
                adoption.adoption_id
            )
        )

        connection.commit()
        connection.close()

    def delete(self, adoption_id):
        connection = get_connection()

        connection.execute(
            "DELETE FROM adoptions WHERE adoption_id = ?",
            (adoption_id,)
        )

        connection.commit()
        connection.close()