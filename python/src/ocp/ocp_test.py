"""Demonstrate Open-Closed Principle."""

from typing import Tuple

import pytest

from ocp import ocp_comply as ocpc
from ocp import ocp_violate as ocpv
from ocp.ocp_comply import Colour as CColour
from ocp.ocp_comply import Product as CProduct
from ocp.ocp_comply import Size as CSize
from ocp.ocp_violate import Colour as VColour
from ocp.ocp_violate import Product as VProduct
from ocp.ocp_violate import Size as VSize


@pytest.fixture(name="v_products")
def fixture_v_products() -> Tuple[VProduct, VProduct, VProduct]:
    """Return a list of products."""
    apple = VProduct("Apple", VColour.GREEN, VSize.SMALL)
    tree = VProduct("Tree", VColour.GREEN, VSize.LARGE)
    house = VProduct("House", VColour.BLUE, VSize.LARGE)

    return (apple, tree, house)


def test_violate_filter_size(v_products: Tuple[VProduct, ...]) -> None:
    """Test filter by size."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_size(v_products, VSize.LARGE)
    assert list(map(lambda prod: prod.name, filtered_prods)) == ["Tree", "House"]


def test_violate_filter_colour(v_products: Tuple[VProduct, ...]) -> None:
    """Test filter by colour."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_colour(v_products, VColour.GREEN)
    assert list(map(lambda prod: prod.name, filtered_prods)) == ["Apple", "Tree"]


def test_violate_filter_size_colour(v_products: Tuple[VProduct, ...]) -> None:
    """Test filter by size and colour."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_size_and_colour(
        v_products, VSize.LARGE, VColour.GREEN
    )
    assert [*map(lambda prod: prod.name, filtered_prods)] == ["Tree"]


@pytest.fixture(name="c_products")
def fixture_c_products() -> Tuple[CProduct, CProduct, CProduct]:
    """Return a list of products."""
    apple = CProduct("Apple", CColour.GREEN, CSize.SMALL)
    tree = CProduct("Tree", CColour.GREEN, CSize.LARGE)
    house = CProduct("House", CColour.BLUE, CSize.LARGE)

    return (apple, tree, house)


def test_comply_filter_size(c_products: Tuple[CProduct, ...]) -> None:
    """Test filter by size."""
    prod_filter = ocpc.ConcreteFilter()
    filtered_prods = prod_filter.filter(c_products, ocpc.SizeSpec(CSize.LARGE))
    assert list(map(lambda prod: prod.name, filtered_prods)) == ["Tree", "House"]


def test_comply_filter_colour(c_products: Tuple[CProduct, ...]) -> None:
    """Test filter by colour."""
    prod_filter = ocpc.ConcreteFilter()
    filtered_prods = prod_filter.filter(c_products, ocpc.ColourSpec(CColour.GREEN))
    assert list(map(lambda prod: prod.name, filtered_prods)) == ["Apple", "Tree"]


def test_comply_filter_size_colour(c_products: Tuple[CProduct, ...]) -> None:
    """Test filter by size and colour."""
    prod_filter = ocpc.ConcreteFilter()
    large_green_spec = ocpc.AndSpec(
        ocpc.SizeSpec(CSize.LARGE), ocpc.ColourSpec(CColour.GREEN)
    )
    filtered_prods = prod_filter.filter(c_products, large_green_spec)
    assert list(map(lambda prod: prod.name, filtered_prods)) == ["Tree"]


def test_comply_generic_spec(c_products: Tuple[CProduct, ...]) -> None:
    """Test filter using dynamically created specifications."""
    prod_filter = ocpc.ConcreteFilter()
    green_spec = ocpc.DynamicSpec(lambda item: item.colour == CColour.GREEN)
    green_prods = prod_filter.filter(c_products, green_spec)
    assert list(map(lambda prod: prod.name, green_prods)) == ["Apple", "Tree"]

    large_green_spec = ocpc.DynamicSpec(
        lambda item: item.size == CSize.LARGE and item.colour == CColour.GREEN
    )
    large_green_prods = prod_filter.filter(c_products, large_green_spec)
    assert list(map(lambda prod: prod.name, large_green_prods)) == ["Tree"]
