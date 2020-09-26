"""Demonstrate Dependency Inversion Principle."""

from dip.dip_common import Person
from dip.dip_violate import Relationships as VRelationships
from dip.dip_violate import Research as VResearch
from dip.dip_comply import Relationships as CRelationships
from dip.dip_comply import Research as CResearch


def test_violate_research_on() -> None:
    """Verify `Research` while in violation of DIP."""
    parent = Person("Jayamma")
    child_1 = Person("Adedayo")
    child_2 = Person("Abebi")
    grandparent = Person("Kwento")

    relationships = VRelationships()
    relationships.add(parent, child_1)
    relationships.add(parent, child_2)
    relationships.add(grandparent, parent)

    research = VResearch(relationships)
    assert list(research.report_on("Jayamma")) == [
        "Jayamma is a parent of Adedayo",
        "Jayamma is a parent of Abebi",
        "Jayamma is a child of Kwento",
    ]


def test_comply_research_on() -> None:
    """Verify `Research` works after being refactored to comply with DIP."""
    parent = Person("Jayamma")
    child_1 = Person("Adedayo")
    child_2 = Person("Abebi")
    grandparent = Person("Kwento")

    relationships = CRelationships()
    relationships.add(parent, child_1)
    relationships.add(parent, child_2)
    relationships.add(grandparent, parent)

    research = CResearch(relationships)
    assert list(research.report_on("Jayamma")) == [
        "Jayamma is a parent of Adedayo",
        "Jayamma is a parent of Abebi",
        "Jayamma is a child of Kwento",
    ]
