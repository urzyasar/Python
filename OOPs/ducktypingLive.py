#Duck Typing
class Bird:
       def fly(self):
              print("Fly with Wings")
class Aeroplane:
       def fly(self):
              print("Fly with Fuel")
class Fish:
       def swim(self):
              print("Swim in water")

for obj in Bird(),Aeroplane(),Fish():
       obj.fly()
