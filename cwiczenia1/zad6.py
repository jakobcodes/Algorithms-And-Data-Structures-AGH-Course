# wyszukiwanie binarne

def search(t, x):
    n = len(t)
    left = 0
    right = n
    i = 0
    while left < right:
        i = (left + right) // 2
        if t[i] == x:
            return i
        elif t[i]<x:
            left = i+1
        else:
            right = i
    
    return "x not found"

t = [1,2,3,4,4,4,5,6,7,8,9,10,10,11,11,12]
print(search(t,1))


            
    