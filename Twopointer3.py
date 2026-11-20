listt = [1,1,2,3,3]
low = 0
high =1

while(high <len(listt)):
    if(listt[high] == listt[high-1]):
        high +=1
        continue
    else:
        listt[low+1] = listt[high]
        low +=1
        high +=1

print(listt[:low+1])
