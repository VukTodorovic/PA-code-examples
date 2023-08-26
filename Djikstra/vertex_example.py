
class Vertex:
    def __init__(self, c=None, p=None, d=None, f=None, name=None):
        self.c = c
        self.p = p
        self.d = d
        self.f = f
        self.name = name

    def __str__(self):
        parent_name = str(self.p.name) if self.p is not None else "None"
        return str(self.name) + ": P = " + parent_name + ", d = " + str(self.d)
    
    # def __repr__(self):
    #     return str(self.name)

class Edge:
    def __init__(self, src=None, dst=None, w=None):
        self.src = src
        self.dst = dst
        self.w = w

class VertexColor:
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Graph:
    def __init__(self, V=None, E=None):
        self.V = V
        self.E = E

    def get_adj(self, v):
        ret = []
        for e in self.E:
            if v is e.src:
                ret.append(e.dst)
        return ret
    
    def get_weight(self, s, d):
        for e in self.E:
            if e.src is s and e.dst is d:
                return e.w