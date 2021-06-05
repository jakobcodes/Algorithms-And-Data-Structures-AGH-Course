def search_uni(T, U):
    if len(T) != 1:
        half = len(T) // 2
        search_uni(T[half:], U)
        search_uni(T[:half], U)
    elif T[0] not in U:
        U.append(T[0])
    return U


def count_uni(T, U, I):
    if len(T) != 1:
        half = len(T) // 2
        count_uni(T[half:], U, I)
        count_uni(T[:half], U, I)
    else:
        for i in range(len(U)):
            if T[0] == U[i]:
                I[i] += 1
                break
    return I


def sort_2(T):
    indeks = 0
    U = search_uni(T, []) # [3, 5, 6, 7]
    U = insertion_sort(U)
    IU = [0 for  in range(len(U))] #  [0, 0, 0, 0]
    I_U = count_uni(T, U, I_U)
    for i in range(len(U)):
        while I_U[i] != 0:
            T[indeks] = U[i] # n*log(logn)
            indeks += 1
            I_U[i] -= 1
    return T