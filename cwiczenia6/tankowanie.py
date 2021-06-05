from math import inf
import random


def tank_a(L,S,t):
    if S[0] > L:
        return "dupa"
    pos = 0
    result = []
    idx = 0
    while pos < t:
        if t - pos <= L:
            print("udalo sie")
            break
        
        isPossible = False
        for i in range(idx,len(S)):
            if S[i] - pos <= L:
                isPossible = True
                best = S[i]
                idx = i

        if isPossible == False:
            return "dupa"
        
        
        pos = best
        result.append(best)

    return result

def tank_b1(L,S,P,t):
    S.append(t)
    P.append(0)
    result = []
    pos = 0
    best_idx = 0
    cost = 0
    fuel = L
    best = inf
    if S[0] > L:
        return "nie da sie"

    for i in range(len(S)):
        if S[i] <= L:
            if P[i] <= best:
                best = P[i]
                best_idx = i
    fuel -= S[best_idx]
    pos = best_idx
    result.append(S[pos])

    if pos == len(S)-1:
        return result,cost

    while True:
        best = inf
        isPossible = False
        for i in range(pos+1,len(S)):
            if S[i] - S[pos] <= L:
                isPossible = True
                if P[i] <= best:
                    best = P[i]
                    best_idx = i
            else:
                break
        if isPossible == False:
            return "nie da sie"

        odleglosc = S[best_idx] - S[pos]
        if P[pos] < best:
            # tankujemy do fulla
            ile = L - fuel
            c = ile*P[pos]
            cost += c
            fuel = L - odleglosc
        
        else:
            # tankujemy tyle zeby dotrzec do tanszej stacji
            if fuel < odleglosc:
                ile = odleglosc - fuel
                c = ile*P[pos]
                cost += c
                fuel = 0
            else:
                ile  = 0
                fuel -= odleglosc
        
        pos = best_idx
        result.append(S[pos])
        if pos == len(S)-1:
            return result,cost
        
def tank_b2(L,S,P,t):
    result = []
    pos = 0
    best_idx = 0
    cost = 0
    fuel = L
    best = inf
    if S[0] > L:
        return "nie da sie"

    for i in range(len(S)):
        if S[i] <= L:
            if P[i] <= best:
                best = P[i]
                best_idx = i
    fuel -= S[best_idx]
    pos = best_idx
    result.append(S[pos])
    while True:
        best = inf
        isPossible = False
        for i in range(pos+1,len(S)):
            if S[i] - S[pos] <= L:
                isPossible = True
                if P[i] <= best:
                    best = P[i]
                    best_idx = i
            else:
                break
        if isPossible == False:
            return "nie da sie"

        # tankowanie do fulla
        ile = L - fuel
        c = ile * P[pos]
        cost += c

        best_cost = inf
        if t - S[best_idx] <= L:
            for i in range(pos+1,len(S)):
                if t - S[i] <= L:
                    dist = S[i] - S[pos]
                    c = dist * P[i]
                    if c < best_cost:
                        best_cost = c
                        best_idx = i


            cost += best_cost
            result.append(S[best_idx])
            return cost, result

        dist = S[best_idx] - S[pos]
        fuel = L - dist

        pos = best_idx
        result.append(S[pos])

        
# L = 14
# S = [1, 9, 15, 16, 17, 27, 28]
# P = [1, 100, 10, 15, 1, 30, 30]
# t = 30
L = 31
S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 2, 10, 15, 22, 30, 32]
t = 35
# L = 10
# S = [3  ,  7,11 ,15 ,18 ,20 , 24   ,29   ,31  , 33,36 ,   42 ]
# P = [1.2,2.1,3.4,5.2,1.4,4.20,1.337,2.115,9.97,6.9,2.5,2.021]
# S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# P = [2, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 1, 2] 
S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 35, 37, 42]
P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 2.6, 2.5, 2.02]
# t = 45
print(S)
# print(tank_a(L,S,t))
print(tank_b2(L, S, P, t))
# print(tank_b2(L, S, P, t))

