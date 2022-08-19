""" This execute the code inside "if" if it is true, however the while loop continues to execute the code the 
    repeatedly as long a the condition is true. Repeating an action until a condiition is not.
    Syntax:
    while condition:
        statement
"""

# Sample programs
x = 10
while x > 0:
    print(x)
    x = x-1
    print("go!")
    
i = 1
while i <= 10:
    print(i * "+")
    i += 1
    

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(num):
    print(num[i])
    i += 1


secret_number = 100
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess = int(input("Guess :"))
    guess_count += 1
    if guess == secret_number:
        print("You got the correct no!")
        break
else:
    print("You did not get the guess")

