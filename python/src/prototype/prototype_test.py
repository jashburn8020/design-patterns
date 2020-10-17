"""Prototype pattern example."""

import copy


class Address:
    """A person's address."""

    def __init__(self, street: str, city: str, country: str):
        self.country = country
        self.city = city
        self.street = street

    def __eq__(self, other: object) -> bool:
        """Two `Address` objects are equal if their attributes are equal."""
        if not isinstance(other, Address):
            return NotImplemented

        return (
            self.country == other.country
            and self.city == other.city
            and self.country == other.country
        )


class Person:
    """A person's name and address."""

    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __eq__(self, other: object) -> bool:
        """Two `Person` objects are equal if their names and addresses are equal."""
        if not isinstance(other, Person):
            return NotImplemented

        return self.name == other.name and self.address == other.address


def test_prototype_full() -> None:
    """Use a prototype that is a fully initialised object."""
    address = Address("123 London Road", "London", "UK")
    john = Person("John", address)

    # Use `john` as a prototype.
    jane = copy.deepcopy(john)
    assert jane == john
    assert jane is not john

    jane.name = "Jane"
    assert jane != john
    assert jane.address == john.address
    assert jane.address is not john.address


def test_prototype_partial() -> None:
    """Use a prototype that is a partially initialised object."""
    address_london = Address("", "London", "UK")

    address_john = copy.deepcopy(address_london)
    address_john.street = "123 London Road"
    john = Person("John", address_john)

    expected = Person("John", Address("123 London Road", "London", "UK"))
    assert john == expected
    assert john is not expected
