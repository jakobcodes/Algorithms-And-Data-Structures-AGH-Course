class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def add(first,val):
    
    if first.value == None:
        first.value = val
        return

    p = first
    while p.next != None:
        p = p.next

    tmp = Node(val)
    p.next = tmp

def sort_my_list(first):
    p = first
    while p.next != None:
        if p.next.value < p.value:
            p.value, p.next.value = p.next.value, p.value #swap values
            p = first
        else:
            p = p.next
    return first

def print_list(first):
    p = first
    while p != None:
        print(p.value,end=' ')
        p = p.next
    print()

def insert_to_sorted_list(first,val):
    p = first
    # insert to empty list
    if p == None:
        return Node(val)

    while p.next != None and val > p.next.value:
        p = p.next
    
    tmp = Node(val)
    tmp.next = p.next
    p.next = tmp
    return first
def delete_max(first):
    p = first
    m = p.value
    while p != None:
        if p.value > m:
            m = p.value
        p = p.next
    p = first
    prev = None
    while p.value != m:
        prev = p
        p = p.next
        
    #usuwanie elem
    if prev == None: #element jest na pierwszym miejscu
        first = first.next
        del p
    else:
        prev.next = p.next
    return first
    
def selection_sort(L):
    p = L
    q = L
    m = p.value
    while q != None:
        m = q.value
        w = q
        p = q
        while p != None:
            if p.value < m:
                m = p.value
                w = p
            p = p.next
        print(m)
        q.value, w.value = w.value, q.value
        q = q.next
        
     
         

if __name__ == "__main__":
    first = Node(6)
    add(first,3)
    add(first,2)
    add(first,0)
    add(first,4)
    add(first,2)
    add(first,4)
    add(first,5)
    add(first,6)
    print_list(first)
    # sort_my_list(first)
    selection_sort(first)
    print_list(first)


