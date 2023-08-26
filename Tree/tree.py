class Node:
    def __init__(self, key, l=None, r=None, p=None):
        self.key = key
        self.l = l
        self.r = r
        self.p = p
    def __str__(self):
        return "{" + str(self.key) + "}"


class Tree:
    def __init__(self, root=None):
        self.root = root


def treeInsert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.l
        else:
            x = x.r
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.l = z
    else:
        y.r = z

def inorderTreeWalk(x):
    if x is not None:
        inorderTreeWalk(x.l)
        print(x.key)
        inorderTreeWalk(x.r)

def treeMin(x):
    while x.l is not None:
        x = x.l
    return x

def treeMax(x):
    while x.r is not None:
        x = x.r
    return x

def treeSucc(x):
    if x.r is not None:
        return treeMin(x.r)
    y = x.p
    while y is not None and x is y.r:
        x = y
        y = y.p
    return y

def treeSearch(x, k):
    if x is None or k is x.key:
        return x
    if k < x.key:
        return treeSearch(x.l, k)
    else:
        return treeSearch(x.r, k)
    
def treeSearchIterative(x, k):
    while x is not None and k is not x.key:
        if k < x.key:
            x = x.l
        else:
            x = x.r
    return x

def treeTransplant(T, u, v):
    if u.p is None:
        T.root = v
    elif u is u.p.l:
        u.p.l = v
    else:
        u.p.r = v
    if v is not None:
        v.p = u.p

def treeDelete(T, z):
    if z.l is None:
        treeTransplant(T, z, z.r)
    elif z.r is None:
        treeTransplant(T, z, z.l)
    else:
        y = treeMin(z.r)
        if y.p is not z:
            treeTransplant(T, y, y.r)
            y.r = z.r
            y.r.p = y
            treeTransplant(T, z, y)
            y.l = z.l
            y.l.p = y