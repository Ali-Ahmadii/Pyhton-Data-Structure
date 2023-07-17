#[link|value|link]<--[link|value|link] --> [link|value|link] link points to the specific linked list
#head refers to first variable and tail refers to last variable
class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None 
    self.prev = None 
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def InsertToEmptyList(self, value):
        if self.head is None:
            incomingNode = Node(value)
            self.head = incomingNode
        else:
            print("The list is empty")
    def InsertToEnd(self, value):
        # Check if the list is empty
        if self.head is None:
            incomingNode = Node(value)
            self.head = incomingNode
            return
        n = self.head
        while n.next is not None:
            n = n.next
        incomingNode = Node(value)
        n.next = incomingNode
        incomingNode.prev = n
    def DeleteAtStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None;
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.next
        
DLL = DoubleLinkedList()
DLL.InsertToEmptyList(100)
DLL.InsertToEnd(50)
DLL.InsertToEnd(123123)
DLL.InsertToEnd(123123123)
DLL.Display()
print()
DLL.DeleteAtStart()
DLL.Display()

