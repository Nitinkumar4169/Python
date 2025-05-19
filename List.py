# map(), filter(), reduce()

#syntax :- map(function, iterable)

#Definition of map():- Applies a function to each item in an iterable (like a list) and returns a new iterable (map object).

numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)

print(result)