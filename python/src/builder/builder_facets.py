"""Builder pattern example: building complicated object using multiple builders.

Note: This builder violates OCP because whenever you need to add a sub-builder, you need
to also add it to the parent builder.
"""


from typing import Optional


class Person:
    """Person class recording the person's address and employment info."""

    def __init__(self) -> None:
        """Create a `Person` object with address and employment info unset."""
        # address
        self.street_address: Optional[str] = None
        self.postcode: Optional[str] = None
        self.city: Optional[str] = None
        # employment info
        self.company_name: Optional[str] = None
        self.position: Optional[str] = None
        self.annual_income: Optional[int] = None


class PersonBuilder:
    """Builder to build a person.

    Contains sub-builders to build the person's job and address.
    """

    def __init__(self, person: Optional[Person] = None) -> None:
        """Create a `PersonBuilder` with`person` as a starting template if provided."""
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def works(self) -> "PersonJobBuilder":
        """Return a sub-builder to build the person's job."""
        return PersonJobBuilder(self.person)

    @property
    def lives(self) -> "PersonAddressBuilder":
        """Return a sub-builder to build the person's address."""
        return PersonAddressBuilder(self.person)

    def build(self) -> Person:
        """Return the `Person` object that is built."""
        return self.person


class PersonJobBuilder(PersonBuilder):
    """Sub-builder to build the person's job.

    Inherits `works` and `lives` properties, and `build` method from `PersonBuilder`.
    """

    def __init__(self, person: Person):
        """Create a job sub-builder for the specified `person`."""
        super().__init__(person)

    def at(self, company_name: str) -> "PersonJobBuilder":
        """Set the person's company name."""
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> "PersonJobBuilder":
        """Set the person's job position."""
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> "PersonJobBuilder":
        """Set the person's annual income."""
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    """Sub-builder to build the person's address.

    Inherits `works` and `lives` properties, and `build` method from `PersonBuilder`.
    """

    def __init__(self, person: Person):
        """Create an address sub-builder for the specified `person`."""
        super().__init__(person)

    def at(self, street_address: str) -> "PersonAddressBuilder":
        """Set the person's street address."""
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str) -> "PersonAddressBuilder":
        """Set the person's post code."""
        self.person.postcode = postcode
        return self

    def in_city(self, city: str) -> "PersonAddressBuilder":
        """Set the person's city."""
        self.person.city = city
        return self
