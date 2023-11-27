""" => quick sort works on the Divide and conquer rule i.e divide the problems into further
=> chooses pivot element
=> takes two pointer one points to next of pivot and one at the last of the list
=> first moves rhs searching for element greter than pivot = a
=> second moves lhs searching for element less that pivot = b
=> start by moving a and if a is greater than pivot stop, otherwise move forward
=> start by moving b lhs and if  less than pivot then stop , otherwise move leftwards.
=> if a and b not crossed each other then swap a and b and if crossed then swap b with pivot.
=>
"""
list1 = [5,8,1,2,6,3,9]

def part(list1,low,high):
    pivot = list1[low]
    i = low+1
    j = high
    while 1:
        while list1[i]<= pivot and i <= j:
            i = i+1
        while list1[j]>=pivot and i <=j:
            j = j-1
        if i <= j:
            list1[j],list1[i]= list1[i],list1[j]
        else:
            break
    list1[low],list1[j]=list1[j],list1[low]
    return j




def quicksort(list1,low,high):
    if low < high:
        piv= part(list1,low,high)
        quicksort(list1,low,piv-1)
        quicksort(list1,piv+1,high)




quicksort(list1,0,6)


print(list1)