def fun1(x, y):
    if x == 0:
        return y
    else:
        return fun1(x - 1, y + x)
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
print("Result of ",x,"and",y,"is:",fun1(x,y))
