from repositories.database import get_connection
from models.animal import Animal
import sqlite3


class AnimalRepository:
    def get_all(self):
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM animals"
        ).fetchall()

        animals = []

        for row in rows:
            animal = Animal(
                row["animal_id"],
                row["name"],
                row["species"],
                row["age"],
                row["health_status"],
                row["arrival_date"]
            )

            animals.append(animal)

        connection.close()
        return animals
    def get_by_id(self, animal_id):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM animals WHERE animal_id = ?",
            (animal_id,)
        ).fetchone()

        connection.close()

        if row is None:
            return None

        animal = Animal(
            row["animal_id"],
            row["name"],
            row["species"],
            row["age"],
            row["health_status"],
            row["arrival_date"]
        )

        return animal
    def create(self, animal):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO animals
            (name, species, age, health_status, arrival_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                animal.name,
                animal.species,
                animal.age,
                animal.health_status,
                animal.arrival_date
            )
        )

        connection.commit()
        connection.close()
    def update(self, animal):
        connection = get_connection()

        connection.execute(
            """
            UPDATE animals
            SET name = ?, species = ?, age = ?,
                health_status = ?, arrival_date = ?
            WHERE animal_id = ?
            """,
            (
                animal.name,
                animal.species,
                animal.age,
                animal.health_status,
                animal.arrival_date,
                animal.animal_id
            )
        )

        connection.commit()
        connection.close()
    def delete(self, animal_id):
        connection = get_connection()
        try:
            connection.execute(
            "DELETE FROM animals WHERE animal_id = ?",
            (animal_id,)
            )

            connection.commit()

        except sqlite3.IntegrityError:
            connection.rollback()
            raise ValueError("Нельзя удалить животное, так как оно уже пристроено")
        finally:
            connection.close()
