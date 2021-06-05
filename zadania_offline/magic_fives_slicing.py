from random import randint, shuffle, seed
import math

def insertion_sort(t):
    n = len(t)
    for i in range(1,n):
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

def magic_fives(A,k):

    fives = [A[i : i+5] for i in range(0,len(A),5)]
    for i in fives:
        insertion_sort(i)
    
    medians = [five[len(five) // 2] for five in fives]

    if len(medians) <= 5:
        insertion_sort(medians)
        pivot = medians[len(medians)//2]
    else:
        pivot = magic_fives(medians, len(medians)//2)
    
    p = partition(A, pivot)

    if p == k:
        return pivot
    
    if k < p:
        return magic_fives(A[:p], k)
    else:
        return magic_fives(A[p+1:], k - p - 1)


seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = magic_fives( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")