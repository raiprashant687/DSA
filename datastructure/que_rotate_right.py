from collections import deque

def rotateright(l,k):
    d = deque()
    #i = len(l)-k
    for i in range(len(l)-k,len(l)):
        d.append(l[i])
    print(d)
    for m in range(k):
        d.append(l[m])
    return d







l=[1,2,3,4,5,6]
print(rotateright(l,3))
#answer would be [4,5,6,1,2,3]