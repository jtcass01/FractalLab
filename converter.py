import moviepy.editor as mp

clip = mp.VideoFileClip("mandelbrot_fractal_animation.gif")
clip.write_videofile("mandelbrot_fractal_animation.mp4")