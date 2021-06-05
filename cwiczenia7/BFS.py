from queue import Queue

class Node:
    def __init__(self):
        self.d = -1
        self.parent = None
        self.nbs = []

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
    
    print(visited)
    print(d)
    print(parent)


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
    
    print(visited)
    print(d)
    print(parent)

def bipartite_graph(G,s):
    Q = Queue()
    visited = [False for _ in range(len(G))]
    d = [-1 for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    colors = [0 for _ in range(len(G))]

    d[s] = 0
    visited[s] = True
    colors[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                d[v] = d[u]+1
                parent[v] = u
                colors[v] = colors[u] * -1
                Q.put(v)
        
            else:
                if colors[v] == colors[u]:
                    return False
    
    return True
    
    print(visited)
    print(d)
    print(parent)
    print(colors)



# G = [
#     [0,1,1,0,0,0,0,0],
#     [1,0,0,0,1,0,0,0],
#     [1,0,0,1,0,1,0,0],
#     [0,0,1,0,1,0,0,0],
#     [0,1,0,1,0,1,0,0],
#     [0,0,1,0,1,0,1,0],
#     [0,0,0,0,0,1,0,1],
#     [0,0,0,0,0,0,1,0]
# ]

# G = [
#     [1, 2],
#     [0, 4],
#     [0, 3, 5],
#     [2, 4],
#     [1, 3, 5],
#     [2, 4, 6],
#     [5, 7],
#     [6]
# ]
G = [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]

print(bipartite_graph(G, 0))
