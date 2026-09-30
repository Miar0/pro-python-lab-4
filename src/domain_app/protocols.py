from typing import Protocol, TypedDict
from .value_objects import Money

class PaymentGateway(Protocol):
    def pay(self, amount: Money) -> str:
        ...

class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> None:
        ...

class BookingPayload(TypedDict):
    guest_id: int
    room_number: str
    days: int