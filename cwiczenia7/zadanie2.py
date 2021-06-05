import random

def job_sequeencing(T, limit_time):
    T.sort(key=lambda x: x[2], reverse=True)
    jobs = [-1]*limit_time
    result = [-1]*limit_time
    max_profit = 0
    for i in range(len(T)):
        for j in range(T[i][1]-1, -1, -1):
            if result[j] == -1 and j < len(T):
                result[j] = 1
                jobs[j] = T[i][0]
                max_profit += T[i][2]
                break
    print(jobs)
    return max_profit

# (numer zadania, deadline, zysk)
def tasks(T):
    T.sort(key=lambda T: T[1])
    values = []
    for i in T:
        if i[1] not in values:
            values.append(i[1])
    profit = 0
    print(values)
    idx = 0
    for i in values:
        best = -1
        while idx < len(T) and T[idx][1] == i:
            if T[idx][2] > best:
                best = T[idx][2]
            idx += 1

        profit += best
    
    return profit
    




T = [(1,1,1), (2,3,1), (3,5,2), (4,6,2), (5,1,3), (6,2,4)]
print(tasks(T))
