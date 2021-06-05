def spr(B):
    q=True
    for i in B:
        if i==0:
            q=False
            break
    return q

def zad7(A,k):
    B=[0]*k
    x=0
    y=10
    j=0
    i=0
    ilosc_zer = k
    while i<len(A):
        if ilosc_zer == 0:
            if i-j-1<y-x:
                x=j
                y=i-1
            if B[A[j]] != 0:
                B[A[j]]-=1
                ilosc_zer += 1
            j+=1
        else:
            if B[A[i]] == 0:
                B[A[i]]+=1
                ilosc_zer -= 1
            i+=1
    print(x,y)

A=[0,0,1,1,2,2,0,0,2,1,1,2,1,1]
zad7(A,3)