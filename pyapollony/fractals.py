# -*- coding: utf-8 -*-
from math import sqrt
from .soddy import soddyCircle1, soddyCircle2, soddyCircle3
from .threecircles import threeCircles
from itertools import chain

def apollony1(c1, c2, c3, exterior, n):
    "Helper function for 'fractal1'"
    circle = soddyCircle2(c1, c2, c3) if exterior else soddyCircle1(c1, c2, c3)
    if n == 1:
        return [circle]
    else:
        return (
            apollony1(c1, c2, circle, False, n-1)
            + apollony1(c1, circle, c3, exterior, n-1)
            + apollony1(circle, c2, c3, exterior, n-1)
        )

def fractal1(n):
    "List of circles of the Apollonian gasket"
    c1 = ((1, -1/sqrt(3)), 1)
    c2 = ((-1, -1/sqrt(3)), 1)
    c3 = ((0, sqrt(3) - 1/sqrt(3)), 1)
    c4 = ((0, 0), 2 + 1/(3+2*sqrt(3)))
    l1 = [apollony1(c1, c2, c3, False, i) for i in range(1, n+1)]
    l2 = [apollony1(c1, c2, c4, True, i) for i in range(1, n+1)]
    l3 = [apollony1(c1, c3, c4, True, i) for i in range(1, n+1)]
    l4 = [apollony1(c2, c3, c4, True, i) for i in range(1, n+1)]
    return (
        list(chain(*l1)) + list(chain(*l2)) 
        + list(chain(*l3)) + list(chain(*l4))
    )

def apollony2(c1, c2, c3, cother, exterior, n):
    "Helper function for 'fractal2'"
    circle = soddyCircle3(c1, c2, c3, cother[1]) if exterior else soddyCircle1(c1, c2, c3)
    if n == 1:
        return [circle]
    else:
        return (
            apollony2(c1, c2, circle, None, False, n-1)
            + apollony2(c1, circle, c3, cother, exterior, n-1)
            + apollony2(circle, c2, c3, cother, exterior, n-1)
        )

def fractal2(n, phi, beta):
    "List of circles of the modified Apollonian gasket"
    c4 = ((0.0, 0.0), 1.0)
    c1, c2, c3 = threeCircles(phi, c4, beta)
    l1 = [apollony2(c1, c2, c3, None, False, i) for i in range(1, n+1)]
    l2 = [apollony2(c1, c2, c4, c3, True, i) for i in range(1, n+1)]
    l3 = [apollony2(c1, c3, c4, c2, True, i) for i in range(1, n+1)]
    l4 = [apollony2(c2, c3, c4, c1, True, i) for i in range(1, n+1)]
    return (
        list(chain(*l1)) + list(chain(*l2)) 
        + list(chain(*l3)) + list(chain(*l4))
    )


def apollony3(c1, c2, c3, n):
    "Helper function for 'fractal3'"
    circle = soddyCircle2(c1, c2, c3)
    if n == 1:
        return [circle]
    else:
        return (
            apollony3(c1, c2, circle, n-1)
            + apollony3(c1, circle, c3, n-1)
            + apollony3(circle, c2, c3, n-1)
        )

def fractal3(n):
    c1 = ((1, -1/sqrt(3)), 1)
    c2 = ((-1, -1/sqrt(3)), 1)
    c3 = ((0, sqrt(3) - 1/sqrt(3)), 1)
    l = [apollony1(c1, c2, c3, False, i) for i in range(1, n+1)]
    return list(chain(*l))