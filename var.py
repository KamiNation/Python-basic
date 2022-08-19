""" Variables are conainer for storing data values.
    The name of the var is declared on the left hand side (LHS) of the "=",
    and on the right hand side (RHS), we assign the value that we want to use later.
"""
# LHS      RHS
school = "hamoye"
print(school)



print("_/|_______________|\__")
print("|_/______|________\__|")
print("|_|0|____________|0|_|")

# Sample programs
first_no = float(input("first no: "))
second_no = int(input("second no: "))
sum = first_no + second_no
print(sum)

student_count = 1000
rating = 4.99
is_listed = False
program_name = "Python Programming"
print(student_count)
print(rating)
print(is_listed)
print(program_name)

name = input("What is your name: ")
print("Hello " + name)

   
num = range(10, 100, 40) #t he first no is a starting no, the second no 
# is the stopping number while the the last no is a step that is it defines
# how the number should be displayed
for nums in num:
    print(nums)
    

price = 5
print(price > 10 and price < 30) #and both
print(not price > 30) #not imverses any given value
print(price > 10 or price < 30) # or at least 