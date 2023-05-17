"""Julia.py: Implementation of the Julia Set as a subclass of Fractal."""

__author__ = ['Jacob Taylor Cassady']
__email__ = ['jacobtaylorcassady@outlook.com']

from typing import List
from numpy import linspace, array, meshgrid, zeros

from Fractal import Fractal

class Julia(Fractal):
    """Julia Set fractal class.

    Args:
        Fractal (class): The Fractal base class."""
    KNOWN_CONSTANTS: List[complex] = [-0.8 + 0.156j, -0.4 + 0.5j,
                                      -0.618 + 0.0j, -0.7 + 0.27015j,
                                      -0.7269 + 0.1889j, -0.835 - 0.2321j]
    def __init__(self, width: int, height: int, xmin: float,
                 xmax:float, ymin: float, ymax: float,
                 constant: complex = -0.835 - 0.2321j) -> None:
        """Constructor for the Julia Set fractal class.

        Args:
            width (int): The width of the fractal.
            height (int): The height of the fractal.
            xmin (float): The minimum x-value for the fractal.
            xmax (float): The maximum x-value for the fractal.
            ymin (float): The minimum y-value for the fractal.
            ymax (float): The maximum y-value for the fractal.
            constant (complex, optional): The complex constant for the Julia Set. Defaults to -0.835-0.2321j."""
        x: array = linspace(xmin, xmax, width)
        y: array = linspace(ymin, ymax, height)
        X, Y = meshgrid(x, y)

        self.constant = constant
        self.z: array = X + 1j * Y
        self.fractal: array = zeros(self.z.shape, dtype=int)

    def iterate(self) -> array:
        """Performs one iteration of the Julia set algorithm.

        Returns:
            array: A 2D NumPy array representing the state of the fractal after the iteration."""
        mask: array = abs(self.z) < 2
        self.z[mask] = self.z[mask] ** 2 + self.constant
        self.fractal += mask
        return self.fractal


if __name__ == '__main__':
    # Set the desired parameters
    width, height = 1000, 1000
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    max_iter = 100
    cmap = 'gist_stern'

    julia_test: Julia = Julia(width=width, height=height, xmin=xmin, xmax=xmax,
                              ymin=ymin, ymax=ymax, constant=Julia.KNOWN_CONSTANTS[-1])
    julia_test.animate(iterations=100, cmap=cmap, xmin=xmin, xmax=xmax,
                       ymin=ymin, ymax=ymax)
