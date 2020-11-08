"""Bridge pattern example.

Circles, squares, and rectangles each can be rendered in vector or raster form.

One way to draw them is by having VectorCircle, VectorSquare, VectorRectangle,
RasterCircle, RasterSquare, and RasterRectangle.

Instead, split the concepts into shapes and renderers.
"""


from abc import ABC, abstractmethod
from unittest import mock

import pytest
from pytest_mock import MockerFixture


class Renderer(ABC):
    """Shape renderer base class."""

    @abstractmethod
    def render_circle(self, radius: int) -> None:
        """Render a circle."""
        # Note: Violates OCP - tied to the shape to be rendered - price to pay for
        # additional flexibility

    @abstractmethod
    def render_square(self, side: int) -> None:
        """Render a square."""

    @abstractmethod
    def render_rectangle(self, horiz_side: int, vert_side: int) -> None:
        """Render a rectangle."""


class VectorRenderer(Renderer):
    """Shape renderer in vector form."""

    def render_circle(self, radius: int) -> None:
        """Render a circle in vector form."""
        # Render as vector image

    def render_square(self, side: int) -> None:
        """Render a square in vector form."""
        # Render as vector image

    def render_rectangle(self, horiz_side: int, vert_side: int) -> None:
        """Render a rectangle."""
        # Render as vector image


class RasterRenderer(Renderer):
    """Shape renderer in raster form."""

    def render_circle(self, radius: int) -> None:
        """Render a circle in raster form."""
        # Render as raster image

    def render_square(self, side: int) -> None:
        """Render a square in raster form."""
        # Render as raster image

    def render_rectangle(self, horiz_side: int, vert_side: int) -> None:
        """Render a rectangle."""
        # Render as raster image


class Shape(ABC):
    """Shape base class."""

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        """Draw the shape."""

    @abstractmethod
    def resize(self, factor: int) -> None:
        """Resize the shape."""


class Circle(Shape):
    """A circular shape."""

    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> None:
        """Draw the circle using the provided renderer."""
        self.renderer.render_circle(self.radius)

    def resize(self, factor: int) -> None:
        """Resize the circle by the specified factor applied to its radius."""
        self.radius *= factor


class Square(Shape):
    """A square shape."""

    def __init__(self, renderer: Renderer, side: int):
        super().__init__(renderer)
        self.side = side

    def draw(self) -> None:
        """Draw the square using the provided renderer."""
        self.renderer.render_square(self.side)

    def resize(self, factor: int) -> None:
        """Resize the square by the specified factor applied to its sides."""
        self.side *= factor


class Rectangle(Shape):
    """A rectangular shape."""

    def __init__(self, renderer: Renderer, horiz_side: int, vert_side: int):
        super().__init__(renderer)
        self.horiz_side = horiz_side
        self.vert_side = vert_side

    def draw(self) -> None:
        """Draw the square using the provided renderer."""
        self.renderer.render_rectangle(self.horiz_side, self.vert_side)

    def resize(self, factor: int) -> None:
        """Resize the rectangle by the specified factor applied to its sides."""
        self.horiz_side *= factor
        self.vert_side *= factor


renderers = (
    pytest.param(RasterRenderer(), id="raster"),
    pytest.param(VectorRenderer(), id="vector"),
)


@pytest.mark.parametrize("renderer", renderers)
def test_circle_rendering(mocker: MockerFixture, renderer: Renderer) -> None:
    """Draw a circle using raster and vector renderers."""
    spy_renderer = mocker.spy(renderer, "render_circle")

    circle = Circle(renderer, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    spy_renderer.assert_has_calls((mock.call(5), mock.call(10)))
    assert spy_renderer.call_count == 2


@pytest.mark.parametrize("renderer", renderers)
def test_square_rendering(mocker: MockerFixture, renderer: Renderer) -> None:
    """Draw a square using raster and vector renderers."""
    spy_renderer = mocker.spy(renderer, "render_square")

    square = Square(renderer, 2)
    square.draw()
    square.resize(3)
    square.draw()
    spy_renderer.assert_has_calls((mock.call(2), mock.call(6)))
    assert spy_renderer.call_count == 2


@pytest.mark.parametrize("renderer", renderers)
def test_rectangle_rendering(mocker: MockerFixture, renderer: Renderer) -> None:
    """Draw a square using raster and vector renderers."""
    spy_renderer = mocker.spy(renderer, "render_rectangle")

    rectangle = Rectangle(renderer, 1, 3)
    rectangle.draw()
    rectangle.resize(2)
    rectangle.draw()
    spy_renderer.assert_has_calls((mock.call(1, 3), mock.call(2, 6)))
    assert spy_renderer.call_count == 2
