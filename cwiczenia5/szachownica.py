def chessboard(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    F[0][0] = A[0][0]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                F[i][j] = F[i][j-1] + A[i][j]
            elif j == 0:
                F[i][j] = F[i-1][j] + A[i][j]
            else:
                F[i][j] = min(F[i-1][j]+A[i][j], F[i][j-1] + A[i][j])
            
    return F[-1][-1], F

A = [[1,100,0,0],
     [99,2,1,0],
     [1,2,1,0],
     [1,2,99,2]
]
B = [[4,0,2,1],
     [0,0,2,1],
     [1,0,0,4],
     [0,3,0,1]]

for i in B:
    print(i)
print()
res = chessboard(B)[1]
for i in res:
    print(i)
print(chessboard(B)[0])
