"""Demonstrate using the Abstract Factory design pattern."""

from factory.abstract_factory import CoffeeFactory, HotDrinkMachine, TeaFactory


def test_abstract_factory() -> None:
    """Create types of hot drinks using abstract factories."""
    machine = HotDrinkMachine()
    machine.register_factory("coffee", CoffeeFactory())
    machine.register_factory("tea", TeaFactory())

    tea = machine.make_drink("tea")
    assert not tea is None and tea.amount() == 200
    tea.consume()
    assert tea.amount() == 0

    coffee = machine.make_drink("coffee")
    assert not coffee is None and coffee.amount() == 50
    coffee.consume()
    assert coffee.amount() == 0
