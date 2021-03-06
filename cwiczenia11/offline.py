class BSTNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
def print_tree(root, key="key", left="left", right="right"):
    def display(root, key=key, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, key, left, right)
    for line in lines:
        print(line)

def insert(root, key):
    if root == None:
        root = BSTNode(key)
        return True

    # zakladam raczej ze root bedzie dobrze podany
    prev = None
    p = root
    left = None # True - p jest lewym dzieckiem prev, False - p jest prawym dzieckiem prev
    while p != None:
        if key == p.key:
            print("element juz istnieje")
            return False
        elif key < p.key:
            prev = p
            p = p.left
            left = True
        else:
            prev = p
            p = p.right
            left = False
    
    if left:
        prev.left = BSTNode(key)
        prev.left.parent = prev
        return True
    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
        return True

def remove(root, key):
    # krotka implementacja znalezienia poprzednika, nie jest potrzebna mi pelna implementacja poniewaz zawsze mam lewe dziecko
    def find_prev(p):
        p = p.left
        while p.right != None:
            p = p.right
        
        return p

    if root == None or root.key == None:
        print("BST is empty")
        return False

    # delete root
    if root.key == key:
        if root.left == None and root.right == None: # BST tree with only root node
            root.key = None
            return True

        
        if find_prev(root) != None:
            tmp = find_prev(root) # jesli nie istnieje
        # else:
        #     tmp = find_next(root)

        remove(root,tmp.key)
        root.key = tmp.key
        return True

        

    prev = None
    p = root
    left = None
    # finding element to delete loop
    while p != None:
        if p.key == key:
            # element found
            if p.left == None and p.right == None: # no childrens
                p.parent = None
                if left:
                    prev.left = None
                else:
                    prev.right = None
                return True

            elif p.left == None or p.right == None: # one children exists (left or right)
                if left: # left children exist
                    if p.left != None:
                        prev.left = p.left
                        p.left = None
                    else:
                        prev.left = p.right
                        p.right = None
                    
                else: # right children exist
                    if p.left != None:
                        prev.right = p.left
                        p.left = None
                    else:
                        prev.right = p.right
                        p.right = None

                p.parent = None
                return True
            else: # both childrens exist
                tmp = find_prev(p)
                remove(root,tmp.key)
                p.key = tmp.key
                return True
                
        elif key < p.key:
            # go left
            prev = p
            p = p.left
            left = True

        else:
            # go right
            prev = p
            p = p.right
            left = False
    
    print("element not found")
    return False

# def find_idx(root,idx):

#     if idx <= root.left.value:
#         root = root.left
#         if root.value == idx:
#             while root.right != None:
#                 root = root.right
#             return root

#     else:
#         idx -= root.left.value
#         if idx > 1:
#             root = root.right
#             idx -= 1
#         else:
#             return root

if __name__ == '__main__':
    root = BSTNode(20)
    print(insert(root,10))
    print(insert(root,5))
    print(insert(root,15))
    print(insert(root,27))
    print(insert(root,22))
    print(insert(root,30))
    print(insert(root,28))
    print(insert(root,35))
    print(insert(root,40))
    print(insert(root,13))
    print(insert(root,21))
    print(insert(root,23))
    print(insert(root,34))
    print_tree(root)

    