import functools
from matplotlib.pyplot import scatter
from numpy import random
from numpy import sqrt
from pylab import show

rand = random

f = open('199607daily.txt')

maxT = []
wind = []
sea = []
minT = []
for i in f.readlines()[1:]:
    try:
        maxT.append(float(i.split(',')[2]))
    except ValueError:
        pass
    try:
        wind.append(float(i.split(',')[-7]))
    except ValueError:
        pass
    try:
        sea.append(float(i.split(',')[-8]))
    except ValueError:
        pass
    try:
        minT.append(float(i.split(',')[3]))
    except ValueError:
        pass

avg_maxT = functools.reduce(lambda x, y: x + y, maxT) / len(maxT)
max_wind = max(wind)
min_wind = min(wind)

sea_max = sorted(sea)[:5]
sea_min = sorted(sea)[-5:]

enum = range(len(minT))

c1 = (rand.random_integers(0, 14000), rand.random_integers(0, 100))
c2 = (rand.random_integers(0, 14000), rand.random_integers(0, 100))
c3 = (rand.random_integers(0, 14000), rand.random_integers(0, 100))

c1p = []
c2p = []
c3p = []

for point in enum:
    dist = []
    x1 = point - c1[0]
    y1 = minT[point] - c1[1]
    dist1 = sqrt(x1**2 + y1**2)
    x2 = point - c2[0]
    y2 = minT[point] - c2[1]
    dist2 = sqrt(x2**2 + y2**2)
    x3 = point - c3[0]
    y3 = minT[point] - c3[1]
    dist3 = sqrt(x3**2 + y3**2)
    c1p.append((point, minT[point])) if dist1 < dist2 and dist1 < dist3 else c2p.append((point, minT[point])) if dist2 < dist3 else c3p.append((point, minT[point]))

scatter(*zip(*c1p), marker='x', c='red')
scatter(*zip(*c2p), marker='x', c='blue')
scatter(*zip(*c3p), marker='x', c='green')
scatter(*c1, marker='o', c='red', s=100)
scatter(*c2, marker='o', c='blue', s=100)
scatter(*c3, marker='o', c='green', s=100)
show()