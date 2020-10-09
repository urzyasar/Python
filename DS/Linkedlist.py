class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
nodeA=Node(1)
nodeB=Node(2)
nodeC=Node(3)


nodeA.next=nodeB
nodeB.next=nodeC

print(nodeA.data)
print(nodeB.data)
print(nodeC.data)

def countNodes(nodeA):
    count=1
    current=nodeA
    while(current.next is not None):
        current=current.next
        count+=1
    return count
print(countNodes(nodeA))

def AddNodes(a):
    return Node(a)
print(AddNodes(5).data)


def PrintNodes(head):
    #current=head
    while(head is not None):
        print(head.data,end="-")
        head=head.next
        
        
PrintNodes(nodeA)

        
