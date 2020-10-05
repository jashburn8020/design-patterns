"""Demonstrate using Builder design pattern with inheritance to avoid violating OCP."""

from builder.builder_inheritance import PersonBirthDateBuilder


def test_build_person() -> None:
    """Build a `Person` using a derived builder."""
    builder = PersonBirthDateBuilder()
    dmitri = builder.born("1/1/1980").works_as_a("Engineer").called("Dmitri").build()

    assert dmitri.name == "Dmitri"
    assert dmitri.position == "Engineer"
    assert dmitri.date_of_birth == "1/1/1980"
