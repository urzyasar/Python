#Linked List
"""
1.Create a List box  ( data,address)
2.Add elements to List Box

       [1,null]-->[2,null] --> [3,null] 

3.Create a Linked List
4.Forming a chain
       head-->Pointing to [1,null]


"""
class Node:
       def __init__(self,a): #initialized during obj creation
              self.data=a
              self.nextValue=None  
class LinkedList:
       def __init__(self):
              self.head=None
       def appendElement(self,element):
              self.head=element                 
       
obj1=Node(1)  #object created and value passed
print(obj1)
obj2=Node(2)
#print(obj2)
obj3=Node(3)
#print(obj3)
"""
obj1.nextValue=obj2
print(obj1.nextValue)
obj2.nextValue=obj3

print(obj2.nextValue)
"""
Llist=LinkedList()
print(Llist)
Llist.appendElement(obj1)
print(Llist.head)
print(Llist.head.data)
print(Llist.head.nextValue)

