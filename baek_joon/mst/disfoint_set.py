class DisjointSet:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.length = V

    def get_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.get_parent(self.parent[node])
        return self.parent[node]

    def find_parent(self, node1, node2):
        node1_parent, node2_parent = self.get_parent(node1), self.get_parent(node2)
        if node1_parent == node2_parent:
            return True
        else:
            return False

    def union(self, node1, node2):
        node1, node2 = self.get_parent(node1), self.get_parent(node2)
        if node1 > node2:
            self.parent[node1] = node2
        else:
            self.parent[node2] = node1
