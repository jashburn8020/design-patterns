"""An example showing violation of Open-Closed Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from enum import Enum
from typing import Generator, Iterable

Colour = Enum("Colour", "RED GREEN BLUE")
Size = Enum("Size", "SMALL MEDIUM LARGE")


class Product:
    """Generic product."""

    def __init__(self, name: str, colour: Colour, size: Size):
        """Create a product of a certain colour and size."""
        self.name = name
        self.colour = colour
        self.size = size


class ProductFilter:
    """Filter products by certain attributes.

    Violates OCP. `ProductFilter` is modified with each new requirement.

    This can cause 'state space explosion' or 'state explosion problem': as the number
    of state variables in the system increases, the size of the system state space
    grows exponentially.

    Filtering by 2 criteria requires 3 or more methods: size, colour, size-and-colour.
    If we consider `OR`, then we also need size-or-colour. With 3 criteria, with just
    `AND`, we need 7 methods: S, C, W (weight), SC, SW, CW, SCW.
    """

    def filter_by_colour(
        self, products: Iterable[Product], colour: Colour
    ) -> Generator[Product, None, None]:
        """Filter products by colour."""
        return (product for product in products if product.colour == colour)

    def filter_by_size(
        self, products: Iterable[Product], size: Size
    ) -> Generator[Product, None, None]:
        """Filter products by size."""
        return (product for product in products if product.size == size)

    def filter_by_size_and_colour(
        self, products: Iterable[Product], size: Size, colour: Colour
    ) -> Generator[Product, None, None]:
        """Filter products by size and colour."""
        return (
            product
            for product in products
            if product.colour == colour and product.size == size
        )
