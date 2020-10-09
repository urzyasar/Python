class Node:
       def __init__(self,val):
              self.data=val
              self.address=None
class LinkedList:
       def __init__(self):
              self.head=None
     
 #obj1         obj2        obj3
#[11,obj2] --> [12,obj3]--> [13,new]-->[14,None]
#^head
              # 1               2         3            4            5
#[10,None] to [10,obj1]-->[11,new] --> [33,obj2]-->  [12,obj3]--> [13,new]-->[14,None]
              #^head       #^head  
              
       def appendElement(self,obj):
              if self.head==None:#
                     self.head=obj
                     
              else:
                     current=self.head#obj1
                    #print(current.data,end=" ")#11
                     while(current.address!=None):
                            current=current.address#obj2
                            #print(current.data,end=" ")
                     current.address=obj
       def printElement(self):
              if self.head==None:
                     print("There is no element")
              else:
                     current=self.head
                     print(current.data,end=" ")
                     while(current.address!=None):#when == None Break the loop
                            current=current.address#obj2,obj3
                            print(current.data,end=" ")
                     print()
       def insertAtLast(self,value):
              new=Node(value)
              current=self.head
              while current.address!=None:
                     current=current.address
              current.address=new
       def insertAtFirst(self,value):
              new=Node(value)              
              new.address=self.head
              self.head=new
              """
       def insertAtposition(self,pos,value):
              new=Node(value)
              current=self.head#obj1
              index=1
              while(index!=pos-1):
                     current=current.address #obj2
                     current1=current.address
                     index=index+1
              current.address=new
              new.address=current1
              """
       def insertAtposition(self,pos,value):
              new=Node(value)
              current=self.head#obj1
              index=1
              while(index!=pos-1):
                     current=current.address #obj2
                     current1=current.address
                     index=index+1
              new.address=current.address
              current.address=new
             

                     
              
              
              
             
                     
              



obj1=Node(11)
#print(obj1)
#print(obj1.data)
#print(obj1.address)
#obj1-->data-add
#obj2-->data-add
obj2=Node(12)
obj3=Node(13)
#creating a object for LinkedList Object
LL1=LinkedList()
LL1.appendElement(obj1)
LL1.appendElement(obj2)
LL1.appendElement(obj3)
LL1.printElement()
print("insert at last postion")
LL1.insertAtLast(14)
LL1.printElement()
print("insert at First position")
LL1.insertAtFirst(10)
LL1.printElement()
print("insert at User position")
LL1.insertAtposition(3,33)
LL1.printElement()
