from random import randint, shuffle, seed
import math

def insertion_sort(t,l,r):
    n = r - l + 1
    for i in range(l+1,r):
        j = i-1
        while j>=0 and t[j]>t[j+1]:
            t[j],t[j+1] = t[j+1], t[j]
            j -= 1

def partition(A,pivot):
    l = 0
    r = len(A)-1
    i = 0

    while i <= r:
        if A[i] == pivot:
            i += 1
        
        elif A[i] < pivot:
            A[l] , A[i] = A[i] , A[l]
            l += 1
            i += 1
        else:
            A[r] , A[i] = A[i] , A[r]
            r -= 1
    return l

def magic_fives(A,l,r,k):
    n = r - l + 1 
    
    medians = []
    i = 0
    while i < n//5:
        insertion_sort(A, l + i*5, l + i*5 + 5)
        medians.append(A[l+2])
        i += 1
    
    if n%5 > 0:
        insertion_sort(A, l + i*5, l + i*5 + n%5)
        medians.append(A[l + n%5//2])
    
    if len(medians) <= 5:
        insertion_sort(medians,0,len(medians)-1)
        pivot = medians[len(medians)//2]
    else:
        pivot = magic_fives(medians, 0, len(medians)-1, len(medians)//2)

    p = partition(A,pivot)

    if p == k:
        return pivot
    
    if k < p:
        return magic_fives(A, l, p-1, k)
    else:
        return magic_fives(A, p+1, r, k)

def linearselect(A,k):
    return magic_fives(A, 0, len(A)-1, k)

seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")