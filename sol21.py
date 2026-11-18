#stack implementation using link list
class Node:
    def __init__(self , value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return  self.top is None

    def push(self,value):
        temp = Node(value)
        temp.next = self.top
        self.top = temp

    def pop(self):
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
        
    def print(self):
        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.next


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

    def dequeue(self):
        if(self.front):
            self.rear = None
        else:
            removed = self.front.data
            print(removed)
            self.front = self.front.next

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next

def reverse_stack(s1):
    q1=LQueue()
    while not s1.isempty():
        q1.enqueue(s1.pop())
    q1.print()








obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.print()
reverse_stack(obj)