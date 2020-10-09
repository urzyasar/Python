"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
"e1 = element(1)"
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
 """                
    def removefromLast(self):
        if self.head:
            current = self.head
            if current.next:
                while current.next.next:
                    current = current.next
                temp = current.next.value 
                current.next = None
            else:
                temp = current.value
                current = None
            return temp 
        else:
            return -1
    
    def removefromFirst(self):
        if self.head:
            temp = self.head.value
            self.head = self.head.next
            return temp
        else:
            return -1
            """
    def printlist(self):
        if self.head:
            current = self.head
            list = [] 
            while current.next:
                list.append(current.value)
                current = current.next
            list.append(current.value)
            return list 
        else:
            return None
        """    
    def getposition(self, position):
        if self.head:
            current = self.head
            for i in range(position-1):
                if current.next:
                    current = current.next
                else:
                    return None
            return current.value
        else:
            return None
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    
    def insertinpos(self, new_value, position):
        if position == 1:
            new_element = Element(new_value)
            new_element.next=self.head
            self.head=new_element    
        else:
            current = self.head
            for i in range(position-2):
                current = current.next
            new_element = Element(new_value)
            new_element.next=current.next
            current.next=new_element    
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

    
    def deletefrompos(self, position):
        if position == 1:
            self.removefromQueue()
        else:
            current = self.head
            for i in range(position-2):
                current = current.next
            temp = current.next.value
            current.next=current.next.next 
            return temp
        pass
    
    def delete(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if prev == None:
            self.head = current.next
        elif current.value == value:
            prev.next = current.next
           """ 
        
        """if current.value == value:
            current.value = current.next.value
            current.next = current.next.next
        Delete the first node with a given value."""
        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
print ll.printlist()
"""
print ll.removefromLast()
print "After removing from Last"
print ll.printlist()
print ll.removefromFirst()
print "After removing from First"
print ll.printlist()
ll.append(Element(5))
ll.append(Element(6))
ll.append(Element(7))
ll.append(Element(8))
ll.append(Element(9))

print ll.printlist()

print ll.deletefrompos(4)
print "after del"
print ll.printlist()
print ll.getposition(13)

print ll.delete(2)
print ll.printlist()
ll.insertinpos(13,3)
print ll.printlist()
"""
