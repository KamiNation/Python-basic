# a class is a blueprint from which individual objects are created
# creating a class, to create your own custom class, you first need to define a class, using the keyword "class"

# suppose you want to create objects to represent a info about a car. each object will represent a single car, you will 
# just need to define a "class" called "car"
class car:
    pass # here the pass statement is used to indicate the class empty

# the self parameter refers to the individual object itself. it is used to fetch or set 
# attribute of the particular instance
# the attribute parameter; every py class has two basic feature: "attribute" and "metthod"

# attributes are the individual things that differentiate one object from the other. 
# they determine the apperance, state or other qualities of that object

# attributes are defined in classes by variable and each object can have it own values for those var
# they are two types of attributes: instance and class 

# instance is a var that is unique to each object(instance). every object of that class has it own copy of that var. 
# any change made to the var doesn't reflect in other object of that class
class car:
    def __init__(self, color, style):
        self.color = color
        self.style = style

# class attribute is a var that is the same for all objects. and there is only one copy of that var that is shared with
# all objects. any changes to that var will reflect in all other objects
wheels = 4

# creating an object, you can create an object by calling the class name and passing argument as 
# as if it were a function

c = car("venza", "green")

# here, we created a new object from the "class car" by passing string for the style and color parameters.
# but we did not pass the self argument, this is because, when you create a new object, python automatically 
# determines what self is(our newly created object in this case) and passes it to the __init__ method

# access and modify attribute, the attribute of an instance are accessed and assigned to by using the "dot . notation" 
print(c.style)
print(c.color)



# a class program
class infrastructure:
    type = "house"  #class attribute

    def __init__(self, style, color):
        self.color = color
        self.style = style

h = infrastructure("bungalow", "yellow")
print(h.style)
print(h.color)