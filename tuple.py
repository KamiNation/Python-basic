#a tuple is an ordered sequence of element.  but it is not mutuable you cannot
#change the element inside while order refers to the index location. when you try to change the 
#value in a tuple, it will return a type error. similarly you cannot add or remove values either

#initializing an empty tuple by using the ()
emptyTuple = ()

#initializing am empty tuple by using the tuple function
emptyTuple = tuple()

#accessing elements of a tuple is just like accessing list, you use indexes
scores = (3, 4, 6, 8) 
print(scores[2])

#you can add multiple tuples together but you cannot add elements to a tuple
#there is no append() or etxend() method, you cammot remove element from a tuple
#there is no remove() or pop() method but you can find element in a tuple, you
#can also use the "check in operator" to check if element is in a tuple
#you can del a tuple by using the del keyword
tuple1 = (3, 6, 0, 5, 7)
tuple2 = (4, 2, 7, 8, 9)
newTuple = tuple1 + tuple2
#del tuple1
print(newTuple)