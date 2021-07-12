arr = ['a', 'c', 'b', 'z', 'x']

# Fastest code on python
# arr.sort()

# sorting using bubble sort method
def bubbleSort(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                
    return mylist


print(bubbleSort(arr))