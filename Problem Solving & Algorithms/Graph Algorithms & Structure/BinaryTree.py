#we need root node
#parent node
#child node
#edge
#leaf node
#internal node
#these were part of a tree
from collections import deque


class BinaryTreeNode :
    def __init__(self ,value):
        self.value =  value
        self.leftChild = None
        self.rightChild = None
    def insert(self, value):
        if value < self.value:
            if self.leftChild is None:
                self.leftChild = BinaryTreeNode(value)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = BinaryTreeNode(value)
            else:
                self.rightChild.insert(value)
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print( self.value),
        if self.rightChild:
            self.rightChild.PrintTree()
    
    def dfs_traversal(self, order='in-order'):
        if order == 'in-order':
            if self.leftChild:
                self.leftChild.dfs_traversal()
            print(self.value, end=' ')
            if self.rightChild:
                self.rightChild.dfs_traversal()
        elif order == 'pre-order':
            print(self.value, end=' ')
            if self.leftChild:
                self.leftChild.dfs_traversal()
            if self.rightChild:
                self.rightChild.dfs_traversal()
        elif order == 'post-order':
            if self.leftChild:
                self.leftChild.dfs_traversal()
            if self.rightChild:
                self.rightChild.dfs_traversal()
            print(self.value, end=' ')
            
    def bfs_traversal(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            print(node.value, end=' ')

            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
                
                
node1 = BinaryTreeNode(100) #creating an object with calling that class with its constructor
node2 = BinaryTreeNode(50)
node3 = BinaryTreeNode(75)
node4 = BinaryTreeNode(12)
node5 = BinaryTreeNode(121)
node6 = BinaryTreeNode(1000)
node7 = BinaryTreeNode(45)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7
                    
                       

print(node1.value)#100 (root node)
print("right Child Of Node 3 Is : "+str(node3.rightChild.value)) #right Child Of Node 3 Is : 45
node1.PrintTree() ## left -> root -> right
node1.dfs_traversal()
print()
node1.dfs_traversal('pre-order') #12 50 121 100 1000 75 45
print() #100 12 50 121 1000 75 45
node1.dfs_traversal('post-order') #12 50 121 1000 75 45 100
print()
node1.bfs_traversal() #100 50 75 12 121 1000 4