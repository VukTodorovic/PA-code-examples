from tree import *

L = [15, 11, 26, 8, 12, 20, 30, 6, 9, 14, 35]
nodeList = []

for l in L:
    nodeList.append(Node(key=l))

T = Tree()

for node in nodeList:
    treeInsert(T, node)

print("----Inorder tree walk----")
inorderTreeWalk(T.root)

print("----Tree min----")
min = treeMin(T.root)
print(min)

print("----Tree max----")
max = treeMax(T.root)
print(max)

print("----Tree succ----")
succ = treeSucc(nodeList[5]) # 20
print(succ)

print("----Tree search 20----")
search_res1 = treeSearch(T.root, 20)
print(search_res1)

print("----Tree search iterative 20----")
search_res2 = treeSearchIterative(T.root, 20)
print(search_res2)

print("----Tree delete root----")
print("Old root:", T.root)
treeDelete(T, T.root)
print("New root:", T.root)