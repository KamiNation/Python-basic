#string concatenation: the adding of one or more string to the end of another
print("i " + " love" + " string")

firstName = "Lola"
lastName = "girl"
fullName = firstName + " " + lastName
print(fullName)

#formatting string allows to write an entire string and inject the var we 
#want to use in the proper location. using this we can also concatenate a string
#and a number

#.format() method takes the passed argument, format them, and places them in the string where the 
#placeholder "{}" is
firstName = "femi"
age = 25
print("my name is {}".format(firstName))# using the .format() method
print("my name is " + firstName)# using the concatenation "+"
print("hello {}, you are + {} today".format(firstName, age))

#.fstring () python 3.6 upward is a new way to inject var into a string. by putting the 
#letter "f" in front of a string, you are able to inject a var into a string directly in line
firstName = "kai"
secondName = "ika"
age = 20
print(f"Hello {firstName}")
print(f"my second name is {firstName}")
print(f"my second name is, {firstName}" " " f"i am {age} yrs old")

#string index, indexing start from 0 not 1. a string is indexed with the []
word = "animal"
print(word[0])
print(word[1])
print(word[2])
print(word[3])

#string manipulation; alteration of string
firstName = "laspotech school"
print(firstName.title()) #the .title() capitalizes the first letter in the output
print(firstName.upper()) #the .upper() capitalizes all the letter in the output
print(firstName.lower()) #he .lower() converts all the letter to lower case in the output
print(firstName.replace("tech", "stress")) #he .replaces() the predefined text letter with the new one in the output
print(firstName.find("stress"))  #the .find() finds a specified word and displays in  the output and return the index