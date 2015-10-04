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
old_c1 = (-1000, -1000)
old_c2 = (-1000, -1000)
old_c3 = (-1000, -1000)

c1p = []
c1x = []
c1y = []

c2p = []
c2x = []
c2y = []

c3p = []
c3x = []
c3y = []


def new_cluster():
    global c1
    global c2
    global c3

    c1p.clear()
    c1x.clear()
    c1y.clear()
    c2p.clear()
    c2x.clear()
    c2y.clear()
    c3p.clear()
    c3x.clear()
    c3y.clear()
    for point in enum:
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
        c1x.append(point) if dist1 < dist2 and dist1 < dist3 else c2x.append(point) if dist2 < dist3 else c3x.append(point)
        c1y.append(minT[point]) if dist1 < dist2 and dist1 < dist3 else c2y.append(minT[point]) if dist2 < dist3 else c3y.append(minT[point])

    # c1 = (functools.reduce(lambda x, y: x + y, c1x) / len(c1x), functools.reduce(lambda x, y: x + y, c1y) / len(c1y))
    c1 = sum(c1x)/len(c1x), sum(c1y)/len(c1y)
    c2 = (functools.reduce(lambda x, y: x + y, c2x) / len(c2x), functools.reduce(lambda x, y: x + y, c2y) / len(c2y))
    c3 = (functools.reduce(lambda x, y: x + y, c3x) / len(c3x), functools.reduce(lambda x, y: x + y, c3y) / len(c3y))

quantisation_error = max(minT) * 0.01

while not (abs(old_c1[0] - c1[0]) < quantisation_error * 140
           and abs(old_c1[1] - c1[1]) < quantisation_error
           and abs(old_c2[0] - c2[0]) < quantisation_error * 140
           and abs(old_c2[1] - c2[1]) < quantisation_error
           and abs(old_c3[0] - c3[0]) < quantisation_error * 140
           and abs(old_c3[1] - c3[1]) < quantisation_error):
    old_c1 = c1
    old_c2 = c2
    old_c3 = c3
    new_cluster()

scatter(*zip(*c1p), marker='x', c='red')
scatter(*zip(*c2p), marker='x', c='blue')
scatter(*zip(*c3p), marker='x', c='green')
scatter(*c1, marker='o', c='red', s=100)
scatter(*c2, marker='o', c='blue', s=100)
scatter(*c3, marker='o', c='green', s=100)
show()
