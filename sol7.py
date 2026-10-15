arr = [1,2,3,4,5]
i=0
k=len(arr)-1
temp =arr
while(i<len(arr)):
    arr[i]= arr[k]
    k-=1
    i+=1
print(arr)

