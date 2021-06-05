# Jakub Łubkowski 406077
# program znajduje najdluzsze podciagi, dodaje je do pomocniczej tablicy, a nastepnie printuje je i zwraca ich ilosc


# Funkcja LIS zwraca: dlugosc najdluzszego podciagu, tablicę F - zawiera dlugosci podciagow,
# tablicę P - przechowuje indeksy do kolejnych elementow w danym podciagu 
def lis(A):
    n = len(A)
    F = [1] * n
    P = [[-1] for _ in range(n)] 
    # szukam malejących podciagow od konca tablicy do poczatku,
    # wypełniam tablice F
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    
    # na bazie tablicy F i A, tworze tablice P
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if F[j]+1 == F[i] and A[j] > A[i]:
                if P[i] == [-1]:
                    P[i] = [j]
                else:
                    P[i].append(j)
    
    return(max(F), F, P)

# głowna funkcja- printuje podciagi oraz zwraca ich ilosc
def printAllLIS(A):

    n = len(A)
    max_value, F, P = lis(A)
    R = [[] for _ in range(n)] # tworze pomocnicza tablice R do ktorej bede wstawial najdluzsze podciagi
    
    for i in range(len(F)): # wywoluje funkcje print_solution dla elementow ktore zaczynają najdluższe podciagi
        if F[i] == max_value:
            res = (print_solution(A,P,i,[],R,max_value,i))

    # printuje najdluzsze znalezione podciagi, a przy okazji je zliczam 
    count = 0
    for i in res:
        for j in i:
            print(*j, sep = ' ')
            count += 1
    return count

# funkcja rekurencyjna, ktora znajduje najdluzsze podciagi,
# a nastepnie "appenduje" je do tablicy R w odpowiednie miejsca,aby zachowana była kolejność
def print_solution(A, P, i, result,R,max_value,i_R):
    # jesli element nie jest ostani wywoluje sie rekurencyjnie
    if P[i] != [-1]:
        print_solution(A,P,P[i][0],result + [A[i]],R,max_value,i_R)
        # for wywola sie gdy w P[i] jest wiecej elementow niz 1
        for j in range(1,len(P[i])):
            print_solution(A,P,P[i][j],result + [A[i]],R,max_value,i_R)
    
    # dodanie ostatniego elementu
    result.append(A[i])
    # dodanie podciagu do tablicy R, jesli spelnia on zalozenia, czyli jest dlugosci max_value
    if len(result) == max_value:
        R[i_R].append(result)

    return R






