""" This is what determines the type of functionality a class has, how it handles it data and it overall behavior.
    Without method, a class would simply be a structure in other case, the "car" might have the following 
    methods: change color, start engine, stop engine, change gear.
    Just as there are instances and class attributes, there are also instances and class methods.
    
    Instance method operate on an instance of a class; whereas class methods operate on the class itself instance 
    methods are nothing but function defined inside a class that operate on "instance" of that class adding method to 
    class; a showDescription() to print the current value of all instances attribute and a changeColor() method to 
    change the values of "color" attributes a class program
"""
class infrastructure:
    type = "house"  #class attribute

# initialize with instance attribute
    def __init__(self, style, color):
        self.color = color
        self.style = style

    def showDescription(self):
        print("This infrastructure is a", self.style, "painted", self.color )
 
    def changeColor(self, color):
        self.color = color

h = infrastructure("bungalow", "yellow") #object

# access attribute  
h.showDescription()
h.changeColor("white")
print(h.style)
print(h.color)

# del attributes and object, to del any attribute we use the del keyword
# del h.color