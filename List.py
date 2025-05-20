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

numbers = [1, 2, 3, 4, 5, 6]

def isEven(n):
    return n % 2 == 0

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))



#REDUCE()

#syntax :- function(function, iterable)

#Definition :- Reduce is used to calcuate a value out of a sequence like a list or [items of an iterable to reduce it to a single value]

#It's little bit different from map() or filter() where it's not available automatically we have to import it from standard library func tools

from functools import reduce

expenses = [
      ('Dinner', 80),
      ('Car repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)

