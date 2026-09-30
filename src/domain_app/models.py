from abc import ABC, abstractmethod
from dataclasses import dataclass
from .value_objects import Money

@dataclass
class Guest:
    id: int
    name: str
    email: str

@dataclass
class Room(ABC):
    number: str
    _base_price: Money
    is_available: bool = True

    @property
    @abstractmethod
    def price(self) -> Money:
        ...

    def __str__(self) -> str:
        return f"Room {self.number} ({self.price})"

@dataclass
class StandardRoom(Room):
    has_window: bool = True

    @property
    def price(self) -> Money:
        return self._base_price

@dataclass
class Suite(Room):
    has_minibar: bool = True

    @property
    def price(self) -> Money:
        return Money(self._base_price.amount * 1.5, self._base_price.currency)

@dataclass
class Booking:
    id: int
    guest: Guest
    room: Room
    days: int
    is_active: bool = True

    @property
    def total_price(self) -> Money:
        return Money(self.room.price.amount * self.days, self.room.price.currency)