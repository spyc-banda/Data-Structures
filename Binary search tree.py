# 
# E-Mail           		: spycbanda@gmail.com
# Creation Date    		: 2018-04-05 15:06:46 
# Last modification		: 2018-04-05 
# by	            	: Ravi Garg
# This code is open source and free to use for all Python devotees.
#

class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#All operations on binary search tree are here
def delete(root, data):
	""" delete the node with the given data and return the root node of the tree """	    
	if root.data == data:
		# found the node we need to delete
		if root.right and root.left: 
			# get the successor node and its parent 
			[psucc, succ] = findMin(root.right, root)
			# splice out the successor
			# (we need the parent to do this) 
			if psucc.left == succ:
				psucc.left = succ.right
			else:
				psucc.right = succ.right					
			# reset the left and right children of the successor
			succ.left = root.left
			succ.right = root.right
			return succ                
		else:
			# "easier" case
			if root.left:
				return root.left  # promote the left subtree
			else:
				return root.right  # promote the right subtree 
	else:
		if root.data > data:  # data should be in the left subtree
			if root.left:
				root.left = delete(root.left, data)
			# else the data is not in the tree 
		else:  # data should be in the right subtree
			if root.right:
				root.right = delete(root.right, data)
	return root
		
def findMin(root, parent):
	""" return the minimum node in the current tree and its parent """
	if root.left:
		return findMin(root.left, root)
	else:
		return [parent, root]

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)

def maxValue(root):
    if not root.right:
        return root.data
    return maxValue(root.right)
    
def minValue(root):
    if not root.left:
        return root.data
    return minValue(root.left)
    
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right) 
    print(root.data,end=" ")

def preorder(root):
    if not root:
        return        
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)    

#=================MAIN PROGRAM======================
bstRoot = BSTNode(3)
insert(bstRoot, BSTNode(7))
insert(bstRoot, BSTNode(1))
insert(bstRoot, BSTNode(5))
insert(bstRoot, BSTNode(2))
insert(bstRoot, BSTNode(9))
inorder(bstRoot)
