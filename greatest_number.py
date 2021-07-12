greatest = None
arr = [100, 3, 40, 7, 9, 11, 13]

for i in range(len(arr)):
    if(greatest is None or greatest < arr[i]):
        greatest = arr[i]

print(greatest)