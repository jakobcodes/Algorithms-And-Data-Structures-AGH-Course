def DFS(G):
    if checkIfPossible(G):
        used = []
        result = [0]
        occur = [False for _ in range(len(G))]
        result = DFSVisit(G,0,0,used,occur,result)
        
        for i in occur:
            if i == False:
                return None
        return result
    return None

def checkIfPossible(G):
    for u in range(len(G)):
        cnt = 0
        for i in G[u]:
            if i == 1:
                cnt += 1

        if cnt >= 2 and cnt % 2 == 0:
            continue
        else:
            return False
    return True

def DFSVisit(G,u,first,used,occur,result=[]):

    for v in range(len(G)):
        if G[v][u] == 1 and (u,v) not in used and (v,u) not in used:
            occur[u] = True
            occur[v] = True
            used.append((u,v))
            if v != first:
                result.append(v)
                DFSVisit(G, v, first,used,occur,result)
            elif v == first:
                DFSVisit(G, u, u,used,occur,result)
                result.append(v)
    
    return result


G1 = [
    [0,1,1,0,0,0],
    [1,0,1,1,0,1],
    [1,1,0,0,1,1],
    [0,1,0,0,0,1],
    [0,0,1,0,0,1],
    [0,1,1,1,1,0]]



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

G3 = [
    [0,1,0,0,0,1,0,0,0],
    [1,0,1,0,1,1,0,0,0],
    [0,1,0,1,1,1,0,0,0],
    [0,0,1,0,1,0,0,0,0],
    [0,1,1,1,0,1,0,0,0],
    [1,1,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,0]
]

G = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

G5 = [
    [0,1,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0],
    [0,1,0,1,1,1,0,0],
    [0,0,1,0,1,1,1,0],
    [0,0,1,1,0,1,1,0],
    [0,0,1,1,1,0,1,0],
    [0,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0]
]

print(DFS(G5))