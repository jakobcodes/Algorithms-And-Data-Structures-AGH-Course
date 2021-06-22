from math import inf

# obliczanie najkrotszych sciezek w sytuacji gdy wagi mogą być ujemne

def bellman_ford(G,s):
    def relax(u,v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    d = [inf for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    d[s] = 0 

    for i in range(len(G)):
        for u in range(len(G)):
            for v in range(len(G)):
                if G[u][v] != -1:
                    relax(u,v)

    for u in range(len(G)):
        for v in range(len(G)):
            if d[v] <= d[u] + G[u][v]:
                continue

            print("mamy ujemny cykl")
    

