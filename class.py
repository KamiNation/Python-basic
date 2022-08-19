""" A class is a blueprint from which individual objects are created.
    Creating a class: To create your own custom class, you first need to define a class, using the keyword 'class'
    Suppose you want to create objects to represent a info about a car. Each object will represent a single car,
    you will just need to define a "class" called 'car'.
"""

# A class with the name car
class car:
    pass # here the pass statement is used to indicate the class empty

""" The self parameter refers to the individual object itself. It is used to fetch or set  attribute of the
    particular instance. The attribute parameter; every py class has two basic feature: "attribute" and "metthod".

    Attributes are the individual things that differentiate one object from the other. They determine the apperance, 
    state or other qualities of that object.

    Attributes are defined in classes by variable and each object can have it own values for those var they are 
    two types of attributes: instance and class 

    Instance is a var that is unique to each object(instance). Every object of that class has it own copy of that var. 
    Any change made to the var doesn't reflect in other object of that class.
"""

class car:
    def __init__(self, color, style):
        self.color = color
        self.style = style

# Class attribute is a var that is the same for all objects. And there is only one copy of that var that is shared with
# all objects. Any changes to that var will reflect in all other objects.
    wheels = 4

# Creating an object, you can create an object by calling the class name and passing argument as if it were a function.

c = car("venza", "green")
""" Here, we created a new object from the "class car" by passing string for the style and color parameters.
    but we did not pass the self argument, this is because, when you create a new object, python automatically 
    determines what self is (our newly created object in this case) and passes it to the __init__ method. 
"""

# Access and modify attribute, the attribute of an instance are accessed and assigned to by using the "dot . notation" 
print(c.style)
print(c.color)



# A class program
class infrastructure:
    type = "house"  #class attribute

    def __init__(self, style, color):
        self.color = color
        self.style = style

h = infrastructure("bungalow", "yellow")
print(h.style)
print(h.color)

class Employee: #Class declaration
    name = "John doe"

    def show(self): #Function called a method
        print("Employee name is ", self.name)

a = Employee() #class instantiate
a.show()

class Vampires:
    name = "Niklaus"
    type = "Hybrid"
    age = 10000

    def show(self):
        print("The vampire bio-information is:", self.name, self.type,  self.age)

v = Vampires()
v.show()
# print(v.show())


# inheritance
class Player:
    def captain(self):
        print("I am the captain of the team")

class Striker(Player):
    def Score(self, name):
        print(f"My name is {name} and i score goals")

s = Player()
s.captain()

p = Striker()
p.Score("Mason")
print(issubclass(Striker, Player))

# continuation on inheritance
class Solution1:
    def Add(self, num1, num2):
        return num1 + num2
    
class Solution2:
    def Multiply(self, num1, num2):
        return num1 * num2
    
class Solution3(Solution1, Solution2):
    def show(self, a, b):
        a = int(input("Enter a num: "))
        b = int(input("Enter a num: "))
        return (a/b)

a = Solution1()
a = a.Add(4,5)
print(a)

b = Solution2()
b = b.Multiply(5,9)
print(b)

c = Solution3()
d = c.show(a, b)
print(d)

# construct
class Beings:
    def __init__(self):
        print("This is a non-para")
        
    def show(self, name):
        print(f'This is a para {name}')

b = Beings()
b.show("Para")


class Employee:
    def __init__(self, name):
        self.name = name
        print(f"My name is {self.name}")
        
    def show(self, age, salary):
        self.age = age
        self.salary = salary
        print(f'Welcome {self.name}. Your salary for the month is {self.salary} and you are {self.age} today')
    
e = Employee("Mike")
e.show(21, 500000)