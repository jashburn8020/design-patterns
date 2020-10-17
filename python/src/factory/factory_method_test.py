"""Demonstrate using the Factory Method design pattern."""

import math

from factory.factory_method import Point


def test_create_point() -> None:
    """Create `Point` using a constructor and factory methods."""
    normal_constructor_pt = Point(2, 3.46410161514)
    cartesian_factory_pt = Point.new_cartesian_point(2, 3.46410161514)
    polar_factory_pt = Point.new_polar_point(4, math.pi / 3)

    assert normal_constructor_pt == cartesian_factory_pt == polar_factory_pt
