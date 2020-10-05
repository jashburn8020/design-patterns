"""Builder pattern example: using inheritance to avoid violating OCP.

Whenever you need to add more information, you inherit from a builder that you've
already got.
"""


from typing import Optional, TypeVar


class Person:
    """Person class recording the person's name, job position, and date of birth."""

    def __init__(self) -> None:
        self.name: Optional[str] = None
        self.position: Optional[str] = None
        self.date_of_birth: Optional[str] = None


T = TypeVar("T", bound="PersonBuilder")


class PersonBuilder:
    """Root builder to be inherited to build various aspects of the `Person` object."""

    def __init__(self) -> None:
        self.person = Person()

    def build(self) -> Person:
        """Build the `Person` object."""
        return self.person


# You can have any number of builders through inheritance to initialise various aspects
# of Person.


class PersonInfoBuilder(PersonBuilder):
    """Build a `Person` along with the person's personal information."""

    def called(self: T, name: str) -> T:
        """Set the person's name."""
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    """Build a `Person` along with the person's personal and job information."""

    def works_as_a(self: T, position: str) -> T:
        """Set the person's job position."""
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    """Build a `Person` along with the person's personal and job information, and birth date."""

    def born(self: T, date_of_birth: str) -> T:
        """Set the person's date of birth."""
        self.person.date_of_birth = date_of_birth
        return self
