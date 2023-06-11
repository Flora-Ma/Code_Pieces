import numpy as np
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.size = {}

    def add(self, x):
        if x in self.parents:
            return
        self.parents[x] = x
        self.size[x] = 1
    
    def find(self, x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        # Path compression
        while self.parents[x] != root:
            self.parents[x], x = root, self.parents[x]
        return root
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.parents[px] = py
            self.size[py] += self.size[px]
    
uf = UnionFind()
for i in range(10):
    uf.add(i)

uf.union(2, 4)
uf.union(4, 6)
uf.union(6, 8)

print(uf.size)


