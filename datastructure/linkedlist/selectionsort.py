list1 = [6,8,3,5,1,4]
#swap i=0 with j =4
# i = 0
# j = 4
#
# temp = list1[i]
# list1[i] = list1[j]
# list1[j] = temp
# print(list1)
#list1 = [6,8,3,5,1,4]

for i in range(len(list1)):
    pos = i
    for j in range(i,len(list1)):
        if list1[j] < list1[pos]:
            pos = j
    temp = list1[pos]
    list1[pos] = list1[i]
    list1[i]= temp
print(list1)