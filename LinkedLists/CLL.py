#  /-->[value|link] --> [value|link]--\
# |                                    |
#  \--[value|link] --> [value|link]<--/
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class CircularLinkedList:  
   def __init__(self):
      self.head = None
   def AddValue(self, value):
      pointer = Node(value)
      temp = self.head    
      pointer.next = self.head

      if self.head is not None:
         while(temp.next != self.head):
            temp = temp.next
         temp.next = pointer
      else:
         pointer.next = pointer
      self.head = pointer

   def print_it(self):
      temp = self.head
      if self.head is not None:
         while(True):
            print(temp.value)
            temp = temp.next
            if (temp == self.head):
               break
CLL = CircularLinkedList()
print("Elements are added to the list ")
CLL.AddValue (1000)
CLL.AddValue (500)
CLL.AddValue (250)
print("The value is : ")
CLL.print_it()