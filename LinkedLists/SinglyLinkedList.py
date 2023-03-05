class Node(object):
    def __init__(self,value):
        # Creating node for linked list that stores value and nextNode
        self.value=value
        self.nextNode=None

# Creating Nodes
a=Node(1)
b=Node(2)
c=Node(3)
# Linking nodes to each other.
a.nextNode=b
b.nextNode=c
print(a.nextNode.value)

