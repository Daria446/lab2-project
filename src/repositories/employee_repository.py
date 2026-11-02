from repositories.database import get_connection
from models.employee import Employee


class EmployeeRepository:

    def get_all(self):
        connection = get_connection()

        rows = connection.execute(
            "SELECT * FROM employees"
        ).fetchall()

        employees = []

        for row in rows:
            employee = Employee(
                row["employee_id"],
                row["surname"],
                row["name"],
                row["patronymic"],
                row["position"],
                row["phone"]
            )

            employees.append(employee)

        connection.close()
        return employees
    def get_by_id(self, employee_id):
        connection = get_connection()

        row = connection.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (employee_id,)
        ).fetchone()

        connection.close()

        if row is None:
            return None

        employee = Employee(
            row["employee_id"],
            row["surname"],
            row["name"],
            row["patronymic"],
            row["position"],
            row["phone"]
        )

        return employee

    def create(self, employee):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO employees
            (surname, name, patronymic, position, phone)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                employee.surname,
                employee.name,
                employee.patronymic,
                employee.position,
                employee.phone
            )
        )

        connection.commit()
        connection.close()

    def delete(self, employee_id):
        connection = get_connection()

        connection.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        connection.commit()
        connection.close()
    def update(self, employee):
        connection = get_connection()

        connection.execute(
            """
            UPDATE employees
            SET surname = ?, name = ?, patronymic = ?,
                position = ?, phone = ?
            WHERE employee_id = ?
            """,
            (
                employee.surname,
                employee.name,
                employee.patronymic,
                employee.position,
                employee.phone,
                employee.employee_id
            )
        )

        connection.commit()
        connection.close()