"""Factory pattern example.

Use a factory class when you have too many factory methods. The class can be separate
(`PointFactory`) or an 'inner' class (`Factory`). The latter eases discovery of its
existence.
"""

from math import cos, isclose, sin


class Point:
    """A point on a plane."""

    def __init__(self, x: float, y: float):
        """Create a point using Cartesian coordinates."""
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        """Two `Point` objects are equal if their coordinates are equal."""
        if not isinstance(other, Point):
            return NotImplemented

        return isclose(self.x, other.x) and isclose(self.y, other.y)

    class Factory:
        """An 'inner' class as factory of `Point` objects.

        This is an alternative to having a factory separate from this (`Point`) class.
        """

        def new_cartesian_point(self, x: float, y: float) -> "Point":
            """Create a point using Cartesian coordinates."""
            return Point(x, y)

        def new_polar_point(self, rho: float, theta: float) -> "Point":
            """Create a point using polar coordinates.

            `theta` is in radians.
            """
            return Point(rho * cos(theta), rho * sin(theta))

    # A convenience member that can be used to get a factory.
    factory = Factory()


class PointFactory:
    """A factory of `Point` objects."""

    def new_cartesian_point(self, x: float, y: float) -> "Point":
        """Create a point using Cartesian coordinates.

        Does not to be a static method.
        """
        return Point(x, y)

    def new_polar_point(self, rho: float, theta: float) -> "Point":
        """Create a point using polar coordinates.

        `theta` is in radians.

        Does not need to be a static method.
        """
        return Point(rho * cos(theta), rho * sin(theta))
