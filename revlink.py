class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next


class SinglyLinkList:
    def __init__(self,head=None):
        self.head = head

    def  insertATEnd(self,value):
        temp = Node(value)
        if(self.head !=None):
            t1=self.head
            while(t1.next !=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
    
    def del_node(self,value):
        temp=self.head
        prev=None
        if(temp.data ==value):
            self.head = self.head.next
            return
        while(temp != None):
            if(temp.data == value):
                break
            else:
                prev=temp
                temp=temp.next
            if temp.next == None:
                print("Value is not present in the list")
            prev.next = temp.next
            temp=None
    def reverse(self):
        curr=self.head
        prev=None
        while(curr !=None):
            nextnode = curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
    def printLL(self):
        t1= self.head
        while(t1.next !=None):
            print(t1.data , end="<-->")
            t1=t1.next
        print(t1.data)


obj =SinglyLinkList()
obj.insertATEnd(10)
obj.insertATEnd(20)
obj.insertATEnd(30)
obj.del_node(10)
obj.del_node(5)

obj.printLL()