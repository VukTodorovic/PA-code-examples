
class Vertex:
    def __init__(self, c=None, p=None, d=None, f=None, name=None):
        self.c = c
        self.p = p
        self.d = d
        self.f = f
        self.name = name

    def __str__(self):
        return str(self.name) 

class VertexColor:
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Graph:
    def __init__(self, V=None, E=None):
        self.V = V
        self.E = E