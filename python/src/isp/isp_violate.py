"""An example showing violation of Interface Segregation Principle.

Example based on https://www.udemy.com/course/design-patterns-python/.
"""

from isp.isp_common import Document


class Machine:
    """Violates ISP.

    This interface forces your interface users to define methods they do not need.
    """

    def print(self, document: Document) -> None:
        """Print a document."""
        raise NotImplementedError()

    def fax(self, document: Document) -> None:
        """Fax a document."""
        raise NotImplementedError()

    def scan(self, document: Document) -> None:
        """Scan a document."""
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):
    """The `Machine` interface is okay if you need a multi-function device."""

    def print(self, document: Document) -> None:
        """Print a document."""
        document.printed = True

    def fax(self, document: Document) -> None:
        """Fax a document."""
        document.faxed = True

    def scan(self, document: Document) -> None:
        """Scan a document."""
        document.scanned = True


class OldFashionedPrinter(Machine):
    """Does not support faxing and scanning."""

    def print(self, document: Document) -> None:
        """Print a document."""
        document.printed = True

    def fax(self, document: Document) -> None:
        """Not supported.

        One way to handle this is to do nothing. A user of this class will still see
        this method, and may assume this method actually does something.
        """

    def scan(self, document: Document) -> None:
        """Not supported.

        Raising an exception may be fine for simple scripts, but it remains that the
        API for this class defines this method and so someone may still try to use it.
        """
        raise NotImplementedError("Printer cannot scan!")
