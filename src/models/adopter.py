from dataclasses import dataclass


@dataclass
class Adopter:
    adopter_id: int
    surname: str
    name: str
    patronymic: str | None
    phone: str
    address: str | None