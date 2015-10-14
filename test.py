import numpy as np
import configparser
from sklearn import datasets, svm


def neuro() -> None:
    config = configparser.RawConfigParser()
    config.read('file.ini')
    iClusters = config.getint('cluster_points', 'clusters_number')

    for i in range(iClusters):
        vPoints = config.get('cluster_points', str(i))
        assert isinstance(vPoints, str)
        vPoints = vPoints.replace('(', '').replace(')', '').split('#')
        vPoints = [x.split(',') for x in vPoints]
        vPoints = [(float(x[0]), float(x[1])) for x in vPoints][:2]


def new() -> None:
    iris = datasets.load_iris()
    X = [
        [0, 0],
        [10, 10],
        [100, 100],
    ]
    y = [0, 1, 3]
    clf = svm.SVC()
    clf.fit(X, y)

    print(clf.predict([500, 4.9999999999999999]))

if __name__ == "__main__":
    new()
