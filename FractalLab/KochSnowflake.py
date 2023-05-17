""" ==== NOT WORKING!!! ====


KochSnowflake.py: Implementation of the KochSnowflake Set as a subclass of Fractal."""

__author__ = ['Jacob Taylor Cassady']
__email__ = ['jacobtaylorcassady@outlook.com']

from numpy import linspace, array, meshgrid

from Fractal import Fractal

class KochSnowflake(Fractal):
    """KochSnowflake Set fractal class.

    Args:
        Fractal (class): The Fractal base class."""

    def __init__(self, width: int, height: int, xmin: float,
                 xmax:float, ymin: float, ymax: float) -> None:
        """Constructor for the KochSnowflake Set fractal class.

        Args:
            width (int): The width of the fractal.
            height (int): The height of the fractal.
            xmin (float): The minimum x-value for the fractal.
            xmax (float): The maximum x-value for the fractal.
            ymin (float): The minimum y-value for the fractal.
            ymax (float): The maximum y-value for the fractal."""
        x: array = linspace(xmin, xmax, width)
        y: array = linspace(ymin, ymax, height)
        X, Y = meshgrid(x, y)

        self.constant: array = X + 1j * Y
        self.z: array = self.constant
        self.fractal = self.z

    def iterate(self) -> array:
        """Performs one iteration of the KochSnowflake set algorithm.

        Returns:
            array: A 2D NumPy array representing the state of the fractal after the iteration."""
        mask: array = abs(self.z) < 1
        self.z[mask] = self.z[mask] / 3
        self.fractal[mask] = self.z[mask]
        return self.fractal.real


if __name__ == '__main__':
    # Set the desired parameters
    width, height = 2000, 2000
    xmin, xmax = -2.5, 1.5
    ymin, ymax = -2, 2
    max_iter = 200
    cmap = 'cool'

    koch_snowflake_test: KochSnowflake = \
        KochSnowflake(width=width, height=height, xmin=xmin,
                      xmax=xmax, ymin=ymin, ymax=ymax)
    koch_snowflake_test.animate(iterations=100, cmap=cmap, xmin=xmin,
                                xmax=xmax, ymin=ymin, ymax=ymax, complex_values=True)
