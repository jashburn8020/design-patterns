"""Factory Method pattern example."""

from math import cos, isclose, sin


class Point:
    """A point on a plane."""

    def __init__(self, x: float, y: float):
        """Create a point using Cartesian coordinates."""
        self.x = x
        self.y = y

    # Redeclaration won't work for polar coordinates.
    #
    # def __init__(self, rho, theta):

    # Without factory methods, we will need to have a complicated constructor, which
    # gets increasingly complicated with each new coordinate system.
    #
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     """Create a point using a coordinate system.
    #
    #     With Cartesian coordinates, `a` and `b` are x and y coordinates.
    #     With polar coordinates, `a` and `b` are ρ and θ (in radians).
    #     """
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    # Factory methods

    @staticmethod
    def new_cartesian_point(x: float, y: float) -> "Point":
        """Create a point using Cartesian coordinates."""
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float) -> "Point":
        """Create a point using polar coordinates.

        `theta` is in radians.
        """
        return Point(rho * cos(theta), rho * sin(theta))

    def __eq__(self, other: object) -> bool:
        """Two `Point` objects are equal if their coordinates are equal."""
        if not isinstance(other, Point):
            return NotImplemented

        return isclose(self.x, other.x) and isclose(self.y, other.y)
