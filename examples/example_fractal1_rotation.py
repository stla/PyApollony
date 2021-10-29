import os
from pyapollony.fractals import fractal1
from math import pi, cos, sin
import pyvista as pv
import numpy as np

def rmatrix(alpha):
    return np.array([
        [cos(alpha), -sin(alpha), 0, 0],
        [sin(alpha),  cos(alpha), 0, 0],
        [        0,           0,  1, 0],
        [        0,           0,  0, 1]
    ])
matrices = [rmatrix(alpha) for alpha in np.linspace(0, 2*pi, 181)[:180]]

###############################################################################        
circles = fractal1(5)
for i, matrix in enumerate(matrices):
    pngname = "pic%03d.png" % i
    pltr = pv.Plotter(window_size=[512, 512], off_screen=True)
    for circle in circles:
        center, radius = circle
        sphere = pv.Sphere(radius, center = center+(0,))
        pltr.add_mesh(sphere, smooth_shading=True, color="red", specular=10)
    pltr.camera.model_transform_matrix = matrix
    pltr.camera.zoom(1.3)
    pltr.show(screenshot=pngname)
    
os.system(
    "magick convert -dispose previous -loop 0 -delay 8 pic*.png ApollonianFractal1.gif"    
)
