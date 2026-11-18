#Two sum prob 1
def twosum(target,nums):
    
    for i in range(len(nums)):
        j = i+1
        while(j<len(nums)):
            if(nums[i]+ nums[j] == target):
                return [i,j]
            j +=1
    print("No target in the array")

print(twosum(9,[2,7,11,15]))
