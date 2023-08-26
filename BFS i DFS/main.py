from vertex_example import *
from bfs import *
from dfs import *

v1 = Vertex(name=1)
v2 = Vertex(name=2)
v3 = Vertex(name=3)
v4 = Vertex(name=4)
v5 = Vertex(name=5)

E = []
E.append([v2, v4])
E.append([v1, v3])
E.append([v2, v4, v5])
E.append([v1, v3, v5])
E.append([v3, v4])

V = []
V.append(v1)
V.append(v2)
V.append(v3)
V.append(v4)
V.append(v5)

G = Graph(V=V, E=E)

BFS(G, v1)

print("----------------- BFS -----------------")
print("----v1 -> v1----")
printPath(G, v1, v1)
print("----v1 -> v2----")
printPath(G, v1, v2)
print("----v1 -> v3----")
printPath(G, v1, v3)
print("----v1 -> v4----")
printPath(G, v1, v4)

DFS(G)

print("----------------- DFS -----------------")
print("----v1 -> v1----")
printPath(G, v1, v1)
print("----v1 -> v2----")
printPath(G, v1, v2)
print("----v1 -> v3----")
printPath(G, v1, v3)
print("----v1 -> v4----")
printPath(G, v1, v4)


