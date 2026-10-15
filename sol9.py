n = int(input("Enter a number:"))
def isARMSTRONG(n):
    count =0
    save =n
    temp =0
    compare =n
    arm=0
    while(n>0):
        n = n//10
        count +=1
    while(save >0):
        temp = save % 10
        arm = arm +(temp **count)
        save =save //10
    if(arm ==compare):
        return True
    else:
        return False
    
    


    