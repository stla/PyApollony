import os
from pyapollony.fractals import fractal2
from math import pi
import pyvista as pv
import numpy as np

beta_ = np.linspace(0, 2*pi, 181)[:180]
for i, beta in enumerate(beta_):
    circles = fractal2(5, 0.35, beta)
    pngname = "zpic%03d.png" % i
    pltr = pv.Plotter(window_size=[512, 512], off_screen=True)
    for circle in circles:
        center, radius = circle
        sphere = pv.Sphere(radius, center = center + (0,))
        pltr.add_mesh(sphere, smooth_shading=True, color="red", specular=10)
    pltr.set_position((0, 0, 4.5))
    pltr.set_focus((0, 0, 0))
    pltr.show(screenshot=pngname)

os.system(
    "magick convert -dispose previous -loop 0 -delay 8 zpic*.png ApollonianFractal2.gif"    
)
