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
    
    prev = None
    p = root
    lewo = None
    while p != None:
        if key == p.key:
            print("element juz istnieje")
            return False
        elif key < p.key:
            prev = p
            p = p.left
            lewo = True
        else:
            prev = p
            p = p.right
            lewo = False
    
    if lewo:
        prev.left = BSTNode(key)
        prev.left.parent = prev
        return True
    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev
        return True

def remove(root, key):
    pass

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
    print_tree(root)
    