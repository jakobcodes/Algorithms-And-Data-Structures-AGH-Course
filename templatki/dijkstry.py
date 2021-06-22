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