# This here is where we discuss the tree data type. Very interesting.

# List of lists representation of of the tree data type

class BinaryTree:
    def __init__(self, rootbbj):
        self.key = rootbbj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newnode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newnode)

        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newnode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newnode)

        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __repr__(self):
        return f"<Binary Tree> root: {self.key}"


def binaryTree(r):
    return [r, [], []]


def insertLeft(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root


def insertRight(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newval):
    root[0] = newval


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def testBinaryTree():
    familyTree = binaryTree('Abbas')
    insertLeft(familyTree, 'Khadijah')
    insertLeft(familyTree, 'Noni')
    insertRight(familyTree, 'Hafsa')
    insertRight(familyTree, 'Angeles')
    print(familyTree)
    lBranch = getLeftChild(familyTree)
    print(lBranch)
    setRootVal(lBranch, 'Ruki')
    print(familyTree)
    insertLeft(lBranch, 'Ebi')
    print(familyTree)
    print(getRightChild(getRightChild(familyTree)))


def buildTree():
    tr = binaryTree('a')
    insertLeft(tr, 'b')
    insertRight(getLeftChild(tr), 'd')

    insertRight(tr, 'c')
    insertLeft(getRightChild(tr), 'e')
    insertRight(getRightChild(tr), 'f')

    return tr


def buildClassyTree():
    classyTree = BinaryTree('a')

    classyTree.insertLeft('b')
    classyTree.insertRight('c')

    classyTree.getLeftChild().insertRight('d')

    classyTree.getRightChild().insertRight('f')
    classyTree.getRightChild().insertLeft('e')
    return classyTree


if __name__ == '__main__':
    d = buildClassyTree()
    print(d)
