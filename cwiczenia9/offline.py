from queue import PriorityQueue
from math import inf

def dijkstry(G,s):
    def relax(u,v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u
       
    Q = PriorityQueue()
    d = [inf for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    Q.put((0,s))
    d[s] = 0
    
    while not Q.empty():
        u = Q.get()[1]
        for i in range(len(G)):
            if G[u][i] != -1:
                relax(u,i)
                if visited[i] == False:
                    Q.put((d[i],i))
                    visited[u] = True
                    
    
    return d,parent

def min_cycle(G):
    best = inf
    for u in range(len(G)):
        for v in range(u+1,len(G)):
            if G[u][v] != -1:
                tmp = G[u][v]
                G[u][v] = -1
                G[v][u] = -1
                d,parent = dijkstry(G,u)
                if d[v] != inf:
                    if d[v] + tmp < best:
                        best = d[v] + tmp
                        path = parent
                        x = v
                
                G[u][v] = tmp
                G[v][u] = tmp

    if best == inf:
        return []

    res = []
    while x != -1:
        res.append(x)
        x = path[x]

    return res

W = [
    [-1,1,-1,-1,5],
    [1,-1,7,8,2],
    [-1,7,-1,1,-1],
    [-1,8,1,-1,3],
    [5,2,-1,3,-1]]
print(min_cycle(W))
G = [[-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]
print(min_cycle(G))
G1 =[[-1,1,-1,-1,-1,-1,1],
    [1,-1,2,1,-1,-1,-1],
    [-1,2,-1,2,-1,-1,-1],
    [-1,1,2,-1,-1,-1,-1],
    [-1,-1,-1,1,-1,1,-1],
    [-1,-1,-1,-1,1,-1,1],
    [1,-1,-1,-1,-1,1,-1]]
print(min_cycle(G1))
graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
        [4, -1, 8, -1, -1, -1, -1, 11, -1],
        [-1, 8, -1, 7, -1, 4, -1, -1, 2],
        [-1, -1, 7, -1, 9, 14, -1, -1, -1],
        [-1, -1, -1, 9, -1, 10, -1, -1, -1],
        [-1, -1, 4, 14, 10, -1, 2, -1, -1],
        [-1, -1, -1, -1, -1, 2, -1, 1, 6],
        [8, 11, -1, -1, -1, -1, 1, -1, 7],
        [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
print(min_cycle(graph))
K = [[-1, 1, -1, -1, -1, -1, 1],
     [1, -1, 2, 1, -1, -1, -1],
     [-1, 2, -1, 2, -1, -1, -1],
     [-1, 1, 2, -1, 1, -1, -1],
     [-1, -1, -1, 1, -1, 1, -1],
     [-1, -1, -1, -1, 1, -1, 1],
     [1, -1, -1, -1, -1, 1, -1]]
print(min_cycle(K))
G = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]
print(min_cycle(G))