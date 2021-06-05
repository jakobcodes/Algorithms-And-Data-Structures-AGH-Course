import random

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-1)//2

def heapify(A,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    
    if m != i:
        A[i],A[m] = A[m],A[i]
        heapify(A,n,m)

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A,i,0)
    return A

def insert_to_heap(A,val):
    A.append(val)
    n = len(A)
    i = n-1
    while i != 0:
        if A[i] > A[parent(i)]:
            A[i] , A[parent(i)] = A[parent(i)], A[i]
            i = parent(i)
        else:
            break
        
    return A

    
if __name__ == "__main__":
    t = [random.randint(0,20) for _ in range(10)]
    print(t)
    buildheap(t)
    print(t)
    print(insert_to_heap(t,21))
    



