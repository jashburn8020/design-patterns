"""Demonstrate Open-Closed Principle."""

from typing import Tuple

import pytest

from ocp import ocp_comply as ocpc
from ocp import ocp_violate as ocpv
from ocp.ocp_common import Colour, Product, Size


@pytest.fixture(name="products")
def fixture_products() -> Tuple[Product, Product, Product]:
    """Return a list of products."""
    apple = Product("Apple", Colour.GREEN, Size.SMALL)
    tree = Product("Tree", Colour.GREEN, Size.LARGE)
    house = Product("House", Colour.BLUE, Size.LARGE)

    return (apple, tree, house)


# Tests verifying behaviour although code violates OCP.


def test_violate_filter_size(products: Tuple[Product, ...]) -> None:
    """Test filter by size."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_size(products, Size.LARGE)
    assert [prod.name for prod in filtered_prods] == ["Tree", "House"]


def test_violate_filter_colour(products: Tuple[Product, ...]) -> None:
    """Test filter by colour."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_colour(products, Colour.GREEN)
    assert [prod.name for prod in filtered_prods] == ["Apple", "Tree"]


def test_violate_filter_size_colour(products: Tuple[Product, ...]) -> None:
    """Test filter by size and colour."""
    prod_filter = ocpv.ProductFilter()
    filtered_prods = prod_filter.filter_by_size_and_colour(
        products, Size.LARGE, Colour.GREEN
    )
    assert [prod.name for prod in filtered_prods] == ["Tree"]


# Tests verifying behaviour after code refactored to comply with OCP.


def test_comply_filter_size(products: Tuple[Product, ...]) -> None:
    """Test filter by size."""
    prod_filter = ocpc.ConcreteFilter()
    filtered_prods = prod_filter.filter(products, ocpc.SizeSpec(Size.LARGE))
    assert [prod.name for prod in filtered_prods] == ["Tree", "House"]


def test_comply_filter_colour(products: Tuple[Product, ...]) -> None:
    """Test filter by colour."""
    prod_filter = ocpc.ConcreteFilter()
    filtered_prods = prod_filter.filter(products, ocpc.ColourSpec(Colour.GREEN))
    assert [prod.name for prod in filtered_prods] == ["Apple", "Tree"]


def test_comply_filter_size_colour(products: Tuple[Product, ...]) -> None:
    """Test filter by size and colour."""
    prod_filter = ocpc.ConcreteFilter()
    large_green_spec = ocpc.AndSpec(
        ocpc.SizeSpec(Size.LARGE), ocpc.ColourSpec(Colour.GREEN)
    )
    filtered_prods = prod_filter.filter(products, large_green_spec)
    assert [prod.name for prod in filtered_prods] == ["Tree"]


def test_comply_generic_spec(products: Tuple[Product, ...]) -> None:
    """Test filter using dynamically created specifications."""
    prod_filter = ocpc.ConcreteFilter()
    green_spec = ocpc.DynamicSpec(lambda item: item.colour == Colour.GREEN)
    green_prods = prod_filter.filter(products, green_spec)
    assert [prod.name for prod in green_prods] == ["Apple", "Tree"]

    large_green_spec = ocpc.DynamicSpec(
        lambda item: item.size == Size.LARGE and item.colour == Colour.GREEN
    )
    large_green_prods = prod_filter.filter(products, large_green_spec)
    assert [prod.name for prod in large_green_prods] == ["Tree"]
