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
    
def add(L,val):
    if L != None and L.value == None:
        L.value = val
        return L
    
    p = L
    while p.next != None:
        p = p.next
    
    tmp = Node()
    tmp.value = val
    p.next = tmp
    return L


def merge(L1, L2):
    p = L1
    q = L2
    result = Node()
    while p != None and q != None:
        if p.value < q.value:
            add(result, p.value)
            p = p.next
        else:
            add(result,q.value)
            q = q.next

    while p != None:
        add(result,p.value)
        p = p.next

    while q != None:
        add(result,q.value)
        q = q.next

    return result

t1 = [1,3,5,7,9]
t2 = [2,4,6,8,10]
L1 = tab2list(t1)
L2 = tab2list(t2)
printlist(L1)
printlist(L2)
result = merge(L1,L2)
printlist(result)
