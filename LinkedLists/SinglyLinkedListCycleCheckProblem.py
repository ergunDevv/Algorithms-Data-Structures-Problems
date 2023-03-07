# PROBLEM: Given a singly linked list, write a function which 
# takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point acutally points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.

# Creating node for linked list.
class Node(object):
    def __init__(self,value) :
        self.value=value
        self.nextnode=None


def cycle_check(node):
    # Creating 2 markers for solution and idea of the solution is like 2 runners running in the circle but marker 2 is runs faster.
    # If marker2 catches the marker 1 linked list is cycle linked list if cannot it is not cycle linked list.
    # Creating nodes
    marker1=node
    marker2=node
    # If marker 2 or marker2.nextnode equal to none returning false cause linked list is not cycle
    while marker2 != None and marker2.nextnode != None :
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode
        # Checking marker 2 equal to marker 1 if it is linked list is cycle linked list cause marker2 is much faster than marker1
        #  and marker 2 not equal to None so it must be cycle
        if marker2 == marker1:
            return True
        
    return False

# Case 1 
a = Node(1)
b = Node(2)
c= Node(3)

a.nextnode=b
b.nextnode=c
c.nextnode=a
# Case 2 
x = Node(5)
y= Node (6)
z= Node (7)
x.nextnode=y
y.nextnode=z
# Printing results.
print(cycle_check(a))
print(cycle_check(x))

