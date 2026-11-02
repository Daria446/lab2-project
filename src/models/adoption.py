from dataclasses import dataclass


@dataclass
class Adoption:
    adoption_id: int
    animal_id: int
    adopter_id: int
    employee_id: int
    adoption_date: str