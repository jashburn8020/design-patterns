"""Demonstrate Liskov Substitution Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""


class Rectangle:
    """Base class."""

    def __init__(self, width: int, height: int):
        """Create a `Rectangle` with a certain width and height."""
        self._height = height
        self._width = width

    @property
    def width(self) -> int:
        """Get the width of the `Rectangle`."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value

    @property
    def height(self) -> int:
        """Get the height of the `Rectangle`."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    @property
    def area(self) -> int:
        """Get the area of the `Rectangle`."""
        return self._width * self._height


class Square(Rectangle):
    """Derived class that violates LSP."""

    def __init__(self, side: int):
        """Create a `Square` with a certain side length."""
        Rectangle.__init__(self, side, side)

    @Rectangle.width.setter
    def width(self, value: int) -> None:
        """Set the width of the Square, which also set the height."""
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value: int) -> None:
        """Set the height of the Square, which also set the width."""
        self._width = self._height = value


def area_height_10(shape: Rectangle) -> int:
    """Area of the `Rectangle`-based shape when the height is 10.

    This function presumes `shape`'s width and height are independent, which is true
    for `Rectangle` but not for `Square`, and so it does not return the right area for
    `Square`. Therefore `Square` violates LSP because `Square` (subtype) is not
    substitutable for `Rectangle` (its base type).
    """
    width = shape.width
    shape.height = 10

    return width * shape.height


def test_rectangle() -> None:
    """`Rectangle` works as expected."""
    rectangle = Rectangle(2, 3)
    assert rectangle.area == 6
    assert area_height_10(rectangle) == 20


def test_square() -> None:
    """Demonstrate `area_height_10` breaks with `Square`."""
    square = Square(5)
    assert square.area == 25

    new_area = area_height_10(square)
    # They should be the same
    assert new_area != Square(10).area

    assert new_area == 50
