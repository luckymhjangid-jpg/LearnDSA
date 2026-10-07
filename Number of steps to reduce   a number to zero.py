
def numberofsteps(num:int)->int:

    count=0
    while(num != 0):
        count=count+1
        if(num % 2 == 0):
            num = num /2
        else:
            num = num-1
    return count

num=14
result =numberofsteps(num)
print(result)