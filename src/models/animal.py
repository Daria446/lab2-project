from dataclasses import dataclass


@dataclass
class Animal:
    animal_id: int
    name: str
    species: str
    age: int | None
    health_status: str
    arrival_date: str