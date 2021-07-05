import queue
import sys


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjacencyMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        if not self.containsEdge(v1, v2):
            self.adjacencyMatrix[v1][v2] = 1
            self.adjacencyMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2):
            self.adjacencyMatrix[v1][v2] = 0
            self.adjacencyMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return self.adjacencyMatrix[v1][v2] != 0

    def DFS(self, v1=0, visited=dict()):
        print(v1, end=" ")
        visited[v1] = 1

        n = len(self.adjacencyMatrix)
        i = v1
        for j in range(n):
            x = self.adjacencyMatrix[i][j]
            if x == 1 and visited.get(j, 0) != 1:
                self.DFS(j, visited)
        return

    def BFS(self, v1=0):
        if len(self.adjacencyMatrix) == 0:
            return
        q = queue.Queue()
        unvisited = dict()
        z = len(self.adjacencyMatrix[0])
        for i in range(z):
            unvisited[i] = 1
        unvisited.pop(v1)
        q.put(v1)
        n = len(self.adjacencyMatrix)
        while not q.empty():
            v1 = q.get()
            print(v1, end=" ")
            for j in range(n):
                x = self.adjacencyMatrix[v1][j]
                if x == 1 and unvisited.get(j, 0) != 0:
                    q.put(j)
                    unvisited.pop(j)
            if q.empty():
                if len(unvisited) != 0:
                    for key in unvisited.keys():
                        q.put(key)
                        unvisited.pop(key)
                        break
        return

    def __str__(self):
        return str(self.adjacencyMatrix)


y = list(map(int, sys.stdin.readline().strip().split()))

v = y[0]
e = y[1]

g = Graph(v)

t = e

while t > 0:
    x = list(map(int, sys.stdin.readline().strip().split()))
    v1 = x[0]
    v2 = x[1]
    g.addEdge(v1, v2)
    t -= 1
g.BFS()
