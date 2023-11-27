from collections import deque

"""first we are adding the first n elements to the new list and then the remaining 
ones on the appending left the remaining ones"""
def rotateleft(l,k):
    d = deque()
    i =0
    for i in range(len(l)-k):
        d.append(l[i])
    print(d)
    i = i+1
    while i<(len(l)):
        d.appendleft(l[i])
        i = i+1
    return d






list1 = [1,2,3,4,5,6]
print(rotateleft(list1,4))
#ans should be [5,6,1,2,3,4]