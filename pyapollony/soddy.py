# -*- coding: utf-8 -*-
from math import sqrt
import cmath
import numpy as np


def soddyRadius(r1, r2, r3, sign = 1):
    "The Soddy radius corresponding to three radii"
    return 1 / (1/r1 + 1/r2 + 1/r3 + sign*2*sqrt(1/r1/r2 + 1/r2/r3 + 1/r3/r1))

def soddyCenter(p1, p2, p3):
    "The Soddy center associated to three points"
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    a = np.linalg.norm(p2 - p3)
    b = np.linalg.norm(p1 - p3)
    c = np.linalg.norm(p1 - p2)
    u1 = x2 - x1
    u2 = y2 - y1
    v1 = x3 - x1
    v2 = y3 - y1
    delta = abs(u1*v2 - u2*v1)
    tc1 = 1 + delta / a / (b + c - a)
    tc2 = 1 + delta / b / (c + a - b)
    tc3 = 1 + delta / c / (a + b - c)
    den = a*tc1 + b*tc2 + c*tc3
    k1 = a*tc1 / den
    k2 = b*tc2 / den
    k3 = c*tc3 / den
    return (k1*x1 + k2*x2 + k3*x3, k1*y1 + k2*y2 + k3*y3)

def soddyCircle1(c1, c2, c3):
    "Soddy circle associated to three circles"
    p1, r1 = c1
    p2, r2 = c2
    p3, r3 = c3
    return (soddyCenter(p1, p2, p3), soddyRadius(r1, r2, r3))

def soddyCircle2(c1, c2, c3):
    "Soddy circle associated to three circles when the third one is exterior"
    p1, r1 = c1
    p2, r2 = c2
    p3, r3 = c3
    r = soddyRadius(r1, r2, -r3)
    z1 = complex(*p1)
    z2 = complex(*p2)
    z3 = complex(*p3)
    term1 = z1/r1 + z2/r2 - z3/r3
    term2 = 2 * cmath.sqrt(z1*z2/r1/r2 - z2*z3/r2/r3 - z1*z3/r1/r3)
    center1 = r * (term1-term2)
    center2 = r * (term1+term2)
    center1_x = center1.real
    center1_y = center1.imag
    center2_x = center2.real
    center2_y = center2.imag
    c3_x, c3_y = p3
    cc13_x = center1_x - c3_x
    cc13_y = center1_y - c3_y
    cc23_x = center2_x - c3_x
    cc23_y = center2_y - c3_y
    d1 = cc13_x*cc13_x + cc13_y*cc13_y
    d2 = cc23_x*cc23_x + cc23_y*cc23_y
    return ((center1_x, center1_y), r) if d1 > d2 else ((center2_x, center2_y), r) 

def soddyCircle3(c1, c2, c3, rother):
    "Soddy circle used by the 'fractal2' function"
    p1, r1 = c1
    p2, r2 = c2
    p3, r3 = c3
    r0 = soddyRadius(r1, r2, -r3)
    if abs((r0-rother)/r0) < 0.001:
        r = soddyRadius(r1, r2, -r3, -1)
        other = True
    else:
        r = r0
        other = False
    z1 = complex(*p1)
    z2 = complex(*p2)
    z3 = complex(*p3)
    term1 = z1/r1 + z2/r2 - z3/r3
    term2 = 2 * cmath.sqrt(z1*z2/r1/r2 - z2*z3/r2/r3 - z1*z3/r1/r3)
    center1 = r * (term1-term2)
    center2 = r * (term1+term2)
    center1_x = center1.real
    center1_y = center1.imag
    center1 = (center1_x, center1_y)
    center2_x = center2.real
    center2_y = center2.imag
    center2 = (center2_x, center2_y)
    c3_x, c3_y = p3
    cc13_x = center1_x - c3_x
    cc13_y = center1_y - c3_y
    cc23_x = center2_x - c3_x
    cc23_y = center2_y - c3_y
    d1 = cc13_x*cc13_x + cc13_y*cc13_y
    d2 = cc23_x*cc23_x + cc23_y*cc23_y
    comparison = d1 < d2 if other else d1 > d2
    return (center1, r) if comparison else (center2, r)

