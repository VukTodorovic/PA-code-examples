from vertex_example import *
from math import inf

def Djikstra(G, s):
    init_single_source(G, s)
    S = []
    Q = G.V[:]
    while len(Q) > 0:
        u = extract_min(Q)
        S.append(u)
        for v in G.get_adj(u):
            relax(u, v, G.get_weight(u, v))


def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.d < min.d:
            min = v
    Q.remove(min)
    return min

def init_single_source(G, s):
    for v in G.V:
        v.d = inf
        v.p = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u

print(inf)