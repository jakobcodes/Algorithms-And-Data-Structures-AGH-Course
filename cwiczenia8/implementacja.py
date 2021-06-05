
def uniwersalne_ujscie(G):

    potencjalne = []
    for u in range(len(G)):
        findAllZeros = True
        for v in range(len(G)):
            if G[u][v] == 1:
                findAllZeros = False
                break
        
        if findAllZeros == True:
            potencjalne.append(u)
    
    for u in potencjalne:
        checkOnes = True
        for v in range(len(G)):
            if u != v:
                if G[v][u] == 0:
                    checkOnes = False
                    break
        
        if checkOnes == True:
            return u
    
    return None

G = [
    [0,0,1,1,1],
    [0,0,0,0,1],
    [0,1,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,0]
]

print(uniwersalne_ujscie(G))
