from random import randint, seed

class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

def qsort( L ):
  def getlast(L):
    while L.next != None:
        L = L.next
    return L

  # pp - przed pivotem, p1 - pivot
  # i - elem przed j, j - elem przechodzacy po liscie
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
        x = qsort(first)
        first = x
        while x.next != None:
            x = x.next
        y = qsort(p1)
        x.next = y
    else:
        qsort(p1)
  L = first
  return L


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

  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

