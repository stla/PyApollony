from math import sqrt, sin, cos, pi
import numpy as np

def circumcircle(p1, p2, p3):
    "Circle passing through three given points"
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    z = [1.0, 1.0, 1.0]
    A = np.array([x, y, z])
    detA = np.linalg.det(A)
    q1 = x1*x1 + y1*y1
    q2 = x2*x2 + y2*y2
    q3 = x3*x3 + y3*y3
    q = [q1, q2, q3]
    B = np.array([q, y, z])
    detB = np.linalg.det(B)
    C = np.array([q, x, z])
    detC = np.linalg.det(C)
    cx = detB / detA / 2
    cy = -detC / detA / 2
    center = (cx, cy)
    radius = sqrt((x1-cx)*(x1-cx) + (y1-cy)*(y1-cy))    
    return (center, radius)

def inversion(phi, m, radius, c):
    "Inversion"
    mx, my = m
    cx, cy = c
    invphi = 1 / phi
    ix = invphi*radius
    k = radius*radius*(invphi*invphi-1)
    imx = mx - ix - cx
    imy = my - cy
    im2 = imx*imx + imy*imy
    return (ix + cx - k/im2*imx, cy - k/im2*imy)

def oneCircle(phi, center, radius, beta):
    cx, cy = center
    sine = sin(pi/3)
    coef = radius / (1 + sine)
    ptx = cx + coef * cos(beta)
    pty = cy + coef * sin(beta)
    r = coef * sine
    p1 = (ptx + r, pty)
    p2 = (ptx, pty + r)
    p3 = (ptx - r, pty)
    q1 = inversion(phi, p1, radius, center)
    q2 = inversion(phi, p2, radius, center)
    q3 = inversion(phi, p3, radius, center)
    cc, rr = circumcircle(q1, q2, q3)
    ccx, ccy = cc
    return ((ccx - 2/phi*radius, ccy), rr)

def threeCircles(phi, cbig, shift):
    center, radius = cbig
    return (
        oneCircle(phi, center, radius, shift),
        oneCircle(phi, center, radius, shift + 2*pi/3),
        oneCircle(phi, center, radius, shift + 4*pi/3)
    )

