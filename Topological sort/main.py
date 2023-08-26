from vertex_example import *
from bfs import *
from dfs import *

vA = Vertex(name='A')
vB = Vertex(name='B')
vC = Vertex(name='C')
vD = Vertex(name='D')
vE = Vertex(name='E')

V = []
V.append(vA)
V.append(vB)
V.append(vC)
V.append(vD)
V.append(vE)

E = []
E.append([vB])
E.append([vC, vE])
E.append([vE])
E.append([vA, vE])
E.append([])

G = Graph(V=V, E=E)


topological_L = DFS_topological(G)

print("----------------- Topological sort -----------------")
for vertex in topological_L:
    print(vertex)


