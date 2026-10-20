str = ["flowers" ,"flow" ,"fly" ,"flight"]

str.sort()


print(str)
str1 = str[0]
length =len(str)-1
str2 = str[length]

print(str1)
print(str2)
word =""
i=0
while(i <len(str1) and i <len(str2)):
    if(str1[i] == str2[i]):
        word = word +str1[i]
    i+=1
print(word)



    



    