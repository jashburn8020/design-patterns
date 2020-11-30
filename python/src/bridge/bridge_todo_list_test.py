"""Bridge pattern example.

A To Do list with the ability to add and remove strings.

For the Bridge pattern, an element is defined in 2 parts: an abstraction and an
implementation.

The implementation is the class that does all the real work. The general behaviour is
defined in the `ListImpl` interface.

Based on example in "Applied Java Patterns."
"""

from abc import ABC, abstractmethod
from typing import Dict, Generator, List


class ListImpl(ABC):
    """Implementor."""

    @abstractmethod
    def add_item(self, item: str) -> None:
        """Add an item."""

    @abstractmethod
    def get_all_items(self) -> Generator[str, None, None]:
        """Get all items that were previously added."""


class OrderedListImpl(ListImpl):
    """ConcreteImplementor.

    Items are stored in insertion order.
    """

    def __init__(self) -> None:
        self._items: List[str] = []

    def add_item(self, item: str) -> None:
        """Add an item."""
        self._items.append(item)

    def get_all_items(self) -> Generator[str, None, None]:
        """Get all items that were previously added."""
        return (item for item in self._items)


class NonDuplicateListImpl(ListImpl):
    """ConcreteImplementor where duplicate items are ignored.

    Items are stored in insertion order.
    """

    def __init__(self) -> None:
        self._items: Dict[str, None] = {}

    def add_item(self, item: str) -> None:
        """Add an item; if the item already exists, it will not be added."""
        self._items[item] = None

    def get_all_items(self) -> Generator[str, None, None]:
        """Get all items that were previously added, without duplicates."""
        return (item for item in self._items.keys())


class BaseList:
    """Abstraction - operations that are available to the outside world."""

    def __init__(self) -> None:
        """Create an instance with `OrderedListImpl` as the default Implementor."""
        self._impl: ListImpl = OrderedListImpl()

    @property
    def implementor(self) -> ListImpl:
        """Return the Implementor associated with this Abstraction."""
        return self._impl

    @implementor.setter
    def implementor(self, impl: ListImpl) -> None:
        """Set the implementor to be used with this Abstraction."""
        self._impl = impl

    def add(self, item: str) -> None:
        """Add a list item."""
        self._impl.add_item(item)

    def get_all(self) -> str:
        """Get all items in the list."""
        return "\n".join(self._impl.get_all_items())


class NumberedList(BaseList):
    """RefinedAbstraction."""

    def get_all(self) -> str:
        """Get all items in the list, each item is numbered."""
        items = (
            f"{num}. {item}"
            for num, item in enumerate(self.implementor.get_all_items(), 1)
        )
        return "\n".join(items)


def test_base_list() -> None:
    """Verify `BaseList`'s `add()` and `get_all()` with `OrderedListImpl`."""
    base_list = BaseList()
    base_list.add("one")
    base_list.add("two")
    base_list.add("one")

    assert base_list.get_all() == "one\ntwo\none"


def test_numbered_list() -> None:
    """Verify `NumberedList` returns a numbered list."""
    numbered_list = NumberedList()
    numbered_list.add("one")
    numbered_list.add("two")
    numbered_list.add("one")

    assert numbered_list.get_all() == "1. one\n2. two\n3. one"


def test_non_duplicate_list() -> None:
    """Verify `BaseList` ignores duplicate items with `NonDuplicateListImpl`."""
    base_list = BaseList()
    base_list.implementor = NonDuplicateListImpl()
    base_list.add("one")
    base_list.add("two")
    base_list.add("one")

    assert base_list.get_all() == "one\ntwo"


def test_non_duplicate_numberd_list() -> None:
    """Verify `NumberedList` ignores duplicate items with `NonDuplicateListImpl`."""
    numbered_list = NumberedList()
    numbered_list.implementor = NonDuplicateListImpl()
    numbered_list.add("one")
    numbered_list.add("two")
    numbered_list.add("one")

    assert numbered_list.get_all() == "1. one\n2. two"
