from math import inf

def tspf2 (i, j, F, D, B):

    if F[i][j] != inf:
        return F[i][j]

    if i == j - 1:
        best = inf
        idx = -1
        for k in range(j - 1):
            tmp = tspf2(k, j - 1, F, D, B) + D[k][j]
            if tmp < best:
                best = tmp
                idx = k

        F[j - 1][j] = best
        # B[j - 1][j] = idx
        B.append(idx)
    else:
        F[i][j] = tspf2(i, j - 1, F, D, B) + D[j - 1][j]
        # B[i][j] = j - 1
        B.append(j-1)
    return F[i][j]

def tspf(i,j,F,D):
    if F[i][j] != inf:
        return F[i][j]

    if i == j-1:
        best = inf
        for k in range(j-1):
            best = min(best,tspf(k,j-1,F,D) + D[k][j])
        
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i,j-1,F,D) + D[j-1][j]
    return F[i][j]

def print_array(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end=" ")
        print()

def get_distance(A, i, j):
    return (((A[j][1] - A[i][1])**2 + (A[j][2] - A[i][2])**2)**0.5)

def find_min(j,F,D):
    best = inf
    best_idx = 0
    for k in range(j-1):
        x = F[k][j] + D[k][j]
        if x < best:
            best = x
            best_idx = k
    return best_idx

if __name__ == "__main__":
    
    C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
    # C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
    # C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2,4], ["Kraków", 3, 1],["paprykarz szczecinski", 1, 3],["Rzeszow",5,2]]#["paprykarz szczecinski", 1, 3]]
    C.sort(key = lambda C : C[1])
    print(C)
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = get_distance(C,i,j)
    # print_array(D)
    F[0][1] = D[0][1]
    
    
    for i in range(n-1):
        tspf(i,n-1,F,D)

    # rout_i = []
    # rout_j = []
    # route = []
    # best_idx = find_min(n-1,F,D)
    # i = best_idx
    # j = n-1
    # while j > 0:
    #     dupa = find_min(j,F,D):
    #     if F[j-1][j] + D[j-1][j] <= F[dupa][j] + D[dupa][j]:
    #         rout_j.append(j)
    #         j -= 1
    #     else:
            

    # while j > 0:
    #     best_idx = find_min(j,F,D)
    #     if best_idx < j-1:
    #         rout_j.append(C[j-1])
    #         print("if")
    #         j = j-1
    #     else:
    #         k = find_min(j,F,D)
    #         rout_j.append(C[j])
    #         print("else")
    #         rout_i, rout_j = rout_j, rout_i
    #         j = j-1
    #         i = k
    # j = n-1
    # while j > 0:
    #     best_idx = find_min(j,F,D)
    #     if best_idx == j-1:
    #         rout_i.append(best_idx)
    #         j = j-1
    #     else:
    #         route.append(j-1)
    #         j = j-1

    print(rout_i)
    print(rout_j)

    



