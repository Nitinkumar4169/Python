#Docstrings

#Definition :- A docstring is a documentation string that desccribes what a function, class, or, modules does. It is a special kind of command enclosed in triple quotes (''' or """) and is placed right after the definition.


"""Dog module

This module does ... bla bla bla and provides the following classes:

- Dog

...
"""
class Dog:
  """A class representing a dog"""
  def __init__(self, name, age):
    """Initialize a new dog"""
    self.name = name
    self.age = age

  def bark(self):
    """Let the dog bark"""  
    print('WOF!')


print(help(Dog))    