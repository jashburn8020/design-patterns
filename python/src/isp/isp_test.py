"""Demonstrate Interface Segregation Principle."""
import pytest

from isp.isp_common import Document
from isp.isp_comply import MultiFunctionMachine, Photocopier, PrintOnlyPrinter
from isp.isp_violate import MultiFunctionPrinter, OldFashionedPrinter


@pytest.fixture(name="doc")
def fixture_document() -> Document:
    """Return a `Document` object."""
    return Document()


def test_violate_multifunctionprinter(doc: Document) -> None:
    """Using `MultiFunctionPrinter` is okay even though ISP is violated."""
    printer = MultiFunctionPrinter()
    printer.print(doc)
    printer.fax(doc)
    printer.scan(doc)

    assert doc.printed == doc.faxed == doc.scanned == True


def test_violate_oldfashionedprinter(doc: Document) -> None:
    """Using `OldFashionedPrinter` can lead to surprises."""
    printer = OldFashionedPrinter()
    printer.print(doc)
    assert doc.printed

    printer.fax(doc)
    assert not doc.faxed

    with pytest.raises(NotImplementedError):
        printer.scan(doc)


def test_comply_printonlyprinter(doc: Document) -> None:
    """No extraneous methods in `PrintOnlyPrinter`'s interface."""
    printer = PrintOnlyPrinter()
    printer.print(doc)
    assert doc.printed

    with pytest.raises(AttributeError) as exc_info:
        printer.fax(doc)
    assert "has no attribute 'fax'" in str(exc_info.value)


def test_comply_photocopier(doc: Document) -> None:
    """No extraneous methods in `Photocopier`'s interface."""
    copier = Photocopier()
    copier.print(doc)
    copier.scan(doc)
    assert doc.printed == doc.scanned == True


def test_comply_multifunction(doc: Document) -> None:
    """The `MultiFunction` interface combines the specific interfaces."""
    copier = MultiFunctionMachine()
    copier.print(doc)
    copier.scan(doc)
    copier.fax(doc)
    assert doc.printed == doc.scanned == doc.faxed == True
