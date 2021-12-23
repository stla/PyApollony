from pyapollony.fractals import fractal3
import pyvista as pv

circles = fractal3(5)
pltr = pv.Plotter(window_size=[512, 512])
for circle in circles:
    center, radius = circle
    sphere = pv.Sphere(radius, center = center+(0,))
    pltr.add_mesh(sphere, smooth_shading=True, color="red", specular=10)
pltr.camera.zoom(0.9)
pltr.show()
