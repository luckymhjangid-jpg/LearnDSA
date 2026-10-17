arr = [1,2,4,2,5,7,9,9,9]
numbers = []
freq = {}
for item in arr:
    if(item in freq):
        freq[item] +=1
    else:
        freq[item] = 1
print(freq)

max_count = 0 
smallest = 0 
for item , count in freq.items():
    if(count > max_count):
        max_count = count
        smallest = item
    elif(count == max_count):
        if(item < smallest):
            smallest = item

print(smallest)
        
    

        



