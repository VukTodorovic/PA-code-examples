from vertex_example import *
from djikstra import *

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
E.append(Edge(src=vA, dst=vB, w=3))
E.append(Edge(src=vB, dst=vC, w=2))
E.append(Edge(src=vB, dst=vE, w=4))
E.append(Edge(src=vC, dst=vE, w=1))
E.append(Edge(src=vD, dst=vA, w=5))
E.append(Edge(src=vD, dst=vE, w=4))

G = Graph(V=V, E=E)


print("----------------- Djikstra -----------------")
print("-----Graph-----")
for vertex in G.V:
    print(vertex)

Djikstra(G, vA)

print("-----Graph-----")
for vertex in G.V:
    print(vertex)
