from copy import deepcopy
from queue import PriorityQueue
from math import inf

# Jakub Łubkowski
# Algorytm to zmodyfikowana wersja dijkstry. C[i] zawiera minimalna przepustowosc krawedzi na sciezce od s do i
# relaxacja dba o to zeby ta minimalna przepustowosc byla jak najwieksza oraz ustawia parenty abym pozniej mogl odczytac sciezke


def max_extending_path( G, s, t ):
  def relax(u,v,poj): # poj - przepustowosc krawedzi (u,v)
        if c[v] < min(c[u],poj): # sprawdzam czy oplaca sie przyjsc do wierzcholka v od wierzcholka u (czy minimalna przepustowosc na tej sciezce bedzie wieksza niz na aktualnej sciezce)
            c[v] = min(c[u],poj)
            parent[v] = u

  Q = PriorityQueue()
  c = [-1 for _ in range(len(G))]
  parent = [-1 for _ in range(len(G))]
  visited = [False for _ in range(len(G))]

  # wstawienie wierzcholka s do kolejki
  Q.put((-inf,s))
  c[s] = inf


  while not Q.empty():
      u = Q.get()[1] # pobranie wierzcholka z kolejki
      visited[u] = True 
      for i in G[u]: # petla przechodzaca po sasiadach u
          relax(u,i[0],i[1]) 
          if visited[i[0]] == False:
              Q.put((-c[i[0]],i[0]))
  
  # odczytanie sciezki, jesli c[t] == 1 to znaczy ze nie udalo nam sie dotrzec do wierzcholka t, zatem zwracamy pusta tablice
  if c[t] != -1:
      result = []
      while t != -1: # przejscie po tablicy parent do wierzcholka s, wierzcholek s to ten co ma parent[s] rowne -1
          result.append(t)
          t = parent[t]
      result.reverse()
      return result

  return []
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
