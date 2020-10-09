#creating a Node Here 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class SLL:
 def __init__(self):
        self.head=None
        self.tail=None
        
        

#Adding Nodes
 def add_Node(self,data):
    newNode=Node(data)
    
    if(self.head ==None):
        print(self)        
        self.head=newNode
        self.tail=newNode
        return newNode
        
    else:
        print(self)
        self.tail.next=newNode  #first node's next is the new Node
        self.tail=newNode      #it will be the new tail
        return newNode
    
 def print_Nodes(self):
     #print(self)
     current=self.head
     
     while(current is not None):
       print(current.data,end=" ")
       current=current.next

       
obj=SLL()
obj2=SLL()
obj.add_Node(2)
obj.add_Node(3)
print(obj)

obj.print_Nodes()
obj2.add_Node(5)
obj2.add_Node(5)
print()

print(obj2)
obj2.print_Nodes()

 

