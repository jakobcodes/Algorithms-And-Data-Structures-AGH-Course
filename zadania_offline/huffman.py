from math import inf

def huffman(S,F):
    for i in range(len(F)):
        F[i] = (F[i], i)


    F.sort(key=lambda F: F[0])

    new_S = []
    for i in range(len(F)):
        new_S.append(S[F[i][1]])
        F[i] = F[i][0]
    print(new_S)
    print(F)
    

    H = [F+[inf]*(len(F)-1),[-1] * (2*len(F)-1)]
    for i in H:
        print(i)
    
    i = 0
    k = len(F)
    p_val = inf
    q_val = inf
    p = 0
    q = 0
    for i in range(len(F)-1):
        for j in range(i,len(H[0])):
            if H[0][j] <= q_val and H[1][j] == -1:
                q_val = H[0][j]
                q = j
                if H[0][j] < p_val:
                    q_val = p_val
                    p_val = H[0][j]
                    q = p
                    p = j
        
        H[0][k] = H[0][p] + H[0][q]
        H[1][p] = k
        H[1][q] = k
        H[0][p] = 0
        H[0][q] = 1
        k += 1

        p_val = inf
        q_val = inf
                
    for i in H:
        print(i)
    
    result = []
    suma = 0
    for i in range(len(S)):
        r = []
        for j in range(len(new_S)):
            if new_S[j] == S[i]:
                k = j
                while H[1][k] != -1:
                    r.append(H[0][k])
                    k = H[1][k]
                r.reverse()
                suma += len(r)*F[j]
                result.append(r)
    
    print(result)
    for i in range(len(S)):
        print(S[i] + " : ",end="")
        for j in result[i]:
            print(j,end="")
        print()

    print("dlugosc napisu: ", end="")
    print(suma)


S = ["a", "b", "c", "d", "e", "f"]
F = [ 10 , 11 , 7 , 13 , 1 , 20 ]
# S = ["a", "b", "c", "d", "e"]
# F = [0.1,0.1,0.15,0.2,0.45]
huffman(S,F)