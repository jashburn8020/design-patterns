"""Variation of the Singleton pattern using monostate.

Variation of the Singleton pattern where you put all the state of an object into a
static variable and at the same time you allow people to create new objects. All new
instances will have the same state.
"""


from typing import Any, ClassVar, Dict


class CEO:
    """Monostate CEO."""

    # Static state that all instances share.
    __shared_state: ClassVar[Dict[str, Any]] = {"name": "Steve", "age": 55}

    def __init__(self) -> None:
        # Assign the shared state to your set of attributes. Whenever you construct a
        # new CEO, you will always have the same attributes. Changing the attribute
        # value for 1 instance changes for all instances.
        self.__dict__ = self.__shared_state


def test_monostate_ceo() -> None:
    """Verify `CEO`s `name` and `age` attributes are monostate."""
    steve = CEO()
    assert (steve.name, steve.age) == ("Steve", 55)

    bob = CEO()
    assert (bob.name, bob.age) == ("Steve", 55)

    bob.name = "Bob"
    bob.age = 66
    assert (steve.name, steve.age) == ("Bob", 66)


class Monostate:
    """A more generic monostate implementation - base class for monostate classes.

    This is NOT a good way to implement monostate.
    """

    _shared_state: ClassVar[Dict[str, Any]] = {}

    # See https://docs.python.org/3/reference/datamodel.html#object.__new__
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    """Monostate CFO."""

    def __init__(self) -> None:
        self.name = ""
        self.money_managed = 0


class COO(Monostate):
    """Monostate COO."""

    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary


def test_monostate_cfo() -> None:
    """Verify `CFO`s `name` and `money_managed` attributes are monostate."""
    sheryl = CFO()
    sheryl.name = "Sheryl"
    sheryl.money_managed = 100_000
    sheryl.some_attr = 22

    ruth = CFO()
    assert (ruth.name, ruth.money_managed) == ("", 0)
    assert (sheryl.name, sheryl.money_managed) == ("", 0)
    assert ruth.some_attr == 22

    ruth.name = "Ruth"
    ruth.money_managed = 200_000
    assert (sheryl.name, sheryl.money_managed) == ("Ruth", 200_000)


def test_monostate_coo():
    ben = COO("Ben", salary=100_000)
    assert (ben.name, ben.salary) == ("Ben", 100_000)

    cfo = CFO()
    assert (cfo.name, cfo.money_managed, cfo.salary) == ("", 0, 100_000)
