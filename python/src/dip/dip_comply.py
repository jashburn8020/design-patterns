"""An example showing compliance to Dependency Inversion Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from abc import ABCMeta, abstractmethod
from typing import Generator, List, Tuple

from dip.dip_common import Person, Relationship


class RelationshipBrowser(metaclass=ABCMeta):
    """Interface to provide an abstraction for a low-level module."""

    @abstractmethod
    def find_relationships_for(
        self, name: str
    ) -> Generator[Tuple[Person, Relationship, Person], None, None]:
        """Find relationships for a person with name `name`."""


class Relationships(RelationshipBrowser):
    """Low-level module (class) to track and browse relationships."""

    def __init__(self) -> None:
        """Create a relationship tracker and browser."""
        self._relations: List[Tuple[Person, Relationship, Person]] = []

    def add(self, parent: Person, child: Person) -> None:
        """Add a parent-child relation."""
        self._relations.append((parent, Relationship.PARENT, child))
        self._relations.append((child, Relationship.CHILD, parent))

    def find_relationships_for(
        self, name: str
    ) -> Generator[Tuple[Person, Relationship, Person], None, None]:
        """Find relationships for a person with name `name`.

        Relationship-finding code moved here from `Research`. We can change the
        implementation (e.g., storage mechanism) here and all client code will still
        continue to work as before.
        """
        return (relation for relation in self._relations if relation[0].name == name)


class Research:
    """High-level module (class) with dependency on low-level module's abstraction.

    Complies with DIP - low-level module implementation can change without affecting
    this high-level module.
    """

    def __init__(self, relationships: RelationshipBrowser):
        """Create `Research` with dependency on low-level module's abstraction."""
        self._relationships = relationships

    def report_on(self, name: str) -> Generator[str, None, None]:
        """Report on the relationships for a named person.

        The report is in the form "[name] is a [parent|child|sibling] of [other name]"
        """
        for relation in self._relationships.find_relationships_for(name):
            yield f"{name} is a {relation[1].value} of {relation[2].name}"
