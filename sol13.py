str ="987654321"
n = int(str)
listt =[]
temp = n
while(n > 0):
    if(n % 2 != 0):
        listt.append(n)
    n  = n//10

largest =0
for item in listt:
    if(item > largest):
        largest = item

print(largest)
