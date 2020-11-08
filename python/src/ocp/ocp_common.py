"""Common classes etc. used to demonstrate OCP."""

from enum import Enum, auto

from dataclasses import dataclass


class Colour(Enum):
    """Enumeration representing colours."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Size(Enum):
    """Enumeration representing sizes."""

    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


@dataclass
class Product:
    """Generic product."""

    name: str
    colour: Colour
    size: Size
