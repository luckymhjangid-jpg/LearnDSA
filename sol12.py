arr = [1,4,6,9,7,5]

max_count = 0
secndmax = 0
for i in range(len(arr)):
    if(arr[i] > max_count):
        secndmax = max_count
        max_count = arr[i]
    elif(arr[i] > secndmax and secndmax !=max_count):
        secndmax = arr[i]
 
print(max_count)
print(secndmax)