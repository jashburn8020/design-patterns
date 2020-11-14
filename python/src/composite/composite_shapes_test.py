"""Composite pattern example."""


from abc import ABC, abstractmethod
from math import isclose, pi
from typing import List

import pytest


class GraphicComponent(ABC):
    """Base class for Leaf and Composite classes."""

    def add(self, shape: "GraphicComponent") -> "GraphicComponent":
        """Fails by default with a `NotImplementedError`."""
        raise NotImplementedError("Add operation not implemented")

    @abstractmethod
    def area(self) -> float:
        """Return area of the component."""


class GraphicComposite(GraphicComponent):
    """Container (Composite) to hold a group of Leaf objects together."""

    def __init__(self) -> None:
        self._children: List[GraphicComponent] = []

    def add(self, shape: GraphicComponent) -> GraphicComponent:
        """Add a (Leaf) shape object to this (Composite) graphic object."""
        self._children.append(shape)
        return self

    def area(self) -> float:
        """Return the sum of areas of all its children."""
        return sum(child.area() for child in self._children)


class Circle(GraphicComponent):
    """A circular (Leaf) shape."""

    def __init__(self, radius: int):
        """Create a `Circle` with the specified radius."""
        self.radius = radius

    def area(self) -> float:
        """Return the area of this circle."""
        return pi * self.radius * self.radius


class Square(GraphicComponent):
    """A square (Leaf) shape."""

    def __init__(self, side: int):
        """Create a `Square` with the specified side."""
        self.side = side

    def area(self) -> float:
        """Return the area of this square."""
        return self.side * self.side


def test_circle() -> None:
    """Test `Circle` as a Leaf."""
    circle = Circle(5)
    assert isclose(circle.area(), 78.5398163397)

    with pytest.raises(NotImplementedError):
        circle.add(Circle(1))


def test_square() -> None:
    """Test `Square` as a Leaf."""
    square = Square(5)
    assert square.area() == 25

    with pytest.raises(NotImplementedError):
        square.add(Square(1))


def test_composite() -> None:
    """Test `GraphicComposite` as a Composite.

    The client code operates on both Composite and Leaf objects uniformly.
    """
    circle = Circle(3)
    square = Square(3)
    sub_composite = GraphicComposite().add(Square(4)).add(Square(5))

    main_composite = GraphicComposite().add(circle).add(square).add(sub_composite)

    assert isclose(circle.area(), 28.2743338823)
    assert square.area() == 9
    assert sub_composite.area() == 41
    assert isclose(main_composite.area(), 78.2743338823)
