def domowe(A):
    n = len(A)
    C = [0 for _ in range(n)]
    B = [0 for _ in range(len(A))]
    for i in A:
        C[i%n] += 1
    
    for i in range(1,n):
        C[i] += C[i-1]
    
    for i in range(len(A)-1,-1,-1):
        C[A[i]%n] -= 1
        B[C[A[i]%n]] = A[i]
    
    for i in range(len(A)):
        A[i] = B[i]

    C = [0 for _ in range(n)]
    B = [0 for _ in range(len(A))]

    for i in A:
        C[i//n] += 1
    
    for i in range(1,n):
        C[i] += C[i-1]
    
    for i in range(len(A)-1,-1,-1):
        C[A[i]//n] -= 1
        B[C[A[i]//n]] = A[i]
    
    for i in range(len(A)):
        A[i] = B[i]
    
t = [80,56,44,12,1,10,16,32,24]
print(t)
domowe(t)
print(t)
