arr = [2, 3, 5, 7, 9, 11, 13]
count = 0

def countPrime(num):
    if num==1 or num==0 or (num % 2 == 0 and num > 2):
        return 0
    else:
        for i in range(3, int(num**(1/2))+1, 2):
            if num%i == 0:
                return 0
        return 1
    
for i in range(len(arr)):
    count += countPrime(arr[i])

print(count)