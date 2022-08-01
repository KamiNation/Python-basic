#dictionary are python implementation of a data structure, generally known
#as associative arrays, hashes, or hashmap. you can look at it as a mapping 
#between a set of indexes (known as keys) and a set of values. each key maps
#to a value. the association of a key and a value is called a key:value pair or 
#somtimes an item

#you can create a dict by placing a comma-separated list of key:value pairs in {},
#each key is separated from its associated value by a colon ":"

#properties of a dict: a key can appear only once, the keys must be unique, if a key
#is speciifed more than once during the creation of a dictionary, the last value for 
#that key becomes the associated value

#creating a dict {}
studentBiodata = {"name":"kami", "age": 23, "department":"computer science", "sport":"basketball", "state":"ogun"}
print(studentBiodata)

#creating a dict using list of zipped keys/values
keys = ["name", "age", "sport"]
values = ["bob", 34, "basketball"]
bio = dict(zip(keys, values))
print(bio)

#accessing dict items; the order of key:value pair is not always the same. in general, the 
#order item in a dict is unpredictable. however this is not a problem because the items of a 
#dict are not indexed with integer indices. insttead, you use the keys to access the corresponding values.

#you can fetch a value from a dict by ref to it keys in []  
print(bio["age"])

#if you refer to a key that is not in the dict you wil get an exception, to avoid such exception
#you can use the "special dict get() method"
#this method returns the value for key if the key is in the dict, else none, so that this method never
#misses a keyword

#when key is present
print(bio.get("sport"))
#when key is not
print(bio.get("count"))

#adding or updating a dict, just refer to the item by it key and assign a value. if the key is already
#present in the dict, it values is replaced by the new one while if the key is not, it is added to the 
#with the value
a = {"name":"isekai",
         "age": 23,
         "job": "death note"
}

a ["name"] = "light yagami"
a ["city"] = "japan"
print(a)


b = {"fav":"mikami",
         "school": "anime schol",
         "email": "deathnote@gmail.com"
}

#merge two dict together using the built-in update() to merge the keys and values of one of one dict into 
#another. note that this blindly overwrites values of the same key if there is a clash
a.update(b)
print(a)

#removing dicitonary items can be done in 3 ways; remove an item by key, by del, by all items
#if you know the key of the item you want to remove, yoy can use the pop() method, it removes the key
#and return the value

#a = a.pop("age")
#del a["city"]
#a.clear()
#print(a)