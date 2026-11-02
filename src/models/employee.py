from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: int
    surname: str
    name: str
    patronymic: str | None
    position: str
    phone: str | None