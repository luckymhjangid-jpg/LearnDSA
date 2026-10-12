class Node:
    def __init__(self,info,pos=None,next=None):
        self.data = info
        self.next = next
        self.pos = pos

class SinglyLinkList:
    def __init__(self,head=None):
        self.head = head
        

    
    def insert_at_pos(self, value, pos):
        if pos < 0:
            print("Invalid position!")
            return
 
        if pos == 0:
            temp = Node(value, next=self.head)
            self.head = temp
            return

        curr = self.head
        index = 0
        while curr != None and index < pos - 1:
            curr = curr.next
            index += 1
 
        if curr == None:
            print("Position out of range!")
            return
 
        temp = Node(value)
        temp.next = curr.next
        curr.next = temp
            
            

    


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

obj.print_LL()        