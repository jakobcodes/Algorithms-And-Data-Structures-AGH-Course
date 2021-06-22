from math import inf

def warshall(W):
    
    S = [[0 for _ in range(len(W))] for _ in range(len(W))]
    for i in range(len(S)):
        for j in range(len(S)):
            if W[i][j] == 0:
                S[i][j] = inf
            else:
                S[i][j] = W[i][j]

    for t in range(len(W)):
        for u in range(len(W)):
            for w in range(len(W)):
                if u != w:
                    S[u][w] = min(S[u][w] , S[u][t] + S[t][w])
    
    for i in S:
        print(i)

W=[[0,4,0,0,0,3],
   [4,0,2,0,0,4],
   [0,2,0,4,0,2],
   [0,0,4,0,5,0],
   [0,0,0,5,0,7],
   [3,4,2,0,7,0]]

warshall(W)