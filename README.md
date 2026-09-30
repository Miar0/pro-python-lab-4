# Hotel Booking OOP Domain Model

Лабораторна робота №4 з дисципліни «Професійний Python»

## Опис проєкту

Типізована об'єктна модель предметної області для системи бронювання готелю (Варіант 8)[cite: 1].  
Проєкт демонструє використання професійного об'єктно-орієнтованого програмування в Python: класи, композицію, наслідування, абстрактні базові класи (ABC), протоколи (Protocol), `dataclass`, `properties`, dunder методи, принципи SOLID та сучасну систему type hints[cite: 1]. Також реалізовано патерни Dependency Injection та Repository із використанням `Generic` та `TypeVar`[cite: 1]. Код проходить повну статичну перевірку типів за допомогою `mypy`[cite: 1].

## Структура проєкту (src-layout)

```text
hotel_booking/
│
├── pyproject.toml
├── README.md
├── .gitignore
└── src/
    └── domain_app/
        ├── __init__.py
        ├── main.py
        ├── models.py
        ├── value_objects.py
        ├── protocols.py
        ├── repositories.py
        └── services.py
```

- `value_objects.py` — незмінні (frozen) об'єкти значень з валідацією, наприклад `Money` із перевизначеними dunder методами (`__add__`, `__lt__`, `__str__`)[cite: 1].
- `protocols.py` — структурні інтерфейси (Protocol) для зовнішніх залежностей (`PaymentGateway`, `Notifier`) та `TypedDict`[cite: 1].
- `models.py` — доменні сутності та абстракції (`Room`, `StandardRoom`, `Suite`, `Guest`, `Booking`), побудовані через ABC та dataclasses[cite: 1].
- `repositories.py` — узагальнений (generic) репозиторій колекцій у пам'яті (`InMemoryRepository`), створений за допомогою `TypeVar`[cite: 1].
- `services.py` — application service (`HotelService`), що оркеструє бізнес-логіку з дотриманням принципів SOLID та впровадженням залежностей (Dependency Injection)[cite: 1].
- `main.py` — точка входу: демонстраційний сценарій роботи системи (пошук вільних номерів, бронювання, скасування)[cite: 1].

## Вимоги

- Python 3.12+
- uv
- mypy

## Встановлення та запуск

1. Встановлення залежностей через `uv`:

```bash
uv sync
```

2. Запуск основного демонстраційного сценарію:
*(Переконайтеся, що запускаєте як модуль з папки `src` або з налаштованим `PYTHONPATH`)*

```bash
cd src
uv run python -m domain_app.main
```

3. Перевірка коду статичним типізатором:

```bash
uv run mypy src/domain_app
```

## Приклад роботи програми

```text
--- Вільні номери ---
Room 101 (1000.00 UAH)
Room 201 (3000.00 UAH)

Найвартісніший (найдешевший) номер: Room 101 (1000.00 UAH)
Потенційний дохід готелю за добу: 4000.00 UAH

--- Бронювання ---
[Payment]: Processed 3000.00 UAH
[Email to alex@example.com]: Reservation confirmed. Room: 101. Payment ref: TXN-9981

--- Після бронювання ---
Вільні номери: 1

--- Скасування ---
[Email to alex@example.com]: Reservation 1 cancelled.
Вільні номери після скасування: 2
```

## Автор

Студент: Івасів Данило

Група: ФеП-32