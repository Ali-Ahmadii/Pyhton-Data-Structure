#now we implement queues in several ways
#FIFO Principle
#implement with lists
Queue0 = []
Queue0.append('A')
Queue0.append('B')
Queue0.append('C')

print(Queue0.pop(0))
print(Queue0.pop(0))
print(Queue0.pop(0))

#Implementation using collections.deque
from collections import deque
Queue1 = deque()
Queue1.append('A')
Queue1.append('B')
Queue1.append('C')

print(Queue1.popleft())
print(Queue1.popleft())
print(Queue1.popleft())

#Implementation using queue.Queue
from queue import Queue
Queue2 = Queue()
Queue2.put('A')
Queue2.put('B')
Queue2.put('C')

print(Queue2.get())
print(Queue2.get())
print(Queue2.get())