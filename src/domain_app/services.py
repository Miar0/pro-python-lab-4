from .models import Room, Guest, Booking
from .protocols import PaymentGateway, Notifier
from .repositories import InMemoryRepository
from .value_objects import Money


class HotelService:
    def __init__(
            self,
            payment_gateway: PaymentGateway,
            notifier: Notifier,
            booking_repository: InMemoryRepository[Booking],
    ) -> None:
        self._payment_gateway = payment_gateway
        self._notifier = notifier
        self._bookings = booking_repository
        self._rooms: list[Room] = []

    def add_room(self, room: Room) -> None:
        self._rooms.append(room)

    def get_available_rooms(self) -> list[Room]:
        return [room for room in self._rooms if room.is_available]

    def get_cheapest_room(self) -> Room | None:
        if not self._rooms:
            return None
        return min(self._rooms, key=lambda r: r.price)

    def calculate_potential_income(self) -> Money:
        total_amount = sum((room.price.amount for room in self._rooms), 0.0)
        return Money(total_amount, "UAH")

    def reserve(self, booking_id: int, guest: Guest, room: Room, days: int) -> Booking:
        if not room.is_available:
            raise ValueError(f"Room {room.number} is not available")

        booking = Booking(id=booking_id, guest=guest, room=room, days=days)
        payment_id = self._payment_gateway.pay(booking.total_price)

        room.is_available = False
        self._bookings.add(booking)

        self._notifier.send(
            guest.email,
            f"Reservation confirmed. Room: {room.number}. Payment ref: {payment_id}"
        )
        return booking

    def cancel_reservation(self, booking_id: int) -> None:
        booking = self._bookings.get(booking_id)
        if booking and booking.is_active:
            booking.is_active = False
            booking.room.is_available = True
            self._notifier.send(booking.guest.email, f"Reservation {booking_id} cancelled.")