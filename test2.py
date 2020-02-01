from baek_joon.mst.config import *
from baek_joon.mst.disfoint_set import *

def kruskal(V, data):
    weight = 0
    disjoint = DisjointSet(V)
    result = []

    for d in sorted(data, key=lambda key: key[2]):
        v, u, w = d
        if not disjoint.find_parent(v, u):
            weight += w
            disjoint.union(v, u)
            result.append(d)

    return result, weight


print(kruskal(V, DATA_LIST))
