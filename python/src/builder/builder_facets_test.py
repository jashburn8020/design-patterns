"""Demonstrate using Builder design pattern for building complicated objects."""

from copy import copy

from builder.builder_facets import PersonBuilder


def test_build_person() -> None:
    """Build a `Person` using a builder and its sub-builders."""
    builder = PersonBuilder()
    person = (
        builder.lives.at("123 London Road")
        .in_city("London")
        .with_postcode("SW12BC")
        .works.at("Fabrikam")
        .as_a("Engineer")
        .earning(123000)
        .build()
    )

    assert person.street_address == "123 London Road"
    assert person.postcode == "SW12BC"
    assert person.company_name == "Fabrikam"
    assert person.annual_income == 123000


def test_build_person_copy() -> None:
    """Build `Person`s using a `Person` as a template."""
    fabrikam_employee = PersonBuilder().works.at("Fabrikam").build()

    london_engineer = (
        PersonBuilder(copy(fabrikam_employee))
        .lives.in_city("London")
        .works.as_a("Engineer")
        .build()
    )
    assert london_engineer.street_address is None
    assert london_engineer.city == "London"
    assert london_engineer.company_name == "Fabrikam"
    assert london_engineer.position == "Engineer"
    assert london_engineer.annual_income is None

    manager = PersonBuilder(copy(fabrikam_employee)).works.as_a("Manager").build()
    assert manager.city is None
    assert manager.company_name == "Fabrikam"
    assert manager.position == "Manager"
