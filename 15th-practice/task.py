class BinaryTree:
    def __init__(self, value=0, lchild=None, rchild=None, parent=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent

    def insert(self, value):
        if self.value == 0:
            self.value = value
        elif value > self.value:
            if self.rchild:
                self.rchild.insert(value)
            else:
                self.rchild = BinaryTree(value=value, parent=self)
        
        elif value < self.value:
            if self.lchild:
                self.lchild.insert(value)
            else:
                self.lchild = BinaryTree(value=value, parent=self)

    def printTree(self, ind=1):
        ind+=2
        if self.lchild:
            self.lchild.printTree(ind)
        print(" " * ind, self.value)
        if self.rchild:
            self.rchild.printTree(ind)

    def copyTree(self):
        copy = BinaryTree(self.value)
        if self.rchild:
            copy.rchild = self.rchild.copyTree()
        if self.lchild:
            copy.lchild = self.lchild.copyTree()
        return copy
    
    def searchNode(self, value):
        if value == self.value:
            return value
        elif self.lchild:
            buf = self.lchild.searchNode(value)
            if buf is not None:
                return buf
        elif self.rchild:
            buf = self.rchild.searchNode(value)
            if buf is not None:
                return buf
        return None
            
    def maxNode(self):
        if self is None:
            return self
        else:
            buf = self
            while(buf.rchild):
                buf = buf.rchild
            return buf.value
            
# Создание дерева
tree = BinaryTree(56)
tree.insert(23)
tree.insert(12)
tree.insert(78)
tree.insert(65)
tree.insert(-23)
tree.insert(89)
tree.insert(-12)
tree.printTree()

# Максимум
print("Max in tree: " + str(tree.maxNode()));

# Копирование дерева
CopyTree = tree.copyTree()
if(isinstance(CopyTree, BinaryTree)):
    print("Tree copied succesfully!!!")