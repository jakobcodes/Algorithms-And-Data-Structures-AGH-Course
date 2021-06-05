from queue import PriorityQueue
from math import inf

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

# Jakub Łubkowski 406077
# Algorytm tworzy tablice H rozmiaru (2n-1) x 2, szuka 2 najmniejszych wartosci, nastepnie laczy te "drzewa" w jedno
# zapisuje ich sume w nowej komorce i lewej galezi przypisuje wartosc 0 a prawej 1. Aby stworzyc polaczenie lewej i prawej galezi
# przypisujemy w drugim wierszu indeks nowo stworzonego drzewa, dzieki niemu odczytamy sciezke. Nastepnie algorytm sie powtarza. 

def huffman( S, F ):
    # dodaje pomocnicza wartosc do tablicy F ktora zawiera indeksy danych elementow,
    # abym mogl ja posortowac i wciaz wiedziec ktory element jest ktory
  for i in range(len(F)):
        F[i] = (F[i], i)


  F.sort(key=lambda F: F[0]) # sortuje tablice F

  new_S = [] # tworze nowa tablice S ktora bedzie w takiej kolejnosci jak posortowana F
  for i in range(len(F)):
      new_S.append(S[F[i][1]])
      F[i] = F[i][0] # usuwam wczesniej zrobiona krotke gdyz nie jest juz mi potrzebna
  

  H = [F+[inf]*(len(F)-1),[-1] * (2*len(F)-1)] # tworze tablice H 
  

  k = len(F) # od tego momentu zaczne uzupelniac tablice nowo powstalymi "drzewami"
  p_val = inf # pierwsza najmniejsza wartosc
  q_val = inf # druga najmniejsza wartosc
  p = 0 # indeks pierwszej wartosci
  q = 0 # indeks drugiej wartosci
  # szukanie dwoch sumboli o najmniejszych czestosci, ktore zawieraja -1 w drugim wierszu 
  for i in range(len(F)-1):
      for j in range(i,len(H[0])):
          if H[0][j] <= q_val and H[1][j] == -1:
              q_val = H[0][j]
              q = j
              if H[0][j] < p_val:
                  q_val = p_val
                  p_val = H[0][j]
                  q = p
                  p = j
      
      H[0][k] = H[0][p] + H[0][q] # w pierwszej wolnej komorce wpisujemy sume czestosci symboli
      H[1][p] = k # w drugim wierszu zapisujemy indeks nowo utworzonego symbolu
      H[1][q] = k # 
      H[0][p] = 0 # wartosc czestosci symbolu p zamieniam na 0
      H[0][q] = 1 # wartosc czestosci symbolu q zamieniam na 1
      k += 1

      p_val = inf
      q_val = inf
              
  # printowanie odpowiedzi
  result = [] # tablia wynikow
  suma = 0 # zmienna przechowujaca laczna liczba bitow potrzebna do wypisania napisu
  for i in range(len(S)):
      r = []
      for j in range(len(new_S)):
          if new_S[j] == S[i]:
              k = j # rozpoczynamy od pola symbolu idziemy do pola 2n-1 korzystajac z drugiego wiersza tab H, zapisujemy wartosci z pierwszego wiersza
              while H[1][k] != -1:
                  r.append(H[0][k])
                  k = H[1][k]
              r.reverse() # powstaly ciag nalezy jeszcze odwrocic aby otrzymac zapis sciezki do symbolu
              suma += len(r)*F[j]
              result.append(r) # dodajemy do tablicy wynikow juz w dobrej kolejnosci
  
  # printowanie wyniku
  for i in range(len(S)):
      print(S[i] + " : ",end="")
      for j in result[i]:
          print(j,end="")
      print()

  print("dlugosc napisu: ", end="")
  print(suma)
  
  
  
huffman( S, F )