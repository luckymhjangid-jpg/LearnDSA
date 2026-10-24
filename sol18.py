class Node:
    def __init__(self , value):
        self.data = value
        self .next = None

class LQueue:
    def __init__(self):
        self.front  = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)
        if(self.rear):
            self.rear.next =new_node
            self.rear =new_node
        else:
            self.front = self.rear = new_node

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        
obj = LQueue()
obj.enqueue(56)
obj.enqueue(71)
obj.enqueue(21)
obj.enqueue(33)
obj.print()
