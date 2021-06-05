from queue import Queue
def BFS_matrix(G,s):
    def printSolution(G,v,u,s):
        result = [u]
        result.append(v)
        result.append(parent[v])
        result.append(s)
        result.append(u)
        print(result)

    Q = Queue()
    visited = [False for _ in range(len(G))]
    d = [-1 for _ in range(len(G))]
    parent = [None for _ in range(len(G))]

    d[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(len(G[u])):
            if G[u][v] == 1:
                if visited[v] == False:
                    visited[v] = True
                    d[v] = d[u] + 1
                    parent[v] = u
                    Q.put(v)
                elif d[v] == 2 and d[u] == 1:
                    printSolution(G,v,u,s)
                    return True
    
    return False

def findCycle4(G):
    isComplete = True
    for i in range(len(G)):
        for j in range(len(G)):
            if i != j and G[i][j] == 0:
                isComplete = False

    if isComplete == False:
        for i in range(len(G)):
            if BFS_matrix(G, i):
                return
        print("brak cyklu dlugosci 4")

    else:
        if len(G) > 3:
            print([0,1,2,3,0])
        else:
            print("brak cyklu dlugosci 4")


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

# graf pelny bez jednej krawedzi
G3 = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [1,1,0,0,1],
    [1,1,1,1,0]
]

findCycle4(G3)