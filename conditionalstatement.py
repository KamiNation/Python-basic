#the code executes in a sequential order i.e the first line
#will be executed first followed by the second line etc.
#conditional statement are used where decision making is required

#if statement is used to execute a code block, only if a "test condition is true"
x = 1
y = 3
if x < y:
    print("x is less than y")

#if else statement, here we combine the "else" code block with the "if code block",
#the if code block is only executed only if the test condition is true, and the else
#code block is executed in the cases when the test is false
x = 5
y = 10
if x > y:
    print("x is greater than y") 
else:
        print("y is greater than x")

#elif statement is used to check multiple condition. in such cases, firstly
#the if test condition is checked, if it is true, then the if code block
#is executed amd if it is false, then the next elif test condition is checked and so on.
#if all condition are false, then the else code is executed
x = 2
y = 3
if x > y:
    print("x is > y")
elif x == y:
    print("x is equal to y")
else:
        print("y is < x")


