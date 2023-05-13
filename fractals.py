import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    fractal = np.zeros(c.shape, dtype=int)

    for i in range(max_iter):
        print("generate_mandelbrot", i, max_iter)
        mask = np.abs(z) < 2
        z[mask] = z[mask] * z[mask] + c[mask]
        fractal += mask

    return fractal

# Set the desired parameters
width, height = 3840, 2160
xmin, xmax = -2.5, 1.5
ymin, ymax = -2, 2
max_iter = 3000

# Update function for each frame of the animation
def update(frame):
    ax.clear()
    ax.set_title("Mandelbrot Set (Iteration {})".format(frame))
    ax.axis('off')
    fractal = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, frame)
    im = ax.imshow(fractal, cmap='hot', extent=(xmin, xmax, ymin, ymax))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Mandelbrot Set")
ax.set_xlabel('Re(c)')
ax.set_ylabel("Im(c)")

# Plot the fractal
# Create the animation
animation = FuncAnimation(fig, update, frames=max_iter+1, interval=100)
# Save the animation as a video file
animation.save('mandelbroth_fractal_animation.gif', writer='pillow')
plt.show()


def generate_julia(width, height, xmin, xmax, ymin, ymax, max_iter, c):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y
    fractal = np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        print("generate_julia", i, max_iter)
        mask = np.abs(z) < 2
        z[mask] = z[mask] ** 2 + c
        fractal += mask

    return fractal
# Set the desired parameters
width, height = 3840, 2160
xmin, xmax = -2, 2
ymin, ymax = -2, 2
max_iter = 10000

# Define the constant for the Julia Set
c = -0.8 + 0.156j

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Julia Set")
ax.axis('off')

# Update function for each frame of the animation
def update(frame):
    ax.clear()
    ax.set_title("Julia Set (Iteration {})".format(frame))
    ax.axis('off')
    fractal = generate_julia(width, height, xmin, xmax, ymin, ymax, frame, c)
    im = ax.imshow(fractal, cmap='hot', extent=(xmin, xmax, ymin, ymax))

# Create the animation
animation = FuncAnimation(fig, update, frames=max_iter+1, interval=100)
# Save the animation as a video file
animation.save('julia_fractal_animation.gif', writer='pillow')
plt.show()

def generate_burning_ship(width, height, xmin, xmax, ymin, ymax, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    fractal = np.zeros(c.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) < 2
        z[mask] = np.abs(z[mask]) ** 2 + c[mask]
        fractal += mask

    return fractal

# Set the desired parameters
width, height = 800, 800
xmin, xmax = -2.5, 1.5
ymin, ymax = -2, 2
max_iter = 100

# Generate the Burning Ship Fractal
fractal = generate_burning_ship(width, height, xmin, xmax, ymin, ymax, max_iter)

# Plot the fractal
plt.figure(figsize=(8, 8))
plt.imshow(fractal, cmap='hot', extent=(xmin, xmax, ymin, ymax))
plt.title("Burning Ship Fractal")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.colorbar(label="Iterations")
plt.show()

def generate_sierpinski(width, height, num_iterations):
    image = np.zeros((height, width), dtype=int)
    image[0, width // 2] = 1

    for i in range(1, height):
        for j in range(1, width - 1):
            if image[i - 1, j] == 1:
                image[i, j - 1] = 1
                image[i, j + 1] = 1

    return image

# Set the desired parameters
width, height = 800, 800
num_iterations = 5

# Generate the Sierpinski Triangle
fractal = generate_sierpinski(width, height, num_iterations)

# Plot the fractal
plt.figure(figsize=(8, 8))
plt.imshow(fractal, cmap='gray', extent=(0, width, 0, height))
plt.title("Sierpinski Triangle")
plt.axis('off')
plt.show()

def generate_koch(width, height, num_iterations):
    image = np.zeros((height, width), dtype=int)
    start = (0, height // 2)
    end = (width, height // 2)
    draw_koch(image, start, end, num_iterations)

    return image

def draw_koch(image, start, end, iterations):
    if iterations == 0:
        draw_line(image, start, end)
    else:
        x1, y1 = start
        x2, y2 = end
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        unit = length / 3

        dx = (x2 - x1) / length
        dy = (y2 - y1) / length

        p1 = (x1 + dx * unit, y1 + dy * unit)
        p2 = (p1[0] + dx * np.cos(np.pi / 3) * unit, p1[1] + dy * np.cos(np.pi / 3) * unit)

        draw_koch(image, start, p1, iterations - 1)
        draw_koch(image, p1, p2, iterations - 1)
        draw_koch(image, p2, end, iterations - 1)

def draw_line(image, start, end):
    x1, y1 = start
    x2, y2 = end
    length = max(abs(x2 - x1), abs(y2 - y1))
    x = np.linspace(x1, x2, int(length), endpoint=False)
    y = np.linspace(y1, y2, int(length), endpoint=False)
    for i in range(int(length)):
        image[int(y[i]), int(x[i])] = 1

# Set the desired parameters
width, height = 800, 800
num_iterations = 5

# Generate the Koch Snowflake
fractal = generate_koch(width, height, num_iterations)

# Plot the fractal
plt.figure(figsize=(8, 8))
plt.imshow(fractal, cmap='gray', extent=(0, width, 0, height))
plt.title("Koch Snowflake")
plt.axis('off')
plt.show()