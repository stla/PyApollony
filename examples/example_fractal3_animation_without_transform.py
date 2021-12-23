import os
from math import pi, sqrt, cos, sin, tan
import numpy as np
from pyapollony.fractals import fractal3
import pyvista as pv


def satellite(t, R, alpha, k):
    return R * np.array([
        cos(alpha) * cos(t) * cos(k*t) - sin(t) * sin(k*t),
        cos(alpha) * sin(t) * cos(k*t) + cos(t) * sin(k*t),
        sin(alpha) * cos(k*t)
    ])

path = []
nframes = 180
t_ = np.linspace(0, 2*pi, nframes+1)[:nframes]
for i in range(nframes):
    path.append(satellite(t_[i], 2, 3*pi/4, 4))

circles = fractal3(4)
for i, point in enumerate(path):
    pltr = pv.Plotter(window_size=[512, 512], off_screen=True)
    pltr.set_background("#363940")
    pltr.camera.zoom(0.9)
    viewup = pltr._theme.camera["viewup"]
    pltr.set_position(point)
    pltr.set_focus((0,0,0))
    pltr.set_viewup(viewup)
    pltr.renderer.ResetCameraClippingRange()
    for circle in circles:
        center, radius = circle
        sphere = pv.Sphere(radius, center = center+(0,))
        pltr.add_mesh(sphere, smooth_shading=True, color="red", specular=10)
    pngname = "zzpic%03d.png" % i
    pltr.show(screenshot=pngname)

os.system(
    "magick convert -dispose previous -loop 0 -delay 8 zzpic*.png Apollony.gif"    
)