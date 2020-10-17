"""Prototype pattern example making use of factory methods.

Making deep copies manually can be quite inconvenient. If you have a few predefined
prototypes, it will be convenient to package them into a factory and provide factory
methods to create copies and apply customisation.
"""

import copy
from typing import Final


class Address:
    """An employee's office address."""

    def __init__(self, street: str, suite_number: int, city: str):
        self.suite_number = suite_number
        self.city = city
        self.street = street

    def __eq__(self, other: object) -> bool:
        """Two `Address` objects are equal if their attributes are equal."""
        if not isinstance(other, Address):
            return NotImplemented

        return (
            self.suite_number == other.suite_number
            and self.city == other.city
            and self.street == other.street
        )


class Employee:
    """An employee's name and office address."""

    def __init__(self, name: str, address: Address):
        self.address = address
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Two `Person` objects are equal if their names and addresses are equal."""
        if not isinstance(other, Employee):
            return NotImplemented

        return self.name == other.name and self.address == other.address


class EmployeeFactory:
    """Factory of `Employee`s that makes use of prototypes."""

    # Prototypes
    __main_office_employee: Final[Employee] = Employee(
        "", Address("123 East Dr", 0, "London")
    )
    __aux_office_employee: Final[Employee] = Employee(
        "", Address("123B East Dr", 0, "London")
    )

    @staticmethod
    def __new_employee(prototype: Employee, name: str, suite: int) -> Employee:
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite_number = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int) -> Employee:
        """Create a main office employee (Factory Method)."""
        return EmployeeFactory.__new_employee(
            EmployeeFactory.__main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int) -> Employee:
        """Create an auxiliary office employee (Factory Method)."""
        return EmployeeFactory.__new_employee(
            EmployeeFactory.__aux_office_employee, name, suite
        )


def test_create_office_employees() -> None:
    """Create office employees using prototypes via factory methods."""
    jane = EmployeeFactory.new_main_office_employee("Jane", 100)
    expected_jane = Employee("Jane", Address("123 East Dr", 100, "London"))
    assert jane == expected_jane

    john = EmployeeFactory.new_aux_office_employee("John", 204)
    expected_john = Employee("John", Address("123B East Dr", 204, "London"))
    assert john == expected_john
