from vertex_example import *

time = 0
L = []

def DFS_topological(G):
    for u in G.V:
        u.c = VertexColor.WHITE
        u.p = None
    global time
    time = 0
    global L
    L = []
    for u in G.V:
        if u.c is VertexColor.WHITE:
            DFS_visit_topological(G, u)
    return L

def DFS_visit_topological(G, u):
    global time
    time = time + 1
    u.d = time
    u.c = VertexColor.GRAY
    for v in G.E[G.V.index(u)]:
        if v.c is VertexColor.WHITE:
            v.p = u
            DFS_visit_topological(G, v)
    u.c = VertexColor.BLACK
    time = time + 1
    u.f = time
    global L
    L = [u] + L