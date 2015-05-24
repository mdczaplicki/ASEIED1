from matplotlib.pyplot import scatter

__author__ = 'Marek'

from numpy import random
from numpy import sqrt
import matplotlib as plt
from pylab import plot, show

rand = random

p = [(rand.random_integers(0, 100), rand.random_integers(0, 100)) for x in range(30)]
print(p)
c1 = (rand.random_integers(0, 100), rand.random_integers(0, 100))
c2 = (rand.random_integers(0, 100), rand.random_integers(0, 100))

c1p = []
c2p = []

for point in p:
    x1 = point[0] - c1[0]
    y1 = point[1] - c1[1]
    dist1 = sqrt(x1**2 + y1**2)
    x2 = point[0] - c2[0]
    y2 = point[1] - c2[1]
    dist2 = sqrt(x2**2 + y2**2)
    c1p.append(point) if dist1 < dist2 else c2p.append(point)


scatter(*c1, marker='o', c='red', s=100)
scatter(*zip(*c1p), marker='x', c='red', s=70)
scatter(*c2, marker='o', c='blue', s=100)
scatter(*zip(*c2p), marker='x', c='blue', s=70)
show()