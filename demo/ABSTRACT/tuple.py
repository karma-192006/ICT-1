my_tuple=('Hello',123456)
print(type(my_tuple))
print(my_tuple) #output: ('Hello',123456)
print(my_tuple[1]) #output: Hello
a,b=my_tuple
print(b)#output:123456
new_tup=tuple(a) #convert string 'Hello' to a tuple of characters
print(new_tup) #output: ('H','e','l','l','o')
concatenated_tuple=my_tuple+new_tup
print(concatenated_tuple) #Output: ('Hello',123456,'H','E','L','L','O')
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1])
del my_tuple
print (my_tuple) #This will raise an error because my_tuple has been deleted
