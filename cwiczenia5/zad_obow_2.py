def findSubsequence(A,x):
    n = len(A)
    F = [[1] + [0] * x for _ in range(n)]
    if A[0] <= x:
        F[0][A[0]] = 1
    
    for i in range(1,n):
        for s in range(1,x+1):
            F[i][s] = F[i-1][s]
            if A[i] <= s and F[i][s] == 0:
                F[i][s] = F[i-1][s-A[i]]

    return F[n-1][x], F

A = [3,4,9,33,5]
result,F = findSubsequence(A,10)
for i in F:
    print(i)
print(result)