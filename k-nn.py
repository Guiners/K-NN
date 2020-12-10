import numpy as np
import random
import math as math
import statistics as stat
data = np.loadtxt(fname='F:\Code\k-nn\ABiris.data', dtype = 'str', delimiter = ",")
point1 = data[0]
print("aaa" , point1)
data_del = np.delete(data, 0, 0)
data_shape = data_del.shape

def counting_distance(point, data_shape, data):
    distances = []
    count = []
    for i in range(data_shape[0]):
        for j in range(data_shape[1]-1):
            count.append((float(point[j]) - float(data[i][j]))**2)
        distances.append([math.sqrt(sum(count)), data[i][(data_shape[1]-1)]])
        count = []
    return distances

all_distances = counting_distance(point1, data_shape, data_del)
def choosing_class(distances):
    common = []
    for i in range(7):
        common.append(distances[i][1])
    return stat.mode(common)

point_class = choosing_class(all_distances)

print("point class is", point_class)
