"""Adapter pattern example, with optional caching.

Caching addresses a common problem where too many temporary objects are created by the
adapter.
"""

from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, Dict, Generator, Iterator, List

import pytest


@dataclass(frozen=True)
class Point:
    """Represents a point."""

    x_coord: int
    y_coord: int

    def __str__(self) -> str:
        return f"({self.x_coord}, {self.y_coord})"


class Canvas:
    """A canvas for drawing."""

    def __init__(self) -> None:
        self.points: Dict[Point, None] = {}

    def draw(self, point: Point) -> None:
        """Draw a point on the canvas."""
        self.points[point] = None

    def points_str(self) -> Generator[str, None, None]:
        """Return the points on the canvas in string form.

        Points are returned in the same order in which they were drawn, excluding
        duplicates.
        """
        return (str(point) for point in self.points)


# You are given the above - a `Point` class and a `Canvas` class with a `draw` method
# for `Point` objects.

# You are working with the following - `Line` and `Rectangle` classes. You want to draw
# rectangles.


@dataclass(frozen=True)
class Line:
    """Represents a line with start and end points.

    Frozen - `@lru_cache` used with `LineToPointsAdapter`'s factory method requires
    that arguments to the cached function must be hashable.
    """

    start: Point
    end: Point


class Rectangle:
    """Represents a rectangle consisting of lines for all 4 sides.

    Implements the `Iterable` protocol for iterating through the sides.
    """

    def __init__(self, x_coord: int, y_coord: int, width: int, height: int):
        """Create a `Rectangle` starting from the specified x- and y-coordinates."""
        # A `Rectangle` consists of 4 lines. Each line has a start and end point.
        top_horiz = Line(Point(x_coord, y_coord), Point(x_coord + width, y_coord))
        left_vert = Line(Point(x_coord, y_coord), Point(x_coord, y_coord + height))
        right_vert = Line(
            Point(x_coord + width, y_coord), Point(x_coord + width, y_coord + height)
        )
        bottom_horiz = Line(
            Point(x_coord, y_coord + height), Point(x_coord + width, y_coord + height)
        )

        self.lines = (top_horiz, left_vert, right_vert, bottom_horiz)

    def __iter__(self) -> Iterator[Line]:
        return iter(self.lines)


# You want to draw `Rectangle`s onto `Canvas`.


class LineToPointsAdapter:
    """Represent a line as a series of points.

    This adapter is needed so that the provided `draw` method can be used to draw the
    points that make up a line.

    Implements the `Iterable` protocol for iterating through the points on the sides.
    """

    def __init__(self, line: Line):
        """Represent the specified `line` using a series of points."""
        self.points: List[Point] = []

        left_x_coord = min(line.start.x_coord, line.end.x_coord)
        right_x_coord = max(line.start.x_coord, line.end.x_coord)
        top_y_coord = min(line.start.y_coord, line.end.y_coord)
        bottom_y_coord = max(line.start.y_coord, line.end.y_coord)

        # If it is a horizontal line
        if top_y_coord == bottom_y_coord:
            for x_coord in range(left_x_coord, right_x_coord + 1):
                self.points.append(Point(x_coord, top_y_coord))
        # If it is a vertical line
        elif left_x_coord == right_x_coord:
            for y_coord in range(top_y_coord, bottom_y_coord + 1):
                self.points.append(Point(left_x_coord, y_coord))
        # Support for diagonal lines is deliberately not implemented.

    def __iter__(self) -> Iterator[Point]:
        return iter(self.points)

    @staticmethod
    @lru_cache
    def new_adapter(line: Line) -> "LineToPointsAdapter":
        """Create a new cacheable adapter using a factory method.

        Repeated calls with lines of the same start and end points will return a cached
        instance.
        """
        return LineToPointsAdapter(line)


@pytest.mark.parametrize(
    "adapter", [LineToPointsAdapter, LineToPointsAdapter.new_adapter]
)
def test_draw_rectangle(adapter: Callable[[Line], LineToPointsAdapter]) -> None:
    """Draw a rectangle on the canvas through an adapter.

    The adapter is created through its normal initialiser and its factory method.
    """
    canvas = Canvas()
    rectangle = Rectangle(1, 6, 3, 2)
    for line in rectangle:
        for point in adapter(line):
            canvas.draw(point)

    assert list(canvas.points_str()) == [
        "(1, 6)",
        "(2, 6)",
        "(3, 6)",
        "(4, 6)",
        "(1, 7)",
        "(1, 8)",
        "(4, 7)",
        "(4, 8)",
        "(2, 8)",
        "(3, 8)",
    ]


def test_cache_adapter() -> None:
    """Verify that the cached adapter is returned by the factory method."""
    adapter_1 = LineToPointsAdapter.new_adapter(Line(Point(2, 4), Point(6, 4)))
    adapter_2 = LineToPointsAdapter.new_adapter(Line(Point(2, 4), Point(6, 4)))
    assert adapter_1 is adapter_2

    adapter_3 = LineToPointsAdapter.new_adapter(Line(Point(2, 4), Point(7, 4)))
    adapter_4 = LineToPointsAdapter.new_adapter(Line(Point(2, 4), Point(7, 4)))
    assert adapter_3 is not adapter_1
    assert adapter_3 is adapter_4
