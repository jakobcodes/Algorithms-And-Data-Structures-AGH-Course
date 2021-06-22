# macierzowo
def DFS(G):
    def DFSVisit(G,u):
        visited[u] = True

        for v in range(len(G)):
            if G[u][v] == 1 and visited[v] == False:
                parent[v] = u
                DFSVisit(G,v)

    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]

    for u in range(len(G)):
        if visited[u] == False:
            DFSVisit(G,u)

#lista sasiedztwa
def DFS(G):
    def DFSVisit(G,u):
        visited[u] = True

        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                DFSVisit(G,v)

    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]

    for u in range(len(G)):
        if visited[u] == False:
            DFSVisit(G,u)