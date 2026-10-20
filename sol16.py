class Node:
    def __init__(self , data , next =None , prev=None):
        self.data = data
        self.next =next
        self.prev = prev

class SinglyLinkList():
    def __init__(self , head =None):
        self.head = head

    def insertATend(self,value):
        temp = Node(value)
        t1 =self.head
        if(self.head ==None):
            self.head = temp
        else:
            while(t1.next != None):
                t1 =t1.next
            t1.next = temp

    def insetATbegin(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head =temp
        else:
            temp.next = self.head
            self.head = temp

    def deleteAtSpecific(self,x):
        temp = Node(x)
        t1= self.head
        prev = None
        if(self.head == None):
            print("No Node in the link list")
        if(self.head == temp):
            self.head = self.head.next
        else:
            while(t1.data !=temp.data):
                prev = t1
                t1 =t1.next
            prev.next = t1.next
            

    def insertAtSpecificpos(self,pos,value):
        count =1
        temp = Node(value)
        t1=self.head
        if(pos == 1):
           temp.next=self.head
           self.head =temp
        while(t1 !=None and count < pos -1):
            t1=t1.next
            count +=1

        if(t1 == None):
            print("Position out of range")
            return
        temp.next = t1.next
        t1.next =temp
           
       

               
           
           
           
                
            
        
            

    def printSinglyLinkList(self):
        
        temp= self.head
        if(self.head ==None):
            print("The link list is empty")
        else:
            while temp != None:
                print(temp.data, end="<-->")
                temp = temp.next


                
            

obj = SinglyLinkList()
obj.insetATbegin(45)
obj.insertATend(30)
obj.insertATend(70)
obj.insertATend(90)
obj.deleteAtSpecific(30)
obj.deleteAtSpecific(70)
obj.printSinglyLinkList()



        
        