#---------------------------------------------------------------
# Part I. Function and class for constructing a binary tree which
# looks like this:
#           a
#          / \
#         b   c
#        /   / \
#       d   e  f
#      / \
#     g   h
#        / \
#       i   j
#---------------------------------------------------------------

# A pointer points to the node of binary tree
class BinaryTreePointer:
    def __init__(self,node):
        self.node = node

# Class for the binary tree node
class BinaryTreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None

def initializeBinaryTree():
    NodeList = [["a",1,2,None],
                ["b",3,None,0],
                ["c",4,5,0],
                ["d",6,7,1],
                ["e",None,None,2],
                ["f",None,None,2],
                ["g",None,None,3],
                ["h",8,9,3],
                ["i",None,None,7],
                ["j",None,None,7]]

    # Initialize tree nodes
    BTreeNode = []
    for i in range(len(NodeList)):
        BTreeNode.append(BinaryTreeNode(NodeList[i][0]))

    # Point to the root node
    BTree = BinaryTreePointer(BTreeNode[0])

    # Link the parents and their children
    for i in range(len(NodeList)):
        if NodeList[i][1] is not None:
            BTreeNode[i].left = BTreeNode[NodeList[i][1]]
        else:
            BTreeNode[i].left = None

        if NodeList[i][2] is not None:
            BTreeNode[i].right = BTreeNode[NodeList[i][2]]
        else:
            BTreeNode[i].right = None

    return BTree

#---------------------------------------------------------------
# Part II. Recursive and Non-recursive implementation of DFS
#---------------------------------------------------------------

# Recursive version of DFS
def DFSRecursive(currentNode):
    print currentNode.node.value
    if currentNode.node.left is not None:
        DFSRecursive(BinaryTreePointer(currentNode.node.left))
    if currentNode.node.right is not None:
        DFSRecursive(BinaryTreePointer(currentNode.node.right))

# Non-recursive version of DFS
def DFSIter(BTree):
    print BTree.node
    stack = [BTree.node]
    while stack != []:
        currentNode = stack.pop()
        print currentNode.value
        if currentNode.left is not None:
            stack.append(currentNode.left)
        if currentNode.right is not None:
            stack.append(currentNode.right)
#----------------------------------------------------------------
# Part III. Test
#----------------------------------------------------------------
BTree = initializeBinaryTree()
print "#-------DFS recurisve--------#"
DFSRecursive(BTree)

print "#-------DFS iterative--------#"
DFSIter(BTree)