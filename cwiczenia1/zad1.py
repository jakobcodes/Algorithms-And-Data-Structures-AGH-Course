from random import randint 

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



        


t = [randint(1,9) for _ in range(10)]
print(t)
t = selection_sort(t)
print(t)