class Node:
    def __init__(self,a):
        self.data=a
        self.nextValue=None
class LinkedList:
    def __init__(self):
        self.head=None

    def appendElement(self,value):
        if(self.head==None):
            self.head=value
        else:
            current=self.head
            while(current.nextValue!=None):
                current=current.nextValue
            current.nextValue=value
    def list(self):
        l=[]
        current=self.head
        while(current!=None):
            l.append(current.data)
            current=current.nextValue
        return len(l)
    
    def positionValue(self,value):
        current=self.head
        position=1
        if(self.list()>=value):
            while(position!=value):
                position+=1
                current=current.nextValue
            return current.data    
        else:
            print("no")
        return -1



        
    def deleteValue(self,value):
        current=self.head
        prev=current
        while(current.data!=value):
            prev=current
            current=current.nextValue
        if(prev==current):

            self.head=current.nextValue
        else:
            prev.nextValue=current.nextValue
    def deleteFromposition(self,userposition):
        current=self.head
        position=1
        prev=current
        while(userposition!=position):
            position+=1
            #prev=current
            current=current.nextValue
        if(prev==current):
            self.head=current.nextValue
        else:
            prev.nextValue=current.nextValue
    def printElement(self):
        current=self.head
        l=[]
        while(current!=None):
            l.append(current.data)
            current=current.nextValue
        return l

    def Countlst(self):
        current=self.head
        count=0
        while(current!=None):
            count+=1
            current=current.nextValue
        return count

    def insertatposition(self,position,value):
        newElement=Node(value)
        if(position==1):
            newElement.nextValue=self.head
            self.head=newElement
        else:
            current=self.head
            for i in range(1,position-1):
                current=current.nextValue
            newElement.nextValue=current.nextValue
            current.nextValue=newElement
                

obj1=Node(1)
obj2=Node(2)
obj3=Node(3)
obj4=Node(4)
obj5=Node(5)
#obj1.nextValue=obj2
#obj2.nextValue=obj3
#obj3.nextValue=obj4
#obj4.nextValue=obj5
Llist=LinkedList()
#Llist.head=obj1
#Llist.deleteFromposition(3)
#Llist.printElement()
print(Llist.printElement())
Llist.appendElement(obj1)
Llist.appendElement(obj2)
Llist.appendElement(obj3)
Llist.appendElement(obj4)
Llist.appendElement(obj5)
"""print(Llist.list())
print(Llist.printElement())
print(Llist.positionValue(3))
print(Llist.printElement())
print(Llist.positionValue(6))"""
print(Llist.Countlst())
Llist.insertatposition(3,6)
print(Llist.printElement())
