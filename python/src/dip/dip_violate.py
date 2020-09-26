"""An example showing violation of Dependency Inversion Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from typing import Generator, List, Tuple

from dip.dip_common import Person, Relationship


class Relationships:
    """Low-level module (class) to track and browse relationships."""

    def __init__(self) -> None:
        """Create a relationship tracker and browser."""
        self.relations: List[Tuple[Person, Relationship, Person]] = []

    def add(self, parent: Person, child: Person) -> None:
        """Add a parent-child relation."""
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class Research:
    """High-level module (class) with dependency on low-level module.

    Violates DIP because it has direct dependency on the low-level module's internal
    storage mechanism. The implementation here breaks if the low-level module changes
    its storage mechanism.
    """

    def __init__(self, relationships: Relationships):
        self.relationships = relationships

    def report_on(self, name: str) -> Generator[str, None, None]:
        """Report on the relationships for a named person.

        The report is in the form "[name] is a [parent|child|sibling] of [other name]"
        """
        for relation in self.relationships.relations:
            if relation[0].name == name:
                yield f"{name} is a {relation[1].value} of {relation[2].name}"
