def ranges(X):
    count = 0
    A = []
    A.append((X[0],X[0]+1))
    j = 1
    for i in range(len(X)):

        while j < len(X) and X[j] <= A[i][1]:
            j += 1
        
        if j < len(X):
            A.append((X[j],X[j]+1))
        else:
            break
    
    return A

if __name__ == "__main__":
    # X = [0.25,0.5,1.6]
    X = [0.25,0.75,1.0,1.337,2.115,2.3,3.8,4.8]
    print(ranges(X))