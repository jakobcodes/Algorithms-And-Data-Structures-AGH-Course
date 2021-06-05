from random import randint, seed

seed(420)

def main(A,B):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if A[i] == B[0]:
            while i < n:
                F[0][i] = 1
                i += 1
            break

    for i in range(n):
        if B[i] == A[0]:
            while i < n:
                F[i][0] = 1
                i += 1
            break
    
    

    for i in range(1,n):
        found = False
        for j in range(1,n):
            if B[i] == A[j] and found == False:
                found = True
                xd = max(F[i-1][j], F[i][j-1] + 1)
                F[i][j] = xd
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    
    for i in F:
        print(i)


A = [randint(1,20) for _ in range(10)]
B = [randint(1,20) for _ in range(10)]

# A = [1,1,1,2,3,6,10]
# B = [1,2,3,6,10,11,12]
print(A)
print(B)
main(A,B)