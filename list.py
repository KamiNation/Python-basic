""" A list is a mutuable, ordered sequence of element. 
    Mutuable is that you can change the element inside while order refers to the index location. 
    Each element is called an item.
    List are also known as data collection i.e they can store multiple item.
"""

# A list named 'name', list1 and list2 with different item set
name = ["ola", "shile", "taiwo"] # A string list
print(name[0])

list1 = ["ola", "shile", 2, 6, 9, True] # A list with different data type
print(list1)

list2 = ["cat", "come", ["fish", "goat"], 70] # A list within a list
print(list2[2])

#print(cmp(list1, list2))

# Changing values of a list
# A list named student
student = ["godwin", "emefele", "sport director", "dark",  "computer science"]
student.sort() # it returns the class type of an object
student.append("python") # appends an element to the list
student.extend(["basketball", "whot"]) # adds multiple element to a string
print(student[1]) #index
print(student.index("emefele")) #index
print(max(student)) #max item from the list is returned
print(min(student)) #min item from the list is returned
print(len(student)) #length of list is returned
print(type(student)) #return type
print(student) # print student
student [1] = 20


# A list can take an iterable construct and turns it into a list
string1 = "python"
list1 = list(string1)
print(list1)
print(list1[3])
print(string1)


# If you want to access the content of the list without printing it out like a list you can use the 
# for in to access the list like below
israel = ["Aries", "Taurus", "Leo", "Scorpio", "Libra"]
for i in israel:
    print(i)
print(israel)


num = [1, 2, 3, 4, 5]
num.append(8)
num.insert(2, 11)
print(111 in num)
print(len(num))