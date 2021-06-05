# Jakub Łubkowski    406077
# Algorytm sprawdza czy istnieje cykl Eulera, jesli tak to szuka "cykli" i laczy je w jeden cykl Eulera

from copy import deepcopy


def euler(G):
    def DFS(G):
        if checkIfPossible(G): 
            used = [] # tutaj bede zapisywal uzyte krawedzie, zeby nie przejsc przez dana krawedz 2 razy
            result = [0] # cykl Eulera
            occur = [False for _ in range(len(G))] # tablica pomocnicza aby sprawdzic czy odwiedziłem kazdy wierzchołek (spójność grafu)
            result = DFSVisit(G,0,0,used,occur,result) # wywołuje funkcje DFSVisit dla pierwszego wierzchołka
            
            # sprawdzam czy graf jest spójny czyli czy udalo mi sie przejsc po kazdym wierzchołku
            for i in occur:
                if i == False:
                    return None

            return result
        
        return None
    
    # Funkcja sprawdza czy graf posiada cykl Eulera, o ile jest on spójny(później spójność będzie sprawdzana)
    def checkIfPossible(G):
        for u in range(len(G)):
            cnt = 0
            for i in G[u]:
                if i == 1:
                    cnt += 1

            if cnt >= 2 and cnt % 2 == 0: # czy stopień wierzchołka jest parzysty i co najmniej 2
                continue
            else:
                return False
        return True

    # funkcja rekurencyjna znajdująca cykl, G - graf, u - wierzchołek na którym jestem, first - wierzchołek rozpoczynający dany cykl(jeden z cykli z których stworzony zostanie cykl Eulera)
    def DFSVisit(G,u,first,used,occur,result=[]):
        # petla przechodzaca po sasiadach wierzchołka na którym jestesmy
        for v in range(len(G)):
            if G[v][u] == 1 and (u,v) not in used and (v,u) not in used: # sprawdzamy czy istnieje krawedz do danego wierzchołka i czy jeszcze jej nie "użylismy"
                occur[u] = True # odznaczam wierzcholki ze sie pojawily
                occur[v] = True
                used.append((u,v)) # dodaje krawedz do uzytych
                if v != first:  # sprawdzam czy jesli przejde z u do v to czy skonczy mi sie obecny cykl, jesli nie to dodaje v i uruchamiam DFSVisit dalej
                    result.append(v) # dodaje wierzcholek do ktorego "ide" do wyniku
                    DFSVisit(G, v, first,used,occur,result)
                elif v == first: # jesli przechodzac z u do v koncze obecny cykl, rozpoczynam kolejny gdzie u jest pierwszym wierzcholkiem w kolejnym cyklu
                    DFSVisit(G, u, u,used,occur,result)
                    result.append(v) # dodaje ostani wierzcholek obecnego cyklu
        return result
    return DFS(G)


# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
# funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
