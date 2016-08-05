class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False



    def preorder(self):
        if self.root is not None:
            print("PreOrder")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()


bst = Tree()
bst.insert(7)
bst.insert(4)
bst.insert(12)
bst.insert(2)
bst.insert(6)
bst.insert(9)
bst.insert(19)
bst.insert(3)
bst.insert(5)
bst.insert(8)
bst.insert(11)
bst.insert(15)
bst.insert(20)





bst.inorder()
#Inorder. The ordering is: the left subtree,the current node, the right subtree.
#Inorder traversal gives: 2, 3, 4, 5, 6, 7, 8 , 9, 11, 12, 15, 19, 20.

bst.preorder()
#Preorder. The ordering is: the current node, the left subtree, the right subtree
#Preorder traversal gives: 7, 4, 2, 3, 6, 5, 12, 9, 8, 11, 19, 15, 20.

bst.postorder()
#Postorder. The ordering is: the left subtree, the right subtree, the current node.
#Postorder traversal gives: 3,2, 5, 6, 4, 8, 11, 9, 15, 20,19, 12, 7.

