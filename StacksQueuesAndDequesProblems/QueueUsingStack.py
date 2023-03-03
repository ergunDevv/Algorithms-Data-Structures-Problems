# PROBLEM : Given the Stack class below, implement a queue class using two stacks! 
# Note, this is a "classic" interview problem. Use a Python list data structure as your Stack

class Queue2Stacks(object):

    def __init__(self) :
        self.inStack=[]
        self.outStack=[]
    def enqueue(self,element):
        self.inStack.append(element)


    def dequeue(self):

        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        self.outStack.pop()
        return self.outStack


a = Queue2Stacks()
a.enqueue(1)
a.enqueue(2)
print(a.enqueue(3))
print(a.dequeue())
