list1 = [2,9,6,4,7,1]

for i in range(1,len(list1)):
    current = list1[i]
    j = i-1
    while list1[j]>current and j >= 0:
        temp = list1[j+1]
        list1[j+1]=list1[j]
        list1[j]= temp
        j = j-1


print(list1)
