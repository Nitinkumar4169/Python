#Recursion

# A function in python which call itself

#Example of recursion is factorial no.

#3! = 3 * 2 * 1 = 6
#4! = 4 * 3 * 2 * 1 = 24

#code

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))

#Decorators

#Defination :- Decorators are a powerful feature in python that allow you to modify or extend the behavioiur of functions or methods without changing their code


#code
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper


@logtime
def hello():
    print("hello")

hello()    
