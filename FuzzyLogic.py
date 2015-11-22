import skfuzzy as fuzz
import numpy as  np
__author__ = 'Marek'

test_data = np.array([(-1, -1), (3, 3)])
print(test_data)

cntr_trained = np.array([(-2, -2), (2, 2), (5, 5)])


u, u0, d, jm, p, fpc = fuzz.cluster.cmeans_predict(
    test_data, cntr_trained, 0., 0.0001, 10
)

print(u)