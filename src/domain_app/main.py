from .models import Guest, StandardRoom, Suite, Booking
from .repositories import InMemoryRepository
from .services import HotelService
from .value_objects import Money


class ConsoleNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email to {recipient}]: {message}")


class DemoPaymentGateway:
    def pay(self, amount: Money) -> str:
        print(f"[Payment]: Processed {amount}")
        return "TXN-9981"


def main() -> None:
    booking_repo = InMemoryRepository[Booking]()
    service = HotelService(
        payment_gateway=DemoPaymentGateway(),
        notifier=ConsoleNotifier(),
        booking_repository=booking_repo,
    )

    room1 = StandardRoom(number="101", _base_price=Money(1000))
    room2 = Suite(number="201", _base_price=Money(2000))
    service.add_room(room1)
    service.add_room(room2)

    guest = Guest(id=1, name="Олександр", email="alex@example.com")

    print("--- Вільні номери ---")
    for r in service.get_available_rooms():
        print(r)

    print(f"\nНайвартісніший (найдешевший) номер: {service.get_cheapest_room()}")
    print(f"Потенційний дохід готелю за добу: {service.calculate_potential_income()}")

    print("\n--- Бронювання ---")
    booking = service.reserve(booking_id=1, guest=guest, room=room1, days=3)

    print("\n--- Після бронювання ---")
    print(f"Вільні номери: {len(service.get_available_rooms())}")

    print("\n--- Скасування ---")
    service.cancel_reservation(booking.id)
    print(f"Вільні номери після скасування: {len(service.get_available_rooms())}")


if __name__ == "__main__":
    main()