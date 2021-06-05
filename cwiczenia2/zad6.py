
def quicksort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        if q-p <= r-q:
            quicksort(A,p,q-1)
            p = q + 1
        else:
            quicksort(A,q+1,r)
            r = q - 1

def partition(A,p,r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1] , A[r] = A[r], A[i+1]
    return i+1

def przedzialy(A):
    quicksort(A,0,len(A)-1)
    B = [0 for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(i-1,-1,-1):
            if A[j][0] > A[i][0]:
                B[i] += 1

            if A[j][1] < A[i][0]:
                break
    
    best = 0
    idx = 0
    for i in range(len(B)):
        if B[i] > best:
            best = B[i]
            idx = i
    
    return A[idx]

T=[(1,6),(3,5),(2,10),(4,7),(5,8),(9,11)]
print(przedzialy(T))


