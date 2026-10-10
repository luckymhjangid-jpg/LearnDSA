class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLinkList:
    def __init__(self,head=None):
        self.head = head

    def insertATEnd(self,value):
        temp = Node(value)
        
        if(self.head != None):
            t1=self.head
            while(t1.next!= None):
                t1=t1.next
            t1.next=temp
                

        else:
            self.head = temp

    def middle_node(self):
        temp = self.head
        t1 = self.head
        count=1
        while(temp != None):
            count+=1
            temp=temp.next

        if(count % 2 == 0):
            count = count//2
        else:
            count = (count//2) +1
        countsearch=1
        while(t1 !=None):
            if countsearch == count:
                print(t1.data)
                return
            countsearch +=1
            t1=t1.next    
            

                

    def print_LL(self):
        temp=self.head
        
        if(self.head == None):
           print("Link List is empty")
        else:
            while(temp != None):
                print(temp.data ,end="<-->")
                temp=temp.next

   
            
        



            


obj = SinglyLinkList();
obj.insertATEnd(30)
obj.insertATEnd(40)
obj.insertATEnd(50)
obj.insertATEnd(80)

obj.middle_node()

obj.print_LL()  