mylist=[1,2,3,4]
double=map(lambda x: x*2, mylist)
print(list(double))

#converting the result of double back to list 
mynewlist=(list(double))
double=map(lambda x: x/2, mynewlist)
print(mylist)



