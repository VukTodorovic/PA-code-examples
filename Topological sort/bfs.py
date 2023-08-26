from queue import Queue
from math import inf
from vertex_example import *
 

def BFS(G, s):
    for u in G.V:
        u.c = VertexColor.WHITE
        u.d = inf
        u.p = None
    s.c = VertexColor.GRAY
    s.d = 0
    s.p = None
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G.E[G.V.index(u)]:
            if v.c is VertexColor.WHITE:
                v.c = VertexColor.GRAY
                v.d = u.d + 1
                v.p = u
                Q.put(v)
        u.c = VertexColor.BLACK

def printPath(G, s, v):
    if v is s:
        print(s)
    elif v.p is None:
        print(f"No path from {s} to {v} exists")
    else:
        printPath(G, s, v.p)
        print(v)