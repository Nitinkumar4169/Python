#Operator Overloading

#Definition :- Operator Overloading in python allows you to define how operators like +,-,*,etc.., behave for objects of a custom class.

#Code

class Dog:
  # the Dog class
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def __gt__(self, other):    #gt = greater than
     return True if self.age > other.age else False   

roger = Dog('Roger', 8)       #objects
syd = Dog('syd', 7)           #objects

print(roger > syd)

