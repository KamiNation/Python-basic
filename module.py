""" A module is a piece of software that has a specific functionality. Each module is a different file, 
    which can be added separately. A test editor is to be used and must be saved in the same folder as the python file.
    Importing a module using the import statement, but we are interested in the function in the module.
    To import a function or class from a module we use the "from module import" statement
    from square_module import square
    python has it own built-in module that you can import
"""
    
def square(x):
    result = x*x;
    return result