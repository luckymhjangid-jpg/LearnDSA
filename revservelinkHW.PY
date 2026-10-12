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


    def reverse_linklist(self):
        curr = self.head
        prev = None
        next = None
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
            



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
obj.reverse_linklist()

obj.print_LL()  