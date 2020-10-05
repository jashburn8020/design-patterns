"""Demonstrate using Builder design pattern."""

from typing import Final

from builder.builder import HtmlElement

# fmt: off
EXP_HELLO: Final[str] = """<p>
  hello
</p>"""

EXP_HELLOS: Final[str] = """<ul>
  <li>
    hello
  </li>
  <li>
    hola
  </li>
</ul>"""
# fmt: on


def test_create_html_manual() -> None:
    """Create HTML elements manually."""
    words = ["hello"]
    parts = ["<p>"]

    for word in words:
        parts.append(f"  {word}")
    parts.append("</p>")

    assert "\n".join(parts) == EXP_HELLO

    words = ["hello", "hola"]
    parts = ["<ul>"]

    for word in words:
        parts.append("  <li>")
        parts.append(f"    {word}")
        parts.append("  </li>")
    parts.append("</ul>")

    assert "\n".join(parts) == EXP_HELLOS


def test_create_html_builder() -> None:
    """Create HTML elements using a builder."""
    builder = HtmlElement.create("p", "hello")
    assert str(builder) == EXP_HELLO

    builder = HtmlElement.create("ul")
    builder.add_child("li", "hello")
    builder.add_child("li", "hola")
    assert str(builder) == EXP_HELLOS


def test_create_html_builder_fluent() -> None:
    """Create HTML elements using a builder with a fluent API."""
    builder = (
        HtmlElement.create("ul")
        .add_child_fluent("li", "hello")
        .add_child_fluent("li", "hola")
    )
    assert str(builder) == EXP_HELLOS
