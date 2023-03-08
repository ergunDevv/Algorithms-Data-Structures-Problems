def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)

    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRight(root,newBranch):
    t = root.pop(2)

    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root


def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0]=newVal

def getLeftChild(root):
    return root[1]
def setLeftChild(root,newVal):
    root[1] = newVal

def getRightChild(root):
    return root[2]
def setRightChild(root,newVal):
    root[2] = newVal


r = BinaryTree(1)
print("Binary Tree",r)
print(insertLeft(r,2))
print(insertLeft(r,3))
print(insertRight(r,4))
print(insertRight(r,5))
