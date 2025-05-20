#Exceptions :- used to handle error in python

try:
  result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!') 
finally:
    result = 1     

print(result)    #1


#Raise exception
try:
   raise Exception('An error!')
except Exception as error:
   print(error)


#Another example
class DogNotFoundException(Exception):
     print("inside")
     pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')