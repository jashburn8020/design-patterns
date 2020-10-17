"""Abstract Factory example.

If you have a hierarchy of types, then you can have a corresponding hierarchy of
factories. You can have an abstract factory as a base class for other factories.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional

# Hierarchy of types.


class HotDrink:
    """Base class for hot drinks."""

    def __init__(self, volume: int):
        """Create a hot drink of a specific amount."""
        self._volume = volume

    def consume(self) -> None:
        """Consume the hot drink completely."""
        self._volume = 0

    def amount(self) -> int:
        """Amount of hot drink available."""
        return self._volume


class Tea(HotDrink):
    """Tea, a type of hot drink."""


class Coffee(HotDrink):
    """Coffee, a type of hot drink."""


# Hierarchy of factories for the above types.


class HotDrinkFactory(ABC):
    """Abstract base class for the factories of specific hot drinks.

    This is not really necessary with Python due to duck typing, but it gives you an
    idea of the API you are expected to implement.
    """

    @abstractmethod
    def prepare(self) -> HotDrink:
        """Prepare the specified volume of a hot drink.

        In general, perform operations to set up the object.
        """


class TeaFactory(HotDrinkFactory):
    """Factory for `Tea`-type hot drink."""

    def prepare(self) -> Tea:
        """Prepare a `Tea` hot drink."""
        return Tea(200)


class CoffeeFactory(HotDrinkFactory):
    """Factory for `Coffee`-type hot drink."""

    def prepare(self) -> Coffee:
        """Prepare a `Coffee`-type hot drink."""
        return Coffee(50)


class HotDrinkMachine:
    """Hot drink dispensing machine."""

    def __init__(self) -> None:
        self._factories: Dict[str, HotDrinkFactory] = {}

    def register_factory(self, drink_name: str, drink_factory: HotDrinkFactory) -> None:
        """Register a hot drink factory."""
        self._factories[drink_name] = drink_factory

    def make_drink(self, drink_name: str) -> Optional[HotDrink]:
        """Return a hot drink, or `None` if its factory has not been registered."""
        factory = self._factories.get(drink_name)
        return factory.prepare() if not factory is None else None
