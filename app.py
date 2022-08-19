# A sample app that can be developed by the community.
# What it does at the moment is to only validate an input

print("Create acoount make we carry you go where you no know")

print("Create account")
username = input("Enter username: ")
password = input("Enter password: ")


print("Your account has been created successfully")
print("login now!")


username2 = input("Enter username: ")
password2 = input("Enter password: ")

if username == username2 and password == password2:
    print("Logged in successfully!!!!")
else:
    print("Invalid credentials")
