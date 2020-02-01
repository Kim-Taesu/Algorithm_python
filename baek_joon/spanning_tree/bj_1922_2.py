import heapq


class DisjointSet:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.length = V

    def get_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.get_parent(self.parent[node])
        return self.parent[node]

    def find_parent(self, node1, node2):
        node1, node2 = self.get_parent(node1), self.get_parent(node2)

        if node1 == node2:
            return True
        else:
            return False

    def union(self, node1, node2):
        node1, node2 = self.get_parent(node1), self.get_parent(node2)

        if node1 > node2:
            self.parent[node1] = node2

        else:
            self.parent[node2] = node1


def kruskal(V, E, data):
    weight = 0
    disjoint = DisjointSet(V)
    while data:
        w, v, u = heapq.heappop(data)
        root1 = disjoint.get_parent(v)
        root2 = disjoint.get_parent(u)

        if root1 != root2:
            disjoint.union(root1, root2)
            weight += w
    return weight


V = int(input().strip())
E = int(input().strip())
E_list = []
for _ in range(E):
    v, u, w = list(map(int, input().strip().split()))
    heapq.heappush(E_list, (w, v-1, u-1))

print(kruskal(V, E, E_list))
