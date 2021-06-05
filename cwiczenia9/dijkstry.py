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
        visited[u] = True
        for i in range(len(G)):
            if G[u][i] > 0:
                relax(u,i)
                if visited[i] == False:
                    Q.put((d[i],i))
                    # visited[u] = True
          
    # u = 2
    # result = []
    # while u != -1:
    #     result.append(u)
    #     u = parent[u]
    
    print(d)
            

G = [
    [(1,1),(4,5)],
    [(0,1),(2,7),(3,8),(4,2)],
    [(1,7),(3,1)],
    [(1,8),(2,1),(4,3)],
    [(0,5),(1,2),(3,3)]
]

W = [
    [0,1,0,0,5],
    [1,0,7,8,2],
    [0,7,0,1,0],
    [0,8,1,0,3],
    [5,2,0,3,0]
]
dijkstry(W,0)
