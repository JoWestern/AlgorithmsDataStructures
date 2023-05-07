class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, newdata):
        newnode = Node(newdata)
        #make this nodes next value point to the current head
        newnode.next = self.head
        #make this node the head
        self.head = newnode  

    def insertEnd(self, newdata):
        newnode = Node(newdata)
        #if there is no node in the list, insert this
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        #loop to find the last element in the list
        while(last.next):
            last = last.next
        #insert this node at the end
        last.next = newnode

    def remove(self, remove):
      head = self.head
         
      if (head is not None):
         if (head.data == remove):
            self.head = head.next
            head = None
            return
      while (head is not None):
         if head.data == remove:
            break
         prev = head
         head = head.next

      if (head == None):
         return

      prev.next = head.next
      head = None
        
    def print(self):
      printval = self.head
      #loop through and print each element
      while printval is not None:
         print (printval.data)
         printval = printval.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

llist = LinkedList()
first_node = Node(0)
prevnode = Node(1)
llist.head = first_node
first_node.next = prevnode

for i in range(2, 10):
    newnode = Node(i)
    prevnode.next = newnode
    prevnode = newnode

llist.insertEnd(50)
llist.insertBeginning(100)
llist.remove(50)

llist.print()
