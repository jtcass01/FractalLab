"""Mandelbrot.py: Implementation of the Mandelbrot Set as a subclass of Fractal."""

__author__ = ['Jacob Taylor Cassady']
__email__ = ['jacobtaylorcassady@outlook.com']

from numpy import linspace, array, meshgrid, zeros, zeros_like

from Fractal import Fractal

class Mandelbrot(Fractal):
    """Mandelbrot Set fractal class.

    Args:
        Fractal (class): The Fractal base class."""

    def __init__(self, width: int, height: int, xmin: float,
                 xmax:float, ymin: float, ymax: float) -> None:
        """Constructor for the Mandelbrot Set fractal class.

        Args:
            width (int): The width of the fractal.
            height (int): The height of the fractal.
            xmin (float): The minimum x-value for the fractal.
            xmax (float): The maximum x-value for the fractal.
            ymin (float): The minimum y-value for the fractal.
            ymax (float): The maximum y-value for the fractal.
        """
        x: array = linspace(xmin, xmax, width)
        y: array = linspace(ymin, ymax, height)
        X, Y = meshgrid(x, y)

        self.constant = X + 1j * Y
        self.z: array = zeros_like(self.constant)
        self.fractal: array = zeros(self.constant.shape, dtype=int)

    def iterate(self) -> array:
        """Performs one iteration of the Mandelbrot set algorithm.

        Returns:
            array: A 2D NumPy array representing the state of the fractal after the iteration.
        """
        mask: array = abs(self.z) < 2
        self.z[mask] = self.z[mask] * self.z[mask] + self.constant[mask]
        self.fractal += mask
        return self.fractal


if __name__ == '__main__':
    # Set the desired parameters
    width, height = 2000, 2000
    xmin, xmax = -2.5, 1.5
    ymin, ymax = -2, 2
    max_iter = 200
    cmap = 'plasma'

    mandelbrot_test: Mandelbrot = \
        Mandelbrot(width=width, height=height, xmin=xmin,
                   xmax=xmax, ymin=ymin, ymax=ymax)
    mandelbrot_test.animate(iterations=100, cmap=cmap, xmin=xmin,
                            xmax=xmax, ymin=ymin, ymax=ymax)
