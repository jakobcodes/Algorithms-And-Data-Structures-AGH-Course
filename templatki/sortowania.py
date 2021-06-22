def bubble_sort(t):
    n = len(t)
    i = 0
    while i < n-1:
        if t[i] > t[i+1]:
            t[i] , t[i+1] = t[i+1], t[i]
            i = 0
            continue
        i+=1
    return t

def insertion_sort(t):
    n = len(t)
    for i in range(1,n):
        j = i-1
        while j>=0 and t[j]>t[j+1]:
            t[j],t[j+1] = t[j+1], t[j]
            j -= 1
    return t

def selection_sort(t):
    n = len(t)
    for i in range(n):
        m = t[i]
        idx_min = i
        for j in range(i+1,n):
            if t[j] < m:
                m = t[j]
                idx_min = j
        t[i], t[idx_min] = t[idx_min], t[i]
    return t

def heapsort(A):
    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    def parent(i):
        return (i-1)//2

    def buildheap(A):
        n = len(A)
        for i in range(parent(n-1),-1,-1):
            heapify(A,n,i)

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

    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A,i,0)
    return A

def quicksort(A,p,r):
    def partition(A,p,r):
        x = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] <= x:
                i += 1
                A[i] , A[j] = A[j] , A[i]
        A[i+1] , A[r] = A[r], A[i+1]
        return i+1

    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def quicker_sort(A,p,r):
    def partition(A,p,r):
        x = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] <= x:
                i += 1
                A[i] , A[j] = A[j] , A[i]
        A[i+1] , A[r] = A[r], A[i+1]
        return i+1

    while p < r:
        q = partition(A,p,r)
        if q-p <= r-q:
            quicker_sort(A,p,q-1)
            p = q + 1
        else:
            quicker_sort(A,q+1,r)
            r = q - 1

def count_sort(T, f):
    n = len(T)
    B = [0]*n
    C = [0]*n
    for i in range(n):
        C[f(T[i])] += 1
    for i in range(1, n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(n):
        T[i] = B[i]

def bucket_sort(T,a):
    n = len(T)
    buckets = [[] for _ in range(n)]

    # for i in T:
        # x = log(i,a)
        # buckets[int(x*n)].append(i)
    
    result = []
    for b in buckets:
        insertion_sort(b,a)
        result += b

    return result

def mergesort(T):
    def merge(L, R):
        i, j, z, result = 0, 0, 0, []
        result += L[:]
        result += R[:]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                result[z] = L[i]
                i += 1
            else:
                result[z] = R[j]
                j += 1
            z += 1
        for a in range(j, len(R)):
            result[z] = R[a]
            z += 1
        for a in range(i, len(L)):
            result[z] = L[a]
            z += 1
        return result

    if len(T) <= 1:
        return T
    half = len(T) // 2
    L = mergesort(T[:half])
    R = mergesort(T[half:])
    return merge(L, R)

