# 
# E-Mail           		: spycbanda@gmail.com 
# Creation Date    		: 2018-04-01 06:15:46 
# Last modification		: 2018-04-03 
# by		              : Ravi Garg
# This code is open source and free to use for all Python devotees.
#

# Node of a Singly Linked List
class Node:
    # method to initialize an empty node
    def __init__(self, data):
        self.data = data
        self.next = None
        
    # method for setting the data field of the node    
    def set_data(self, data):
        self.data = data
        
    # method for getting the data field of the node   
    def get_data(self):
        return self.data
        
    # method for setting the next field of the node
    def set_next(self, next):
        self.next = next

    # method for getting the next field of the node    
    def get_next(self):
        return self.next
        
    # returns true if the node points to another node
    def has_next(self):
            return self.next != None

# Class for defining a Singly Linked List   
class SingleLL(object):
    # initializing a list as empty
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
         
    # method to add a node in the linked list
    def add(self, node):
        if self.length == 0:
            self.insert(node)
        else:
            self.append(node)
    
    # method to add a node after the node having the data=data. 
    def addAfterValue(self, node, data):
        newNode = node
        currentnode = self.head
        
        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                newNode.next = currentnode.next
                currentnode.next = newNode
                self.length = self.length + 1
                if newNode.next == None:
                  self.tail = newNode
                return
            else:
                currentnode = currentnode.next
                 
        print("The data provided is not present")
                 
    # method to add a node at a particular position. Position starts with 1.
    def addAtPos(self, node, pos = 1):
        count = 0
        currentnode = self.head
        previousnode = self.head
        
        if pos > self.length or pos <= 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    if node.next == None:
                      self.tail = node
                    return
                     
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next
         
         
                 
    # method to add a node at the end of a list
    def append(self, node):
        currentnode = self.tail
 
        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.tail = newNode
        self.length = self.length + 1
              
    # method to delete the first node of the linked list
    def delete(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
              self.tail = None
              
    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
        
        if self.length == 0:
            self.head = None
            self.tail = None
            print("The list is empty")
        elif pos > self.length or pos <= 0:
            print("The position does not exist. Please enter a valid position")
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.delete()
            self.length -= 1
        else:        
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    if previousnode.next == None:
                        self.tail = previousnode
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next
                    
    # method to delete a node having the given data
    def deleteValue(self, data):
        if self.length == 0:
            self.head = None
            self.tail = None
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
             
            while currentnode.next != None or currentnode.data != data:
                if currentnode.data == data:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    if previousnode.next == None:
                        self.tail = previousnode
                    return
                        
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next
                     
            print("The data provided is not present")
    
    # returns node at any position
    def getAtPos(self, pos):
        count = 0
        currentnode = self.head
         
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next

    # returns the first element of the list
    def getFirst(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data
     
    # returns the last element of the list
    def getLast(self):
         
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.tail
                 
            return currentnode.data
     
    # returns the length of the list        
    def getLength(self):
        return self.length
        
    # method to insert a node at the beginning of the list  
    def insert(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        if self.length == 1:
          self.tail = self.head
        else:
          self.tail = self.tail.next
         
     
    # method to delete the last node of the linked list
    def pop(self):
        if self.length == 0:
            self.head = None
            self.tail = None
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
             
            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next
                 
            previousnode.next = None
            self.tail = previousnode 
            self.length -= 1
             
    # method to print the whole list
    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print(nodeList)  

# Main Program
if __name__ == "__main__":
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(5)
	ll = SingleLL()
	ll.add(node1)
	ll.add(node2)
	ll.add(node3)
	ll.add(node4)
	ll.add(node5)
	ll.print_list()
