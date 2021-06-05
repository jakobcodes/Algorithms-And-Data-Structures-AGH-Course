from queue import PriorityQueue
from math import inf

def dijkstry(G,s,t):
    def relax(u,v,poj):
        if c[v] < min(c[u],poj):
            c[v] = min(c[u],poj)
            parent[v] = u

    Q = PriorityQueue()
    c = [-1 for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    Q.put((-inf,s))
    c[s] = inf
    
    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True
        for i in G[u]:
            relax(u,i[0],i[1])
            if visited[i[0]] == False:
                Q.put((-c[i[0]],i[0]))
                # visited[u] = True
    
    print(c)
    if c[t] != -1:
        result = []
        while t != -1:
            result.append(t)
            t = parent[t]
        result.reverse()
        return result

    else: return []

G = [[(1,4), (2,3)], # 0
    [(3,2)], # 1
    [(3,5)], # 2
    []]

G2 = [
    [(1,1),(2,10)],
    [(6,1)],
    [(1,5),(3,4),(5,4)],
    [(4,4)],
    [(5,4)],
    [(3,4),(6,3)],
    []
]

print(dijkstry(G2,0,6))