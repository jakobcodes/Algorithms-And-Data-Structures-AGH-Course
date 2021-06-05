
def knapsack3(W,V,MaxW):
    n = len(V)
    mxs = sum(V)
    F = [[10000 for _ in range(mxs+1)] for _ in range(n)]

    F[0][V[0]] = W[0]

    sumt = [0 for _ in range(n)]

    for i in range(n):
        sumt[i] = sumt[i-1] + V[i]

    for i in range(1,n):
        for s in range(1,sumt[i]+1):
            F[i][s] = F[i-1][s]
            if V[i] <= s:
                F[i][s] = min(F[i][s], F[i-1][s-V[i]] + W[i])
    
    result = mxs
    for i in range(len(F[n-1])):
        print(i,F[n-1][i])

    while F[n-1][result] > MaxW:
        result -= 1
    print(result)
    return result

    return F

W = [4,5,12,9,1,13]
V = [10,8,4,5,3,7]
res = knapsack3(W,V,20)
# print(get_solution(res,W,V,24))
