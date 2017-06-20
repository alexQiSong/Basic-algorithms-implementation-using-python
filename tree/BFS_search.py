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
# Part II. Non-recursive implementation of BFS
#---------------------------------------------------------------
def BFSIter(BTree):
    queue = [BTree.node]
    while queue != []:
        currentNode = queue.pop(0)
        print currentNode.value
        if currentNode.left is not None:
            queue.append(currentNode.left)
        if currentNode.right is not None:
            queue.append(currentNode.right)
        
#----------------------------------------------------------------
# Part III. Test
#----------------------------------------------------------------
BTree = initializeBinaryTree()

print "#-------BFS iterative--------#"
BFSIter(BTree)
