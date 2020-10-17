"""Demonstrate using the Factory design pattern."""

import math
from factory.factory import Point, PointFactory


def test_create_point_inner_factory() -> None:
    """Create `Point` using an 'inner' factory class."""
    normal_constructor_pt = Point(2, 3.46410161514)
    class_factory_cartesian_pt = Point.Factory().new_cartesian_point(2, 3.46410161514)
    assert normal_constructor_pt == class_factory_cartesian_pt

    class_factory_polar_pt = Point.Factory().new_polar_point(4, math.pi / 3)
    assert normal_constructor_pt == class_factory_polar_pt

    member_factory_cartesian_pt = Point.factory.new_cartesian_point(2, 3.46410161514)
    assert normal_constructor_pt == member_factory_cartesian_pt

    member_factory_polar_pt = Point.factory.new_polar_point(4, math.pi / 3)
    assert normal_constructor_pt == member_factory_polar_pt


def test_create_point_external_factory() -> None:
    """Create `Point` using an external factory class."""
    normal_constructor_pt = Point(2, 3.46410161514)
    factory_cartesian_pt = PointFactory().new_cartesian_point(2, 3.46410161514)
    factory_polar_pt = PointFactory().new_polar_point(4, math.pi / 3)

    assert normal_constructor_pt == factory_cartesian_pt == factory_polar_pt
