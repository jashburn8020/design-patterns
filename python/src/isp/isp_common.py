"""Common classes etc. used to demonstrate ISP."""


class Document:
    """A document that can be processed by a machine."""

    def __init__(self) -> None:
        """Create a document."""
        self.printed = False
        self.scanned = False
        self.faxed = False
