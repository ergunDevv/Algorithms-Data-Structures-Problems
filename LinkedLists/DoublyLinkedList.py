class DoublyLinkedListNode(object):
    def __init__(self,value) :
        # Creating Doubly Linked List Node Object
        self.value = value
        self.prev_node=None
        self.next_node=None
# Creating Doubly Linked List Node
a=DoublyLinkedListNode(1)
b=DoublyLinkedListNode(2)
c=DoublyLinkedListNode(3)

# Defining the links between nodes.
a.next_node=b
b.prev_node=a
b.next_node=c
c.prev_node=b
print(c.prev_node.value)
print(b.prev_node.value)

