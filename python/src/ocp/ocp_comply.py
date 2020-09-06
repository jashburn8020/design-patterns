"""An example showing compliance to Open-Closed Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""
from enum import Enum
from typing import Any, Callable, Generator, Iterable

Colour = Enum("Colour", "RED GREEN BLUE")
Size = Enum("Size", "SMALL MEDIUM LARGE")


class Product:
    """Generic product."""

    def __init__(self, name: str, colour: Colour, size: Size):
        """Create a product of a certain colour and size."""
        self.name = name
        self.colour = colour
        self.size = size


class Specification:
    """Base class to determine if an item is satisfied by a particular criterion."""

    def is_satisfied(self, item: Any) -> bool:
        """Return `True` if `item` meets this specification."""


# Each new specification is added as a separate class rather than by modifying existing
# code.


class ColourSpec(Specification):
    """Colour-based specification."""

    def __init__(self, colour: Colour) -> None:
        """Create a specification for a specific colour."""
        self.colour = colour

    def is_satisfied(self, item: Product) -> bool:
        """Return `True` if `item`'s colour meets this specification."""
        return item.colour == self.colour


class SizeSpec(Specification):
    """Size-based specification."""

    def __init__(self, size: Size) -> None:
        """Create a specification for a specific size."""
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        """Return `True` if `item`'s size meets this specification."""
        return item.size == self.size


class AndSpec(Specification):
    """Combinator specification - combines multiple specifications into one."""

    def __init__(self, *specs: Specification) -> None:
        """Create a specification using a combination of specifications."""
        self.specs = specs

    def is_satisfied(self, item: Product) -> bool:
        """Return `True` if `item` meets all the specifications."""
        return all(map(lambda spec: spec.is_satisfied(item), self.specs))


class DynamicSpec(Specification):
    """Specification whose satisfaction logic can be provided dynamically."""

    def __init__(self, satisfied: Callable[[Product], bool]) -> None:
        """Create a specification using the provided satisfaction logic."""
        self.satisfied = satisfied

    def is_satisfied(self, item: Product) -> bool:
        """Return `True` if `item` meets the satisfaction logic."""
        return self.satisfied(item)


class Filter:
    """Base class to filter items by some specification."""

    def filter(
        self, items: Iterable[Any], spec: Specification
    ) -> Generator[Any, None, None]:
        """Return items that meet the specification specified by `spec`."""


class ConcreteFilter(Filter):
    """Concrete filter to filter items based on a specification.

    Implement logic in a subclass so that if we want to use a different filtering logic,
    we can create a new concrete filter inheriting from `Filter` rather than changing
    it here - closed for modification, open for extension.
    """

    def filter(
        self, items: Iterable[Product], spec: Specification
    ) -> Generator[Product, None, None]:
        """Return products that meet the specification specified by `spec`."""
        return (item for item in items if spec.is_satisfied(item))
