import numpy as np
import configparser
from sklearn import datasets, svm


def readFromIni() -> list:
    config = configparser.RawConfigParser()
    config.read('file.ini')
    iClusters = config.getint('cluster_points', 'clusters_number')

    vPoints = [[] for _ in range(iClusters)]
    for i in range(iClusters):
        temp = config.get('cluster_points', str(i))
        assert isinstance(temp, str)
        temp = temp.replace('(', '').replace(')', '').split('#')
        temp = [x.split(',') for x in temp]
        vPoints[i] = [(float(x[0]), float(x[1])) for x in temp]

    return vPoints


def learnNeuralNetwork(vLearning) -> svm.SVC:
    clf = svm.SVC(kernel='linear')
    X = []
    y = []
    for iCluster in range(len(vLearning)):
        for point in vLearning[iCluster]:
            X.append(point)
            y.append(iCluster)

    clf.fit(X, y)
    return clf


def askNeuralNetwork(clf, vAsking):
    for point in vAsking:
        print(clf.predict(point))


if __name__ == "__main__":
    vPoints = readFromIni()
    vLearning, vAsking = [], []
    for vClusterPoints in vPoints:
        vLearning.append(vClusterPoints[:-5])
        vAsking.append(vClusterPoints[-5:])

    clf = learnNeuralNetwork(vLearning)
    askNeuralNetwork(clf, vAsking)
