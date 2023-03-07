# PROBLEM: Write a function to reverse a Linked List in place. 
# The function will take in the head of the list as input and return the new head of the list.



# Defining Node
class Node(object):
        def __init__(self,value) :
           self.value=value
           self.nextnode=None

def reverse (head):
        # Defining previous, current, next for changing the order of linked list
        previous=None
        current=head
        next=None
        # Creating while loop until last element of linked list.
        while current:
            #  Saving current.nextnode to next
              next =current.nextnode
            #  Than changing current.nextnode to previous this way making linked list reversal.
              current.nextnode=previous
            # And passing to other element with changing previous to current node and current node to next node
              previous=current
              current=next
        return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d
print(reverse(a))
print(a.nextnode)
print(b.nextnode.value)
