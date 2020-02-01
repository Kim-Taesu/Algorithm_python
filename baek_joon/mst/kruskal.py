from baek_joon.mst.config import *
from baek_joon.mst.disfoint_set import *


def kruskal(V, data_list):
    weight = 0
    disjoint = DisjointSet(V)
    result = []
    for data in sorted(data_list, key=lambda cost: cost[2]):
        v, u, w = data
        root1 = disjoint.find(v)
        root2 = disjoint.find(u)

        if root1 != root2:
            disjoint.union(root1, root2)
            result.append(data)
            weight += w
    return result, weight


print(kruskal(V, DATA_LIST))
