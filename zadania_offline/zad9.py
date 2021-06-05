from copy import deepcopy
from queue import PriorityQueue
from math import inf
# Jakub Łubkowski
# Algorytm usuwa krawedz (u,v) i  wywoluje algorytm dijkstry bez tej krawedzi, sprawdza czy da sie dojsc do wierzcholka v z wierzcholka u,
# jesli sie da to znaczy ze istnieje cykl, nastepnie sprawdza czy waga tego cyklu jest najmniejsza, sposrod innych cyklow w grafie,
# jesli waga jest najmniejsza zapisuje wierzcholek v oraz tablice parent aby pozniej moc odczytac wynik,
# pozniej przywracam usunieta krawedz i usuwam kolejna itd

def dijkstry(G,s):
    def relax(u,v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u
        

    Q = PriorityQueue()
    d = [inf for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    Q.put((0,s))
    d[s] = 0
    
    while not Q.empty():
        u = Q.get()[1]
        for i in range(len(G)):
            if G[u][i] != -1:
                relax(u,i)
                if visited[i] == False:
                    Q.put((d[i],i))
                    visited[u] = True
    
    return d,parent

def min_cycle( G ):
  best = inf
  for u in range(len(G)):
      for v in range(u+1,len(G)):
          if G[u][v] != -1:
              tmp = G[u][v]
              G[u][v] = -1
              G[v][u] = -1
              d,parent = dijkstry(G,u)
              if d[v] != inf:
                  if d[v] + tmp < best:
                      best = d[v] + tmp
                      path = parent
                      x = v
              
              G[u][v] = tmp
              G[v][u] = tmp

  # brak cyklu
  if best == inf:
      return []

  # odczytanie cyklu
  res = []
  while x != -1:
      res.append(x)
      x = path[x]

  return res
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
  
