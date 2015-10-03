import functools
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from collections import defaultdict
from numpy import random


__author__ = 'Marek'


def preMain() -> None:
    # user provide a number of clusters
    try:
        iClusters = int(input("How many clusters?"))
        if iClusters < 1:
            raise ValueError
        main(iClusters)
    except ValueError:
        print("Please provide positive integer.")
        quit()


def main(iClusters) -> None:

    # open file with points
    f = open('a2.txt', 'r')
    vPoints = []

    # create a list with read points
    for sLine in f.readlines():
        vPoints.append((int(sLine.split()[0]), int(sLine.split()[1])))

    # count for minimum and maximum values of list
    (iMinX, iMinY, iMaxX, iMaxY) = (
            min(vPoints, key=lambda x: x[0])[0],
            min(vPoints, key=lambda x: x[1])[1],
            max(vPoints, key=lambda x: x[0])[0],
            max(vPoints, key=lambda x: x[1])[1])
    # print(iMinX, iMinY, iMaxX, iMaxY)

    # generate random position of clusters
    vClusters = [(random.randint(iMinX, iMaxX), random.randint(iMinY, iMaxY))
                 for _ in range(iClusters)]
    # make old position of clusters very far away
    vOldClusters = [(float("inf"), float("inf"))] * iClusters

    # cluster belongings
    dClusterPoints = defaultdict(list)

    def new_cluster() -> None:
        dClusterPoints.clear()
        for point in vPoints:
            vDist = []
            for cluster in vClusters:
                x, y = point[0] - cluster[0], point[1] - cluster[1]
                dist = np.sqrt(x**2 + y**2)
                vDist.append(dist)

            # cluster to which point belongs, based on minimum distance
            iBelong = vDist.index(min(vDist))

            # add this point to a list of points of any cluster
            assert isinstance(point, tuple)
            dClusterPoints[iBelong].append(point)

        for i in range(iClusters):
            dCP = dClusterPoints
            try:
                vClusters[i] = (functools.reduce(lambda z, v: z + v, [d[0] for d in dCP[i]]) / len(dCP[i]),
                                functools.reduce(lambda z, v: z + v, [d[1] for d in dCP[i]]) / len(dCP[i]))
            except TypeError:
                print("There were probably two clusters at the same position. Restarting now...")
                main(iClusters)

    iDiffX = iMaxX - iMinX
    iDiifY = iMaxY - iMinY
    fQuantisationError = np.sqrt(iDiffX**2 + iDiifY**2) * 0.000000001

    while True:
        vbBreak = []
        for i in range(iClusters):
            x, y = vOldClusters[i][0] - vClusters[i][0], vOldClusters[i][1] - vClusters[i][1]
            fDiff = np.sqrt(x**2 + y**2)
            print(fDiff)
            if fDiff > fQuantisationError:
                vbBreak.append(False)
                break
            else:
                vbBreak.append(True)
        if all(vbBreak):
            break
        vOldClusters = np.copy(vClusters)
        new_cluster()

    # drawing a scatter with points
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = cm.rainbow(np.linspace(0, 1, iClusters))
    for i, color in zip(range(iClusters), colors):
        ax.scatter(*zip(*dClusterPoints[i]), marker='x', color=color)
    for cluster, color in zip(vClusters, colors):
        ax.scatter(*cluster, marker='o', color='black', s=150)
        ax.scatter(*cluster, marker='o', color=color, s=100)
    plt.show()
    quit()


if __name__ == "__main__":
    preMain()
