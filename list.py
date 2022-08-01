#a list is a mutuable, ordered sequence of element. mutuable is that you can
#change the element inside while order refers to the index location. each element
#is called an item. list are also known as data collection i.e they can store multiple item
name = ["bola", "shile", "taiwo"]# a string list
print(name[0])

list1 = ["bola", "shile", 2, 6, 9, True] # a list with different data type
print(list1)

list2 = ["cat", "come", ["fish", "goat"], 70] # a list within a list
print(list2[2])

#print(cmp(list1, list2))

#changing values of a list
student = ["godwin", "emefele", "sport director", "dark",  "computer science"]
student.sort()# it returns the class type of an object
student.append("python")# appends an element to the list
student.extend(["basketball", "whot"])#adds multiple element to a string
print(student[1])#index
print(student.index("emefele"))#index
print(max(student))#max item from the list is returned
print(min(student))#min item from the list is returned
print(len(student))#length of list is returned
print(type(student))#return type
print(student)
student [1] = 20


#a list can take an iterable construct and turns it into a list
string1 = "python"
list1 = list(string1)
print(list1)
print(list1[3])
print(string1)