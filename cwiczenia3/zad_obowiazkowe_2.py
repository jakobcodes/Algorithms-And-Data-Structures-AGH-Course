def binarySearch (T, i, j, x):
    if (i > j):
        return None
    c = (i + j) // 2
    if (T[c] == x):
        retval = binarySearch(T, i, c - 1, x)
        if (retval == None): return c
        return retval
    if (T[c] > x):
        return binarySearch(T, i, c - 1, x)
    else:
        return binarySearch(T, c + 1, j, x)

def zaddom(A):
    C = []
    for i in range(len(A)):
        if  binarySearch(C,0, len(C) - 1, A[i]) == None: #dla kazdego z n elementów w tablicy dlugosci log(n) szukam bs'em czy element nalezy
            j = len(C)-1
            C.append(A[i])
            while j >= 0 and C[j] > C[j+1]:
                C[j], C[j+1] = C[j+1], C[j]
                j -= 1

    D = [0]*len(C)
    for i in A:
        D[binarySearch(C,0, len(C) - 1, i)] += 1
    print(D)

    x = 0
    y = 0
    for i in D:
        for j in range(i):
            A[x] = C[y]
            x += 1
        y += 1

T = [1, 1, 1, 3, 4, 2, 2, 2]
zaddom(T)
print(T)