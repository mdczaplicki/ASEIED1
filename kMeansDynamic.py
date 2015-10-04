import functools
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from collections import defaultdict
from numpy import random
from mpl_toolkits.mplot3d import Axes3D


__author__ = 'Marek'


def preMain() -> None:
    # user provide a number of clusters
    try:
        iClusters = int(input("How many clusters?"))
        if iClusters < 1:
            raise ValueError
    except ValueError:
        print("Please provide positive integer.")
        quit()
    main(iClusters)


def main(iClusters) -> None:
    # open file with points
    f = open('yeast.txt', 'r')
    vPoints = []
    iDimensions = 0
    bTemp = True

    # create a list with read points
    for sLine in f.readlines():
        vLineSplit = sLine.split()
        if bTemp:
            iDimensions = len(vLineSplit)
            bTemp = False
        vPoints.append(tuple(float(x) for x in vLineSplit))


    # count for minimum and maximum values of list
    vClusters = [tuple(random.uniform() for _ in range(iDimensions)) for _ in range(iClusters)]
    # make old position of clusters very far away
    vOldClusters = [tuple([float("inf")] * iDimensions)] * iClusters

    # cluster belongings
    dClusterPoints = defaultdict(list)

    def new_cluster() -> None:
        """
        :rtype : None
        """
        dClusterPoints.clear()
        for point in vPoints:
            vDist = []

            for c in vClusters:
                vDimDist = []
                for dim in range(iDimensions):
                    vDimDist.append(point[dim] - c[dim])
                vDimDist = [x**2 for x in vDimDist]
                dist = np.sqrt(sum(vDimDist))
                vDist.append(dist)

            # cluster to which point belongs, based on minimum distance
            iBelong = vDist.index(min(vDist))

            # add this point to a list of points of any cluster
            assert isinstance(point, tuple)
            dClusterPoints[iBelong].append(point)

        for n in range(iClusters):
            dCP = dClusterPoints
            # try:
            #     vClusters[n] = tuple([sum([d[dim] for d in dCP[n]])/len(dCP[n]) for dim in range(iDimensions)])
            # except ZeroDivisionError:10
            #     # if there is no points
            #     vClusters[n] = tuple([sum([d[dim] for d in vPoints])/len(vPoints) for dim in range(iDimensions)])
            try:
                vClusters[n] = tuple([functools.reduce(lambda b, m: b + m, [d[dim] for d in dCP[n]]) / len(dCP[n]) for dim in range(iDimensions)])
            except TypeError:
                vClusters[n] = tuple([functools.reduce(lambda b, m: b + m, [d[dim] for d in vPoints]) / len(vPoints) for dim in range(iDimensions)])

    fQuantisationError = 0.001

    while True:
        vbBreak = []
        for i in range(iClusters):
            vDimDist = []
            for dim in range(iDimensions):
                vDimDist.append(vOldClusters[i][dim] - vClusters[i][dim])
            vDimDist = [x**2 for x in vDimDist]
            fDiff = np.sqrt(sum(vDimDist))
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
    if iDimensions ==2:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        colors = cm.rainbow(np.linspace(0, 1, iClusters))
        for i, color in zip(range(iClusters), colors):
            ax.scatter(*zip(*dClusterPoints[i]), marker='x', color=color)
        for cluster, color in zip(vClusters, colors):
            ax.scatter(*cluster, marker='o', color='black', s=150)
            ax.scatter(*cluster, marker='o', color=color, s=100)

    elif iDimensions == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        colors = cm.rainbow(np.linspace(0, 1, iClusters))
        for i, color in zip(range(iClusters), colors):
            ax.scatter(*zip(*dClusterPoints[i]), marker='x', color=color)
        for cluster, color in zip(vClusters, colors):
            ax.scatter(*cluster, marker='o', color='black', s=150)
            ax.scatter(*cluster, marker='o', color=color, s=100)

    elif iDimensions > 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        colors = cm.rainbow(np.linspace(0, 1, iClusters))
        for i, color in zip(range(iClusters), colors):
            dCP = dClusterPoints[i]
            dCP = [x[:3] for x in dCP]
            ax.scatter(*zip(*dCP), marker='x', color=color)
        for cluster, color in zip(vClusters, colors):
            cluster = cluster[:3]
            ax.scatter(*cluster, marker='o', color='black', s=150)
            ax.scatter(*cluster, marker='o', color=color, s=100)
    plt.show()
    quit()


if __name__ == "__main__":
    preMain()
