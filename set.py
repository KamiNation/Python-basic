""" A set is an unordered collection of unique items. They are commonly used for computing
    mathematical operations such as union, difference and symmetric difference.
    Properties are: 
    sets are unorderd, 
    items are unique and 
    are mutuable.
"""
# You can create a set by placing a comma-separated sequence of items in curly bracket {}
# A set named color
colors = {"red", "blue", "green", "orange", "indigo", "violet", "yellow", "green"}
print(colors)

""" If you create a set with duplicate items, the duplicate will be removed automatically during the set creation
    You can also create a set using the set function, that is also great for converting sequence iterable to set and 
    removing duplicate from list.
"""


# A list conversion to set
list1 = ["bola", "shile", 2, 6, 9, True, "bola"]
newList = set(list1)
print(newList)

bioData = set(["kami", "adedamola", "computer science", "anime", "basketball"])

bioData.add("python") #adding items to a set
bioData.remove("basketball") #removing items from a set
print(newList.union(bioData)) #set union returns a new set containing the union of 2 or more set
newList.update(bioData)
print(newList.intersection(bioData)) #set intersection
print(newList.symmetric_difference(bioData)) #symmetric_difference
print(newList.difference(bioData)) #set difference
print(bioData) #print set

# Using the for in
for i in bioData:
    print(i)
    
# Multiple set code
