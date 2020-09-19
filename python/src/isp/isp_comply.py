"""An example showing compliance to Interface Segregation Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from abc import abstractmethod, ABCMeta
from isp.isp_common import Document

# Instead of having a large interface, we can split it into small interfaces so that
# people can implement what they need.


class Printer(metaclass=ABCMeta):
    """Interface for a machine that can print documents."""

    @abstractmethod
    def print(self, document: Document) -> None:
        """Print a document."""


class Scanner(metaclass=ABCMeta):
    """Interface for a machine that can scan documents."""

    @abstractmethod
    def scan(self, document: Document) -> None:
        """Scan a document."""


class Facsimile(metaclass=ABCMeta):
    """Interface for a machine that can fax documents."""

    @abstractmethod
    def fax(self, document: Document) -> None:
        """Fax a document."""


class PrintOnlyPrinter(Printer):
    """A printer that only prints."""

    def print(self, document: Document) -> None:
        """Print a document."""
        document.printed = True


class Photocopier(Printer, Scanner):
    """A photocopier scans and prints documents."""

    def print(self, document: Document) -> None:
        """Print a document."""
        document.printed = True

    def scan(self, document: Document) -> None:
        """Scan a document."""
        document.scanned = True


class MultiFunction(Printer, Scanner, Facsimile):
    """If you really need an interface with all the different methods."""

    @abstractmethod
    def print(self, document: Document) -> None:
        """Print a document."""

    @abstractmethod
    def scan(self, document: Document) -> None:
        """Scan a document."""

    @abstractmethod
    def fax(self, document: Document) -> None:
        """Fax a document."""


class MultiFunctionMachine(MultiFunction):
    """This is the same as `isp_violate.MultiFunctionPrinter`."""

    def print(self, document: Document) -> None:
        """Print a document."""
        document.printed = True

    def fax(self, document: Document) -> None:
        """Fax a document."""
        document.faxed = True

    def scan(self, document: Document) -> None:
        """Scan a document."""
        document.scanned = True
