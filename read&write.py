file = open("C:/Users/HP/Desktop/Python-basic/hello.txt", "r+")
file.write("#This is a comment")
print(file.readlines())
file.close()