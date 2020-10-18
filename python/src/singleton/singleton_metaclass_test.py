"""Singleton pattern example using metaclass.

See also https://realpython.com/python-metaclasses/#custom-metaclasses
"""


from typing import Any, ClassVar, Dict


class Singleton(type):
    """Metaclass that creates a Singleton base type when called."""

    # Store class object of type Singleton and an instance of the class
    _instances: ClassVar[Dict["Singleton", Any]] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        # When `SomeClass()` is called (where this metaclass is `SomeClass`'s
        # metaclass), this method is executed.
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

            # The above should be the same as:
            # Singleton._instances[cls] = super().__call__(*args, **kwargs)

        return Singleton._instances[cls]


class DataSource(metaclass=Singleton):
    """Singleton representing a data source."""

    called_num: ClassVar[int] = 0

    def __init__(self) -> None:
        DataSource.called_num += 1


class Resource(metaclass=Singleton):
    """Singleton representing a resource."""

    called_num: ClassVar[int] = 0

    def __init__(self) -> None:
        Resource.called_num += 1


def test_singleton_datasource() -> None:
    """Verify that 1 and only 1 instance is created."""
    data_source_1 = DataSource()
    data_source_2 = DataSource()
    assert DataSource.called_num == 1
    assert data_source_1 is data_source_2

    resource_1 = Resource()
    resource_2 = Resource()
    assert Resource.called_num == 1
    assert resource_1 is resource_2

    data_source_3 = DataSource()
    assert DataSource.called_num == 1
    assert data_source_3 is data_source_1
