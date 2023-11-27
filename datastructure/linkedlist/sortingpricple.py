list1 = [6,8,3,5,1,4]

for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j]= list1[j],list1[i]
print(list1)
#1,3,4,5,6,8

#after 3rd iteration the list would be 8,6,5,3,1,4 and i = 4
#list1 = [6,8,3,5,1,4]
# a = 0
# b = a+1
