st1 = "cluster"
st2 = "clue"
str3 =["flowers" ,"flow" ,"fly" ,"flight"]
count1 =1
freq = {}
listt1 =[]
listt2 = []


print(s)

for i in range(len(st1)):
    listt1.append(st1[:count1])
    count1 +=1


count2 =1
for i in range(len(st2)):
    listt2.append(st2[:count2])
    count2 +=1

ans = ""

for item in listt1:
    if item in listt2:
        if(item >ans):
            ans = item
print(ans)



