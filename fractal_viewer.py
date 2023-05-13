import numpy as np
from pyqtgraph import GraphicsView, PlotItem, ImageItem, colormap, ColorMap, GraphicsLayoutWidget
from sys import argv, exit as sys_exit
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from qdarkstyle import load_stylesheet
from typing import Callable
import cv2

class JuliaAnimation(QMainWindow):
    def __init__(self, width, height, xmin, xmax, ymin, ymax, max_iter, c):
        super().__init__()

        self.width = width
        self.height = height
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.max_iter = max_iter
        self.c = c

        self.view = GraphicsView()
        self.setCentralWidget(self.view)

        self.view.setBackground('w')
        self.plot_item = PlotItem()
        self.view.setCentralItem(self.plot_item)

        self.graphics_layout = GraphicsLayoutWidget()

        self.plot_item.setRange(xRange=[self.xmin, self.xmax], yRange=[self.ymin, self.ymax])
        self.plot_image = ImageItem()
        self.plot_item.addItem(self.plot_image)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_fractal)
        self.timer.start(100)  # Update interval in milliseconds

        self.frame_counter = 0
        self.video_writer = None

        self.setCentralWidget(self.view)

        print("Hmm.")

    def generate_julia(self):
        x = np.linspace(self.xmin, self.xmax, self.width)
        y = np.linspace(self.ymin, self.ymax, self.height)
        X, Y = np.meshgrid(x, y)
        z = X + 1j * Y
        fractal = np.zeros(z.shape, dtype=int)

        for i in range(self.max_iter):
            mask = np.abs(z) < 2
            z[mask] = z[mask] ** 2 + self.c
            fractal += mask

        return fractal

    def update_fractal(self):
        fractal = self.generate_julia()
        self.plot_image.setImage(fractal, autoLevels=True, levels=(0, self.max_iter))
        lut = ColorMap([0, 0.5, 1], [(0, 0, 0), (255, 255, 255), (255, 0, 0)])
        self.plot_image.setLookupTable(lut)

        # Save each frame as an image
        print(self.view.size())
        pixmap = QPixmap(self.view.size())
        painter: QPainter = QPainter(pixmap)
        self.view.render(painter)
        self.view.update()
        image = pixmap.toImage()

        if self.video_writer is None:
            fps = 10  # Frames per second
            codec = cv2.VideoWriter_fourcc(*"mp4v")  # Video codec
            file_name = "julia_set_animation.mp4"  # Output video file name
            self.video_writer = cv2.VideoWriter(file_name, codec, fps, image.width(), image.height())

        image = image.convertToFormat(QImage.Format_RGB888)
        frame_data = image.bits().asstring(image.byteCount())
        frame = np.frombuffer(frame_data, dtype=np.uint8).reshape(image.height(), image.width(), 3)

        # Convert RGB to BGR format (required by OpenCV)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        self.video_writer.write(frame)
        self.frame_counter += 1

        # Stop the animation after a certain number of frames
        if self.frame_counter >= self.max_iter:
            self.timer.stop()
            self.video_writer.release()

            print("Video saved successfully.")

class FractalViewer:
    def __init__(self) -> None:
        self.generated_windows = {}

    def open_window(self, window: QMainWindow) -> None:
        if window.__class__ in self.generated_windows.keys():
            self.generated_windows[window.__class__].append(window)
        else:
            self.generated_windows[window.__class__] = [window]

        window.show()


if __name__ == "__main__":
    # Set the desired parameters
    width, height = 800, 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    max_iter = 100

    # Define the constant for the Julia Set
    c = -0.8 + 0.156j

    # Create the application instance
    app = QApplication(argv)

    # Create the Julia Animation window
    window: JuliaAnimation = JuliaAnimation(width, height, xmin, xmax, ymin, ymax, max_iter, c)
    fractal_viewer: FractalViewer = FractalViewer()

    # app.setStyleSheet(load_stylesheet(pyside=True))
    fractal_viewer.open_window(window=window)

    sys_exit(app.exec())