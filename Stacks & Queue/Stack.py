#We have several ways to implement stacks in python and here we implement stack with lists, dqeue and LifoQueue
#implement with lists
mystack = []
mystack.append("A")
mystack.append("B")
mystack.append("C")
#as you know append adds element to end of the list
print(mystack.pop()) #C
print(mystack.pop()) #B
#as you can see C will pop and our principle is LIFO

#implement with deque library
from collections import deque
mystack1 = deque()
mystack1.append("A")
mystack1.append("B")
mystack1.append("C")

print(mystack1.pop()) #C
print(mystack1.pop()) #B

#implement with LifoQueue library
from queue import LifoQueue
mystack2 = LifoQueue()
mystack2.put("A")
mystack2.put("B")
mystack2.put("C")

print(mystack2.get()) #C
print(mystack2.get()) #B
