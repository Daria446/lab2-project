from repositories.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def get_all(self):
        return self.repository.get_all()

    def add_employee(self, employee):
        if not employee.surname or not employee.name:
            raise ValueError("Введите фамилию и имя")

        if not employee.position:
            raise ValueError("Укажите должность")

        self.repository.create(employee)

    def update_employee(self, employee):
        old_employee = self.repository.get_by_id(employee.employee_id)

        if old_employee is None:
            raise ValueError("Сотрудник не найден")

        if not employee.surname or not employee.name:
            raise ValueError("Введите фамилию и имя")

        self.repository.update(employee)

    def delete_employee(self, employee_id):
        employee = self.repository.get_by_id(employee_id)

        if employee is None:
            raise ValueError("Сотрудник не найден")

        self.repository.delete(employee_id)