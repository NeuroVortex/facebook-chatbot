from typing import NamedTuple

from src.services.crm.contract.client import Client
from src.services.crm.contract.reservation import Reservation


class Appointment(NamedTuple):
    id: int
    selected_services: list[int]
    description: str
    client: Client
    reservation: Reservation