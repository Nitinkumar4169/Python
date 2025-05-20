# map(), filter(), reduce()

#syntax :- map(function, iterable)

#Definition of map():- Applies a function to each item in an iterable (like a list) and returns a new iterable (map object).

numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)

print(result)

#FILTER()

#SYNTAX :- filter(function, iterable)

#Definition :- Filters items from an iterable based on a function that returns True or False

numbers = [1, 2, 3]

def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)

print(result)