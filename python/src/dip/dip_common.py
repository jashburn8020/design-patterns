"""Common classes etc. used to demonstrate DIP."""

from enum import Enum


class Relationship(Enum):
    """Types of relationships."""

    PARENT = "parent"
    CHILD = "child"
    SIBLING = "sibling"


class Person:
    """Simple `Person` class for setting up relationships."""

    def __init__(self, name: str):
        """Create a person with the specified name."""
        self.name = name
