class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return

    if x.rank > y.rank:
        y.parent = x
    
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def make_list(W):
    e = []
    for i in range(len(W)):
        for j in range(i+1,len(W)):
            if (W[i][j] > 0):
                e.append((W[i][j],(i,j)))
    return e

def kruskal(W):
    def make_set():
        V = []
        for i in range(len(W)):
            V.append(Node(i))
        return V

    edges = make_list(W)
    edges.sort(key=lambda edges: edges[0])
    V = make_set()

    result = []
    for i in edges:
        u = V[i[1][0]]
        v = V[i[1][1]]
           
        if find(u) != find(v):
            union(u,v)
            result.append((u.val,v.val))
        
    return result



W  = [
    [0,7,0,0,0,1],
    [7,0,2,0,3,8],
    [0,2,0,5,0,0],
    [0,0,5,0,6,4],
    [0,3,0,6,0,12],
    [1,8,0,4,12,0]
]
print(kruskal(W))