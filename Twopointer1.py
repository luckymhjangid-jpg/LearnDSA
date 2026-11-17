def twoSum(numbers,target):
    i=0
    j=len(numbers)-1
    while(i<j):
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i+1 , j+1]
        elif sum > target:
            j -=1
        elif sum < target:
            i +=1
    return -1

print(twoSum([2,7,11,15],9))
