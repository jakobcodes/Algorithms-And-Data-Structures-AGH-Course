# szukanie sumy

def szukanie_sumy(t,x):
    i = 0
    j = len(t)-1

    while i < j:
        suma = t[i] + t[j]
        if suma == x:
            return i,j
        
        elif suma < x:
            i += 1
        else:
            j -= 1
        
    return "nie istnieje taka suma"


t = [1,2,3,4,5,6,7,8,9]
print(szukanie_sumy(t,8))