count = 0
findString = "i"
some_string = "IFS Solusi Integrasi, PT"

# Best & Fastest method on python
# print(some_string.lower().count(findString)) 

# Basic Code
for i in range(len(some_string)):
    if(some_string[i].lower() == findString):
        count += 1
        
print(count)