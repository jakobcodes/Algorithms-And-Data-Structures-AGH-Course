import random

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

t = [random.randint(0,10) for _ in range(10)]
L = tab2list(t)
printlist(L)

def getlast(L):
    while L.next != None:
        L = L.next
    return L

def partition(L,p):
    if L == p:
        return 
    i = L
    j = L
    while j != p:
        if j.value < p.value:
            i.value , j.value = j.value, i.value
            i = i.next
        j = j.next
    p.value , i.value = i.value, p.value
    q = L
    while q.next != i:
        q = q.next

    partition(L,q)
    partition(i,getLast(i))

def quicksort(L):
    first = L
    if L.next != None:
        p = getlast(L)
        val = p.value
        i = pp = None
        p1 = p
        j = L
        while j != p1:
            if j.value > val:
                if i == None:
                    p.next = j
                    j = j.next
                    first = j
                    p = p.next
                    p.next = None
                else:
                    p.next = j
                    j = j.next
                    p = p.next
                    p.next = None
                    i.next = j
                    
            else:
                i = j
                pp = j
                j = j.next
        
        if pp != None:
            pp.next = None
            x = quicksort(first)
            first = x
            while x.next != None:
                x = x.next
            y = quicksort(p1)
            x.next = y
        else:
            quicksort(p1)

    return first

    
    
        

def qsort(L, s):
    if s == None or L == s:
        return
    second = s.next
    s.next = None
    if L.next != None:
        pivot = getlast(L)
        x = pivot
        p = Node()
        p.next = L
        L = p

        while p.next != pivot:

            if p.next.value > pivot.value:
                tmp = p.next
                p.next = tmp.next
                x.next = tmp
                x = x.next
                x.next = None
                del tmp

            elif p.next.value == pivot.value:
                tmp = p.next
                p.next = tmp.next
                tmp.next = pivot.next
                pivot.next = tmp
                if p.value == None and x == pivot:
                    x = pivot.next
                del tmp

            elif p.next.value < pivot.value:
                p = p.next

        printlist(L.next)
        L = L.next
        i = L
        j = pivot
        
        while i != None and i.next != pivot:
            i = i.next
        qsort(L,i)

        while j != None and j.value == pivot.value:
            j = j.next

        qsort(j,getlast(j))

def partition3(L):

    pivot = getlast(L)
    x = pivot
    p = Node()
    p.next = L
    L = p

    while p.next != pivot:

        if p.next.value > pivot.value:
            tmp = p.next
            p.next = tmp.next
            x.next = tmp
            x = x.next
            x.next = None
            del tmp

        elif p.next.value == pivot.value:
            tmp = p.next
            p.next = tmp.next
            tmp.next = pivot.next
            pivot.next = tmp
            if p.value == None and x == pivot:
                x = pivot.next
            del tmp

        elif p.next.value < pivot.value:
            p = p.next


t = quicksort(L)
printlist(t)

    
    





    