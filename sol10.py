arr = ["apple" ,"banana" , "orange" , "cherry" ,"apple" ,"mango" , "mango" ,"mango"]
numbers = []
freq = {}
for item in arr:
    if(item in freq):
        freq[item] +=1
    else:
        freq[item] =1
print(freq)

