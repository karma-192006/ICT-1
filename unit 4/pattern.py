def pattern(n):
    if n == 1:
        print("*")    
        return 
    pattern(n - 1)
    print("*" * n)

n=int(input("Enter a number:"))

print( pattern(n))

