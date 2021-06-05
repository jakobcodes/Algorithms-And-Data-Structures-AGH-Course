def main(A,k):

    F = [[0 for _ in range(k)] for _ in range(len(A))]
    odp = [i for i in range(k)]
    

    for i in range(k):
        F[k-1][i] = A[i]
    
    

    for i in range(k,len(A)):
        p = k-2
        q = k-1
        
        
    return F

A = [1,2,3,2,4,6,11,1,12,13,2,3,0]
k = 5
F = main(A,k)
for i in F:
    print(i)