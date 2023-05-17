"""Fractal.py: An abstract base class defining a Fractal and its methods."""

__author__ = ['Jacob Taylor Cassady']
__email__ = ['jacobtaylorcassady@outlook.com']

from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from numpy import array
from copy import copy
from matplotlib.pyplot import subplots, show
from matplotlib.animation import FuncAnimation

class Fractal(ABC):
    """Abstract Base Class for a Fractal.

    Args:
        ABC (class): The Abstract Base Class from Python's abc module.

    Returns:
        None: This is an abstract class and should not be directly instantiated."""

    @abstractmethod
    def __init__(self, width: int, height: int, xmin: float,
                 xmax:float, ymin: float, ymax: float) -> None:
        """_summary_

        Args:
            width (int): The width of the fractal.
            height (int): The height of the fractal.
            xmin (float): The minimum x-value for the fractal.
            xmax (float): The maximum x-value for the fractal.
            ymin (float): The minimum y-value for the fractal.
            ymax (float): The maximum y-value for the fractal."""

    @abstractmethod
    def iterate(self) -> array:
        """Iterates the Fractal one step.

        Returns:
            array: A 2D NumPy array representing the state of the fractal after the iteration."""

    def run(self, iterations: int, keep_history: bool = False) -> List[array]:
        """Iterates over the fractal for a given number of iterations.

        Args:
            iterations (int): The number of iterations to run.
            keep_history (bool, optional): Whether to keep a history of each iteration's state. Defaults to False.

        Returns:
            List[array]: The history of each iteration's state, if keep_history is True. Otherwise, returns None."""
        history = []

        for _ in range(iterations):
            if keep_history:
                history.append(copy(self.iterate()))
            else:
                self.iterate()

        return history

    def animate(self, iterations: int, cmap: str = 'gist_stern',
                file_name: Optional[str] = None, show_animation: bool = True,
                xmin: float = -1., xmax: float = 1.,
                ymin: float = -1., ymax: float = 1.,
                figsize: Tuple[int, int] = (8, 8),
                complex_values: bool = False) -> None:
        """Animates the iteration process over a given number of iterations.

        Args:
            iterations (int): The number of iterations to animate.
            cmap (str, optional): The colormap to use for the animation. Defaults to "gist_stern".
            file_name (Optional[str], optional): The name of the file to save the animation as. If None, the animation is not saved. Defaults to None.
            show_animation (bool, optional): Whether to display the animation. Defaults to True.
            xmin (float, optional): The minimum x-value for the plot. Defaults to -1..
            xmax (float, optional): The maximum x-value for the plot. Defaults to 1..
            ymin (float, optional): The minimum y-value for the plot. Defaults to -1..
            ymax (float, optional): The maximum y-value for the plot. Defaults to 1..
            figsize (Tuple[int, int], optional): The size of the figure for the plot. Defaults to (8, 8)."""
        fig, ax = subplots(figsize=figsize)
        frames: List[array] = self.run(iterations=iterations, keep_history=True)

        # Update function for each frame of the animation
        def update(frame):
            ax.clear()
            ax.set_title(f'{self.__class__} (Iteration {frame})')
            ax.axis('off')
            frame = frames[frame]

            if complex_values:
                _ = ax.scatter(frame.real, frame.imag, s=1)
            else:
                _ = ax.imshow(frame, cmap=cmap, extent=(xmin, xmax, ymin, ymax))

        # Create the animation
        animation = FuncAnimation(fig, update, frames=len(frames), interval=10)

        if show_animation:
            show()

        if file_name is not None:
            # Save the animation as a video file
            print(f'Saving {file_name}...')
            if file_name is not None:
                animation.save(file_name, writer='pillow')
