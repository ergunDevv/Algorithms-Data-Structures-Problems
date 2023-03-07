# PROBLEM: Given a singly linked list, write a function which 
# takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point acutally points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.

class Node(object):
    def __init__(self,value) :
        self.value=value
        self.nextnode=None

def cycle_check(node):
    marker1=node
    marker2=node

    while marker2 != None and marker2.nextnode != None :
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode
        if marker2 == marker1:
            return True
        
    return False


a = Node(1)
b = Node(2)
c= Node(3)

a.nextnode=b
b.nextnode=c
c.nextnode=a

x = Node(5)
y= Node (6)
z= Node (7)
x.nextnode=y
y.nextnode=z
print(cycle_check(a))
print(cycle_check(x))

