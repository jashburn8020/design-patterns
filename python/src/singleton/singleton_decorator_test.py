"""Singleton pattern example using a decorator.

See also https://realpython.com/primer-on-python-decorators/#creating-singletons
"""

import functools
from typing import Any, Callable, ClassVar, Dict, Optional, Tuple, Type, TypeVar

T = TypeVar("T")


def singleton(class_: Type[T]) -> Callable[..., T]:
    """Class decorator to enforce singleton."""
    # Called once for every class that is decorated.

    instance: Optional[T] = None

    @functools.wraps(class_)
    def wrapper_singleton(*args: Tuple[Any], **kwargs: Dict[str, Any]) -> T:
        # Called once every time the class is instantiated (i.e., `SomeClass()`)
        nonlocal instance
        if instance is None:
            instance = class_(*args, **kwargs)

        return instance

    return wrapper_singleton


@singleton
class DataSource:
    """Singleton representing a data source."""

    called: ClassVar[int] = 0

    def __init__(self) -> None:
        DataSource.called += 1


@singleton
class Resource:
    """Singleton representing a resource."""

    called: ClassVar[int] = 0

    def __init__(self) -> None:
        Resource.called += 1


def test_singleton_datasource() -> None:
    """Verify that 1 and only 1 instance is created."""
    data_source_1 = DataSource()
    data_source_2 = DataSource()
    assert DataSource.called == 1
    assert data_source_1 is data_source_2

    resource_1 = Resource()
    resource_2 = Resource()
    assert Resource.called == 1
    assert resource_1 is resource_2

    data_source_3 = DataSource()
    assert DataSource.called == 1
    assert data_source_3 is data_source_1
