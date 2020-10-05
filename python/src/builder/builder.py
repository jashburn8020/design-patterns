"""Builder pattern example."""

from typing import Final, List


class HtmlElement:
    """An HTML element."""

    INDENT_SIZE: Final[int] = 2

    def __init__(self, name: str = "", text: str = ""):
        """Create an HTML element with the given `name` and `text`."""
        self.name = name
        self.text = text
        self.subelements: List[HtmlElement] = []

    def __str(self, indent_level: int) -> str:
        lines: List[str] = []
        indent = " " * (indent_level * self.INDENT_SIZE)
        lines.append(f"{indent}<{self.name}>")

        if self.text:
            indent_text = " " * ((indent_level + 1) * self.INDENT_SIZE)
            lines.append(f"{indent_text}{self.text}")

        for subelement in self.subelements:
            lines.append(subelement.__str(indent_level + 1))

        lines.append(f"{indent}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name: str, text: str = "") -> "HtmlBuilder":
        """Create an `HtmlBuilder` with a `name` root element."""
        return HtmlBuilder(name, text)


class HtmlBuilder:
    """Builder of `HtmlElement`s."""

    def __init__(self, root_name: str, root_text: str = ""):
        """Create a builder of `HtmlElement`s."""
        self.__root = HtmlElement(name=root_name, text=root_text)

    def add_child(self, child_name: str, child_text: str) -> None:
        """Add a child element."""
        self.__root.subelements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name: str, child_text: str) -> "HtmlBuilder":
        """Add a child using a fluent API."""
        self.__root.subelements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)
