#Polymorphism

#Definition :- we call same method on different classes

#If two different classes have a method with the same name, they can be interchangeably

class Dog:
     def eat(self):
          print('Eating dog food')

class Cat:
     def eat(self):
          print('Eat cat food')   

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()