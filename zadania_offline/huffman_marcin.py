def printsolution(res, S, F, S2, N): #funkcja wypisujaca rozwiazanie


    cnt = 0 #do zliczania  łącznej liczby bitów potrzebnej do wypisania napisu
    for k in S2:
        for i in range(N):#wypisywanie elementow w kolejnosci takiej jak byly podane
            if S[i] == k:
                sol = [res[i][0]]
                iter = res[i][1]
                print(S[i], end=": ")

                while res[iter][1] != 100000: #tworzenie ciagu wynikowego dla danego drzewa
                    sol = sol + [res[iter][0]]
                    iter = res[iter][1]

                cnt += F[i]*len(sol)

                sol.reverse() #ciag jest odczytany do kocna dlatego trzeba jeszcze odwrocic tablice wynikowa
                print(*sol, sep = " ")

    print("Dlugosc napisu: ", cnt)
    return cnt


def hufman(F, S):
    inf = 100000
    N = len(S)
    S2 = S[:N] #kopia wejsciowej tablicy znakow, potrzebna do wypisywania zgodnie z kolejnoscia

    quicksort(F, S, 0, len(F) - 1) #sortowanie talibc F i S po wartościach w tablicy F
    res = [[inf] * 2 for _ in range(2*N - 1)]   #tworzenie talibyc o wyiarach 2* 2*N - 1, tablica przechowuje kopiec z rozwiazaniem
    for i in range(N): #przepisywanie wartosci z F do S, potrzebne żeby w dalszej części programu odpowiednio dobierac wartosci zgodnie z zalozeniem kodowania huffmana
        res[i][0] = F[i]

    #mozna by obejsc sie bez tych zmiennych, jednak rozwiazanie wydaje sie bardziej zrozumiale na pierwszy rzut oka
    min1 = inf
    idmin1 = 0
    min2 = inf
    idmin2 = 0
    #opis rozwiazania
    #wyszukiwanie 2 drzew o najmniejszej wartosci
    for i in range(0, N - 1):
        for j in range(i, N + i):
            if min1 > res[j][0] and res[j][1] == inf:
                min2 = min1
                idmin2 = idmin1
                min1 = res[j][0]
                idmin1 = j

            elif min2 >= res[j][0] and res[j][1] == inf:
                min2 = res[j][0]
                idmin2 = j


        #tworzenie nowego drzewa o wartosci będącej sumą 2 drzew o minimalnej wartosci
        res[i + N][0] = min1 + min2
        #zapisywanie numeru nowego drzewka (wpisuje pod indeksy min1 i min2 - to znaczy ze nowe drzewo skalada sie wlasnie z tych drzew)
        res[idmin1][1] = N + i
        res[idmin2][1] = N + i
        #lewa galąź nowego drzewka ustawiam na 0, prawą na 1
        res[idmin1][0] = 0
        res[idmin2][0] = 1
        #resetuje min'y zeby powtarzac algorytm dopoki wszystkie drzewa nie sa polaczone
        min1 = inf
        min2 = inf

    printsolution(res, S, F, S2, N)