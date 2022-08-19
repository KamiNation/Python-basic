""" Function are the first step to code re-use, they allow to define a re-usuable block of code that can be
    used repeatedly in a program. 
    syntax
    def function_name(); #Function name
    statement; #Function body, it is executed when the function is called
    return value; #Returns value and the function call and sends data back to the program

    The def statement only creates a function by passing values, known as arguments. Arguments are declared after 
    the function name in parenthesis, when you call a function with argument the values of those are copied to 
    their corresponding parameters inside the function
"""



def hello(name):  # Function name
    print("hello", name) # Statement
    
hello("bob") # Function call

def description(name, age, sport): # Function name
    print("My is", name,"i am", age, "yrs old", "i love to play", sport)  # Statement
    
description("kami", 24, "basketball") # Function call

""" Types of function; 
    positional, 
    keyword, 
    default argument, var length keyword arg(kwarg) and
    var length positional arg(arg)

    Positional are the most common, whose values are copied to their corresponding paragraph in order. 
    The only downside is that you need to pass argument in the order in which they are defined

    Keyword can be said to avoid positional argument confusion , you can pass argument using the name of their 
    corresponding parameters, in this case, the order of the argument no longer matter because argument are matched 
    by name, not position.
"""

# Example of keyword below
def bioData(name, job):
    print(name, "is a", job)
    
bioData(name="bob", job="devOps")

""" Default argument is used if the function is called without a corresponding argument. In short, default allows 
    you to make selected argument optional example of default.
"""

# Default arg
def employee(name, job="dev"):
    print(name, "is a", job)
    
employee("kayode", "manager")
employee("kayode")

""" Var length arg(*args and *kwargs) are useful when you want to create a function that takes am unlimited number of
    argument. 
    Unlimited in the sense that you do not know beforehand how many argument can be passed to that argument by the user.
    This feature is always referred to as var-args (*args), when you prefix a parameter with an asterik(*), it collects
    all the unlimited positional arg into a tuple. Due to the fact that it is a normal tuple object, you can perform
    any operation that a tuple support, like indexing, iteration etc
"""

#example of a *args
def printArg(*args):
    print(args)
    
printArg(1,32,56,89)

""" **kwargs, the ** syntax is similar but it only works for keyword argument. It collect them into a new dictionary, 
    where the arg name are the key, and the values are the corresponding dictionary values example of a **kwarg
"""

def printArg(**kwargs):
    print(kwargs)
printArg(name="bob", age=25, job="devOps")

"""Return value is used to return value from a function. Once, a return statement is executed, nothing else in the 
    function body is executed.
"""

# Example of a function
def sum(a,b):
    return a+b

x=sum(3,4)
print(x)

# Return multiple
def multiple(a,b):
    return a+b, a-b

result = multiple(9, 6)
print(result)

# Using the function in a module
from module import square
print(square(2))

# Using input with function
def print_name(name, age):
    print("Welcome " +name+ ". You are " +str(age)+ " years old.")

# Getting user input from keyboard with input 
name = input("Enter your name: ") # Input name
age = input("Enter your age: ") # Input age
print_name(name, age) # Print name and age after input by calling the function "print_name"


# Return statement in function 
def add_numbers(num1, num2):
    return num1+num2

num1 = int(input("Enter no: "))
num2 = int(input("Enter no: "))
print(add_numbers(num1, num2))