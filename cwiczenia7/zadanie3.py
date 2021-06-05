
def loading(K, W):
    result  = []
    W.sort(reverse=True)
    suma = 0
    for w in W:
        if suma + w <= K:
            suma += w
            result.append(w)
    
    return result, suma

W = [2,2,4,8,1,8,16]
print(loading(27,W))


