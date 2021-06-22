def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        time += 1
        d[u] = time
        low[u] = time
        visited[u] = True

        for v in range(len(G)):
            if G[u][v] == 1:
                if visited[v] == False:
                    parent[v] = u
                    DFSVisit(G,v)
                elif parent[u] != v:
                    low[u] = min(d[u], d[v], low[u])

        for v in range(len(G)):
            if G[u][v] == 1:
                if parent[u] != v:
                    low[u] = min(low[u],low[v])
        
        if low[u] == d[u]:
            if parent[u] != None:
                print((u,parent[u]))
        

    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    time = 0
    d = [0 for _ in range(len(G))]
    low = [0 for _ in range(len(G))]


    # printowanie mostów
    for u in range(len(G)):
        if visited[u] == False:
            DFSVisit(G,u)
    
    
    print(low)





