"""Demonstrate Single Responsibility Principle."""

from pathlib import Path

from srp import srp_comply
from srp import srp_violate


def test_violate_add_entry() -> None:
    """Verify `Journal`'s main responsibility."""
    journal = srp_violate.Journal()
    journal.add_entry("test 1")
    journal.add_entry("test 2")

    assert list(journal.get_entries()) == ["0: test 1", "1: test 2"]


def test_violate_save(tmp_path: Path) -> None:
    """Verify `Journal`'s extraneous responsibility."""
    journal = srp_violate.Journal()
    journal.add_entry("test 1")
    journal.add_entry("test 2")

    output = tmp_path.joinpath("test.txt")
    journal.save(output)

    with open(output) as file:
        data = file.read()
    assert data == "0: test 1\n1: test 2\n"


def test_comply_save(tmp_path: Path) -> None:
    """Verify SRP-compliant saving journal entries to file."""
    journal = srp_comply.Journal()
    journal.add_entry("test 1")
    journal.add_entry("test 2")

    output = tmp_path.joinpath("test.txt")
    srp_comply.PersistenceManager.save(journal, output)

    with open(output) as file:
        data = file.read()
    assert data == "0: test 1\n1: test 2\n"
