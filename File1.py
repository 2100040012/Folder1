#Tuple is like list, but it is unchangeable. 
thistuple=("apple",5,False)
print(thistuple)
print(type(thistuple))
#We can use Length function to see length of tuple. 
print(len(thistuple))
#To create a tuple with length one, we must use a comma.
thistuple1=("apple",)
print(thistuple1)
#Tuples allow duplicate items at different indexes.
thistuple2=("apple","orange","apple",6)
print(thistuple2)
#Tuples can be constructed with tuple function.
thistuple3=tuple(("man","John",55))
print(thistuple3)
#Same concept of indexing
print(thistuple3[1])
#But tuples cannot be updated. we can delete entire tuple only.
