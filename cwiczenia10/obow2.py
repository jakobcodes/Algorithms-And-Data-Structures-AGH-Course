# macierzowo
def DFS(G):
    def DFSVisit(G,u,s):
        visited[u] = True

        for v in range(len(G)):
            if G[u][v] == 1 and visited[v] == False:
                H[s][v] = 1
                DFSVisit(G,v,s)


    H = [[0 for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(H)):
        for j in range(len(H)):
            if i == j:
                H[i][j] = 1

    for u in range(len(G)):
        visited = [False for _ in range(len(G))]
        DFSVisit(G,u,u)
    
    for i in H:
        print(i)

G = [   [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 0, 0, 0]
         ]

DFS(G)