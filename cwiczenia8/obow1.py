
def DFS(G):
    def DFSdelete(G,u):
        visited[u] = True

        for v in range(len(G)):
            if G[v][u] == 1:
                if visited[v] == False:
                    parent[v] = u
                    DFSdelete(G, v)
        
        result.append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    result = []
    DFSdelete(G,0)
    return result

    

                

G2 = [
    [0,1,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,0],
    [0,0,1,0,1,1,1,1,0,1],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0],
    [0,0,0,1,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,0,1,0]
]

G1 = [
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,0],
    [0,0,1,1,0,1,0,0],
    [0,0,0,0,1,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,0]
]

print(DFS(G1),"G1")
print(DFS(G2),"G2")
