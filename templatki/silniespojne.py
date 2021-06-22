def DFS(G):
    def obroc_krawedzie(G):
        for u in range(len(G)):
            for v in range(u+1,len(G)):
                G[u][v], G[v][u] = G[v][u], G[u][v]

    def DFSVisit(G,u,res):
        visited[u] = True
        
        for v in range(len(G)):
            if visited[v] == False and G[u][v] == 1:
                parent[v] = u
                DFSVisit(G,v,res)
        
        res.append(u)
    

    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    kolejnosc = []

    for u in range(len(G)):
        if visited[u] == False:
            DFSVisit(G,u,kolejnosc)
            
    kolejnosc.reverse()
    obroc_krawedzie(G)
    result = [[] for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    for i in kolejnosc:
        if visited[i] == False:
            DFSVisit(G,i,result[i])
    
    print(result)


if __name__ == "__main__":

    graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
            ]

    print(DFS(graph))