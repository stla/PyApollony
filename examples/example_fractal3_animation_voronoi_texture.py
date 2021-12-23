import os
from math import pi, sqrt, cos, sin, tan, atan2, asin
import numpy as np
import quaternion
from pyapollony.fractals import fractal3
import pyvista as pv


def transform_matrix_from_rotation_matrix(rotation_matrix):
    return np.vstack(
        (
            np.hstack((rotation_matrix, np.zeros((3,1)))), 
            np.array([0, 0, 0, 1])
        )
    )

def get_quaternion(u ,v): # u and v must be normalized
    "Get a unit quaternion whose corresponding rotation sends u to v"
    d = np.vdot(u, v)
    c = sqrt(1+d)
    r = 1 / sqrt(2) / c
    W = np.cross(u, v)
    arr = np.concatenate((np.array([c/sqrt(2)]), r*W))
    return quaternion.from_float_array(arr)


def satellite(t, R, alpha, k):
    return R * np.array([
        cos(alpha) * cos(t) * cos(k*t) - sin(t) * sin(k*t),
        cos(alpha) * sin(t) * cos(k*t) + cos(t) * sin(k*t),
        sin(alpha) * cos(k*t)
    ])

matrices = []
nframes = 180
t_ = np.linspace(0, 2*pi, nframes+1)
satellite0 = satellite(0, 2, 3*pi/4, 4)
A = satellite0.copy()
q0 = quaternion.from_float_array([1, 0 ,0, 0])
matrices.append(transform_matrix_from_rotation_matrix(
    quaternion.as_rotation_matrix(q0)
))
for i in range(nframes):
    B = satellite(t_[i+1], 2, 3*pi/4, 4)
    q1 = get_quaternion(A/2, B/2) * q0
    rmatrix = quaternion.as_rotation_matrix(q1)
    A = B
    q0 = q1
    matrices.append(transform_matrix_from_rotation_matrix(rmatrix))

path = []
nframes = 180
t_ = np.linspace(0, 2*pi, nframes+1)[:nframes]
for i in range(nframes):
    path.append(satellite(t_[i], 2, 3*pi/4, 4))
    
tex = pv.read_texture("voronoi.jpg")

circles = fractal3(4)
for i, matrix in enumerate(matrices[:nframes]):
    pltr = pv.Plotter(window_size=[512, 512], off_screen=True)
    pltr.add_background_image("SpaceBackground.png")
    #pltr.set_background("#363940")
    pltr.camera.distance = 2.0
    pltr.set_focus((0,0,0))
    pltr.set_position(satellite0)
    pltr.camera.roll = atan2(-matrix[2, 0], matrix[2, 2]) * 180/pi
    pltr.camera.elevation = asin(matrix[2, 1]) * 180/pi
    pltr.camera.azimuth = atan2(-matrix[0, 1], matrix[1, 1]) * 180/pi
    pltr.camera.zoom(1.15)
    for circle in circles:
        center, radius = circle
        sphere = pv.Sphere(radius, center = center+(0,))
        sphere.texture_map_to_sphere(inplace=True)
        pltr.add_mesh(sphere, texture=tex)
    pngname = "zzpic%03d.png" % i
    pltr.show(screenshot=pngname)

os.system(
    "magick convert -dispose previous -loop 0 -delay 8 zzpic*.png ApollonyVoronoiTexture.gif"    
)
