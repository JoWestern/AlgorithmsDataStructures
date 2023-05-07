class Stack:
    def __init__(self):
        self.items = []

    #check if the list is empty
    def is_empty(self):
        return len(self.items) == 0

    #add an element at the end of the list 
    def push(self, item):
        self.items.append(item)

    #remove the first element in the list
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    #looks at the last element in the list
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]
    
    #remove the first element in the list
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.pop(0)

    #looks at the first element in the list
    def front(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self.items[0]

    #returns the size of the list
    def size(self):
        return len(self.items)

stack = Stack()
for i in range(20):
    stack.push(i)

print(stack.peek())
print(stack.front())
stack.dequeue()
stack.pop()
print(stack.peek())
print(stack.front())

