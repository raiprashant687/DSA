list1 = [1,9,3,2,7,4,8]

for i in range(len(list1)):
    for j in range((i+1),len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)