# Problem: Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list.

# FIRST SOLUTION

# Defining Node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    current = head
    # In this solution finding how long our linked list and subtracting the nth last node from length of linked list
    # than finding the nth node from start.

    # Finding the length of linked array
    numberOfNodes = 0
    while current:
        numberOfNodes += 1
        current = current.nextnode
    fromStartNode = numberOfNodes-n
    numberOfNodes = 0
    current = head
    # Finding the nth node from start
    while numberOfNodes < fromStartNode:
        numberOfNodes += 1
        current = current.nextnode
    # Returning the nth node's value
    return current.value

# SECOND SOLUTION


def nth_to_last_node2(n, head):
    # In this solution defining 2 pointers
    left_pointer = head
    right_pointer = head
    # And defining right_pointer to nth node from start
    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')
        right_pointer = right_pointer.nextnode
    # Than adding left and right pointer until right_pointer.nextnode doesn't exist
    # Because of defined right_pointer the nth node and adding 1 to left and right pointers left pointer is the nth node from end
    while right_pointer.nextnode:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode
    return left_pointer.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d
print(nth_to_last_node(1, a))
print(nth_to_last_node2(1, a))
