#[value|link] --> [value|link] link points to the specific linked list
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,value) :
        incomingNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = incomingNode
        else :
            self.head = incomingNode
    def printMyList(self):
        currentNode = self.head
        while(currentNode.next):
            print(currentNode.value)
            currentNode = currentNode.next
        print(currentNode.value)
            
    
class Node :
    def __init__(self ,value = None , next = None):
        self.value = value
        self.next = next

LL = LinkedList()
LL.insert(300)
LL.insert(200)
LL.insert(400)
LL.printMyList()