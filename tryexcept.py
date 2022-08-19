# the try except is used to stop errors from showing on the src
try:
    x = int(input("Input an integer: "))
    print(x)
except ValueError:
    print("Somthing went wrong, pls try again")
finally:
    print("nothibg went wrong")

# the except method can be used for specific type

