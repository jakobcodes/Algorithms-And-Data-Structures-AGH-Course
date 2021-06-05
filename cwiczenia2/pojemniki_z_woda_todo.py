def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def partition(A,p,r):
    x = A[r][0][1]
    i = p-1
    for j in range(p,r):
        if A[j][0][1] <= x:
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1] , A[r] = A[r], A[i+1]
    return i+1

def water(A,S):
    upper_border = []
    for i in A:
        upper_border.append(i)

    suma = 0
    i = 0
    quicksort(upper_border,0,len(A)-1)
    while suma <= S and i < len(upper_border):

        container_surface = (abs(upper_border[i][1][0] - upper_border[i][0][0]) * abs(upper_border[i][1][1] - upper_border[i][0][1]))
        suma += container_surface
        i += 1
    
    if suma <= S:
        return i
    return i-1


A = [((10,389),(15,1)),((11,557),(12,3)),((121,16),(67,34)),((13,54),(56,32))]
print(water(A,5000))