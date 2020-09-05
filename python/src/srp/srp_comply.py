"""An example showing compliance to Single Responsibility Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from pathlib import Path
from typing import Generator, List


class Journal:
    """A simple journal.

    Complies with SRP - persistence is refactored into a separate class.
    """

    def __init__(self) -> None:
        self.entries: List[str] = []
        self.count = 0

    def add_entry(self, entry: str) -> None:
        """Add a journal entry."""
        self.entries.append(f"{self.count}: {entry}")
        self.count += 1

    def remove_entry(self, pos: int) -> None:
        """Remove journal entry at position `pos`."""
        del self.entries[pos]

    def get_entries(self) -> Generator[str, None, None]:
        """Get entries stored in this journal."""
        return (entry for entry in self.entries)


class PersistenceManager:
    """Utility class responsible for persistence."""

    @staticmethod
    def save(journal: Journal, file: Path) -> None:
        """Save journal entries into a file."""
        with open(file, "w") as output:
            output.writelines(f"{entry}\n" for entry in journal.get_entries())

    @staticmethod
    def load(journal: Journal, file: Path) -> None:
        """Load journal entries from a file."""

    @staticmethod
    def load_from_web(journal: Journal, uri: str) -> None:
        """Load journal entries from a URI."""
