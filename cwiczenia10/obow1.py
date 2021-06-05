from queue import PriorityQueue
from math import inf

def dijkstry(G,s,t):

    Q = PriorityQueue()
    Q.put((0,s,[s]))
    
    while not Q.empty():
        tmp = Q.get()
        d = tmp[0]
        u = tmp[1]
        path = tmp[2]
        if len(path) > 1:
            last = path[-2]
            if path[-1] == t:
                return path,d
        

        for v in range(len(G)):
            if len(path) == 1 and G[u][v] > 0:
                # relax(u,v)
                Q.put((d + G[u][v],v,path + [v]))
            
            elif G[u][v] > 0 and G[last][u] > G[u][v]:
                # relax(u,v)
                Q.put((d + G[u][v],v,path + [v]))
    
    return None
    

G2 =[[0,1,5,0,0,0],
    [1,0,5,7,8,0],
    [5,5,0,0,3,2],
    [0,7,0,0,1,0],
    [0,8,3,1,0,0],
    [0,0,2,0,0,0]]

print(dijkstry(G2,4,5))