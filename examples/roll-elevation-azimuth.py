# -*- coding: utf-8 -*-
from math import pi, sqrt, cos, sin, tan, atan2
import numpy as np
import quaternion

# take a unit quaternion:
q = quaternion.from_rotation_vector([1, 2, 3])

# convert it to a rotation matrix:
R = quaternion.as_rotation_matrix(q)

# roll, elevation, azimuth
roll = atan2(R[2, 2], -R[2, 0])
elevation = asin(R[2, 1])
azimuth = atan2(R[1, 1], -R[0, 1])

roll = atan2(-R[2, 0], R[2, 2])
elevation = asin(R[2, 1])
azimuth = atan2(-R[0, 1], R[1, 1])

Ry = np.array([
    [cos(roll), 0, sin(roll) ],
    [0,         1, 0         ],
    [-sin(roll), 0, cos(roll)]    
])

Rx = np.array([
    [1, 0,              0              ],
    [0, cos(elevation), -sin(elevation)],
    [0, sin(elevation), cos(elevation) ]    
])

Rz = np.array([
    [cos(azimuth), -sin(azimuth), 0],
    [sin(azimuth), cos(azimuth),  0],
    [0,            0,             1]    
])

Rz @ Rx @ Ry

R