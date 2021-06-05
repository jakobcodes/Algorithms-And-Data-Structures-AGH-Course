import random, time

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1] , A[r] = A[r], A[i+1]
    return i+1

def quicker_sort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        if q-p <= r-q:
            quicker_sort(A,p,q-1)
            p = q + 1
        else:
            quicker_sort(A,q+1,r)
            r = q - 1
        

A = [random.randint(0,9) for _ in range(100000)]
N = A

# print(A)
# t1 = time.time()
# quicksort(A,0,len(A)-1)
# t2 = time.time()
# print(f"quicksort, czas: {t2-t1}")

# print(N)
t1 = time.time()
quicker_sort(N,0,len(N)-1)
t2 = time.time()
print(f"quicker_sort, czas: {t2-t1}")

