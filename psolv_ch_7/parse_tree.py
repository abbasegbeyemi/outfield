from psolv_ch_7.tree_ADT import BinaryTree
from psolv_ch_4.psolv_ch_4_ADT import Stack
import operator

recognised_operators = '+-*/'


def buildParseTree(expression):
    expression_list = expression.split()
    parents_stack = Stack()
    expression_tree = BinaryTree('')
    parents_stack.push(expression_tree)
    current_tree = expression_tree

    for i in expression_list:
        if i == '(':
            current_tree.insertLeft('')
            parents_stack.push(current_tree)
            current_tree = current_tree.getLeftChild()

        elif i in recognised_operators:
            current_tree.setRootVal(i)
            current_tree.insertRight('')
            parents_stack.push(current_tree)
            current_tree = current_tree.getRightChild()

        elif i == ')':
            current_tree = parents_stack.pop()

        elif i not in recognised_operators + ')':
            try:
                current_tree.setRootVal(int(i))
                parent = parents_stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError(f"Token {i} is not valid in this case you dummy.")

    return expression_tree


pt = buildParseTree("( ( 10 + 5 ) * 3 )")

opers = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}


def evaluate(parsetree: BinaryTree) -> int:
    leftC = parsetree.getLeftChild()
    rightC = parsetree.getRightChild()

    if leftC and rightC:
        fn = opers[parsetree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))

    else:
        return parsetree.getRootVal()


# Here we start looking at tree traversals. Preorder, Postorder, Inorder
# Preorder; Visit: Node, Left, Right
# Inorder; Visit: Left, Node, Right
# Postorder; Visit: Left, Right, Node
def preorder(tree: BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def inorderprinted(tree: BinaryTree):
    expression = ""
    if tree:
        lc = inorderprinted(tree.getLeftChild())
        rc = inorderprinted(tree.getRightChild())
        op = tree.getRootVal()
        if lc and rc:
            expression = f"({lc} {op} {rc})"

        else:
            expression = f"{op}"
    return expression


# preorder(pt)
# postorder(pt)
# inorder(pt)
print(inorderprinted(pt))


# We could also rewrite the evaluation of the parse tree to follow more closely with postorder
def postordereval(tree: BinaryTree) -> int:
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())

        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)

        else:
            return tree.getRootVal()


print(postordereval(pt))
