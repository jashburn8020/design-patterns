"""An example showing violation of Single Responsibility Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from pathlib import Path
from typing import Generator, List


class Journal:
    """A simple journal.

    Violates SRP - combines both journal entry manipulation and persistence.
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

    # Breaks SRP.
    # In a larger application, there can be other types that require persistence the
    # same way, and you may want to centrally change the way persistence works, e.g.,
    # to perform some validation before saving.
    def save(self, file: Path) -> None:
        """Save journal entries into a file."""
        with open(file, "w") as output:
            output.writelines(f"{entry}\n" for entry in self.entries)

    def load(self, file: Path) -> None:
        """Load journal entries from a file."""

    def load_from_web(self, uri: str) -> None:
        """Load journal entries from a URI."""
