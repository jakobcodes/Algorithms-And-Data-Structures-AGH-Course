# Proszę zaimplementować funkcję odwracającą listę jednokierunkową
class Node:
    def __init__(self):
        self.value = None
        self.next = None

def print_list(first):
    p = first
    while p != None:
        print(p.value,end=' ')
        p = p.next
    print()

def create_node(val):
    tmp = Node()
    tmp.value = val
    return tmp

def add_node_to_list(L,nod):
    p = L

    if p.next == None:
        p.next = nod
        return 
    
    while p.next != None:
        p = p.next
    
    p.next = nod

def flip_the_list(L):
    p = L
    NewList = Node()
    while L.next != None:
        p = L
        while p.next.next != None:
            p = p.next

        add_node_to_list(NewList,p.next)
        p.next = None

    return NewList

L = Node()
add_node_to_list(L,create_node(1))
add_node_to_list(L,create_node(2))
add_node_to_list(L,create_node(3))
add_node_to_list(L,create_node(4))
add_node_to_list(L,create_node(5))
add_node_to_list(L,create_node(6))

print_list(L)
L = flip_the_list(L)
print_list(L)


        
        
