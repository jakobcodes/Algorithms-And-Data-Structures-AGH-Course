from queue import Queue

def BFS_matrix(G,s):
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

def BFS_3(G,s):
    Q = Queue()
    visited = [False for _ in range(len(G))]
    d = [-1 for _ in range(len(G))]
    parent = [None for _ in range(len(G))]

    d[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                d[v] = d[u]+1
                parent[v] = u
                Q.put(v)