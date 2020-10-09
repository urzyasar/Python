class Node:
       def __init__(self,value):
              self.data=value
              self.nextValue=None
class LinkedList:
       def __init__(self):
              self.head=None

       def appendElement(self,element):
#if head is none add the head element
              if(self.head==None):
                     self.head=element
              else:
                     current=self.head
                     while(current.nextValue!=None):
                            current=current.nextValue
                     current.nextValue=element
       def printElement(self):
              if self.head==None:
                     print("No Element in List")
              else:
                     current=self.head
                     print(current.data,end=" ")
                     while(current.nextValue!=None):
                            current=current.nextValue
                            print(current.data,end=" ")
              print()
       def count(self):
              if self.head==None:
                     print("count",0)
              else:
                     current=self.head
                     c=1
                     while(current.nextValue!=None):
                            current=current.nextValue
                            c+=1
              return c

       def positionElement(self,userposition):              
              if(userposition<=self.count()):
                     position=1
                     current=self.head
                     while(position!=userposition):
                            current=current.nextValue
                            position+=1

                     return current.data
              else:
                     return "Position exceeded"

       def deleteLast(self):
              current=self.head
              if current.nextValue==None:
                     current.data=None
                     return current.data
              else:
                     while(current.nextValue!=None):
                            prev=current
                            current=current.nextValue
                     prev.nextValue=None
                     return current.data

       def deleteFirst(self):
              current=self.head
              self.head=current.nextValue
              return current.data

       def insertAtPosition(self,uposition,newValue):
              newelement=Node(newValue)
              if uposition==1:
                     newelement.nextValue=self.head
                     self.head=newelement
              else:              
                     position=1
                     current=self.head
                     while(position!=uposition-1):                     
                            current=current.nextValue
                            position+=1
                     
                     newelement.nextValue=current.nextValue
                     current.nextValue=newelement
                     return newelement.data
              
       def deletefromPosition(self,uposition):
              position=1
              current=self.head
              if uposition==1:
                     temp=current
                     self.head=current.nextValue
              else:                     
            
                     while(position!=uposition-1):
                            position+=1
                            current=current.nextValue
                     temp=current.nextValue
                     current.nextValue=current.nextValue.nextValue
              return temp.data
       
       def deleteByValue(self,value):
              current=self.head
              if value==current.data:
                     self.head=current.nextValue
              else:                     
                     while(current.data!=value):
                            prev=current
                            current=current.nextValue
                     prev.nextValue=current.nextValue
              return value
                     
                            
       
              



obj1=Node(11)
obj2=Node(12)
obj3=Node(13)
obj4=Node(14)
obj5=Node(15)

#print(a)#prints the object address
print(obj1.data)


LL=LinkedList()

LL.appendElement(obj1)
LL.appendElement(obj2)
LL.appendElement(obj3)
LL.appendElement(obj4)
LL.appendElement(obj5)


#To print the LinkedList
LL.printElement()
#TO print the count
print("count :",LL.count())

#To print the PositionElement
print("Position Element {}:",LL.positionElement(4))
"""
#To delete the last Element
print("Last Element :",LL.deleteLast())
LL.printElement()

#To delete First Element
print("First Element :",LL.deleteFirst())
LL.printElement()
"""

print("insert at position :",LL.insertAtPosition(6,55))
LL.printElement()


#TO delete the element in the position
print("The deleted element :",LL.deletefromPosition(1))
LL.printElement()

#To delete by value
print("Deleted value :",LL.deleteByValue(55))
LL.printElement()

"""how the class attribute of one class accessed from other class"""

