#function are the first step to code re-use, they allow to define a re-usuable block of code
#that can be used repeatedly in a program
#syntax
# def function_name(); function name
# statement; function body, it is executed when the function is called
# return value; returns value and the function call and sends data back to the program

#the def statement only creates a function by passing values, known as arguments.
#arguments are declared after the function name in parenthesis, wehen you call a 
#function with argument the values of those are copied to their corresponding parameters inside the function

from email.policy import default


def hello(name):  #function name
    print("hello", name) #statement
hello("bob") #return value

def description(name, age, sport):
    print("my is", name,"i am", age, "yrs old", "i love to play", sport) 
description("kami", 24, "basketball")

#types of function; positional, keyword, default argument, var length keyword arg(kwarg), var length positional arg(arg)

#positional are the most common, whose values are copied to their corresponding paragraph in order. the only downside 
#is that you need to pass argument in the order in which they are defined

#keyword can be said to avoid positional argument confusion , you can pass argument using the name of their corresponding
#parameters, in this case, the order of the argument no longer matter because argument are matched by name, not position 
#example of keyword below
def bioData(name, job):
    print(name, "is a", job)
bioData(name="bob", job="devOps")

#default argument is used if the function is called without a corresponding argument. in short, default allows you to
#make selected argument optional
#example of default
def employee(name, job="dev"):
    print(name, "is a", job)
employee("kayode", "manager")
employee("kayode")

#var length arg(*args and *kwargs) are useful when you want to create a function that takes am unlimited number of
#argument. unlimited in the sense that you do not know beforehand how many argument can be passed to that argument
#by the user. this feature is alwasy referred to as var-args (*args), when you prefix a parameter with an asterik(*),
#it collects all the unlimited positional arg into a tuple. due to the fact that it is a normal tuple object, you can
#perform any operation that a tuple support, like indexing, iteration etc
#example of a *args
def printArg(*args):
    print(args)
printArg(1,32,56,89)

#**kwargs, the ** syntax is similar but it only works for keyword argument. it collect them into a new dictionary, where
#the arg name are the key, and the values are the corresponding dictionary values
#example of a **kwarg
def printArg(**kwargs):
    print(kwargs)
printArg(name="bob", age=25, job="devOps")

# return value is used to return value from a function. once, a return statement is executed, nothing else in the function
# body is executed
# example of a function
def sum(a,b):
    return a+b
x=sum(3,4)
print(x)

#return multiple
def multiple(a,b):
    return a+b, a-b
result = multiple(9, 6)
print(result)

# using the function in a module
from module import square
print(square(2))