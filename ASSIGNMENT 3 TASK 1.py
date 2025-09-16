def factorial(n):
    if n<0:
        return "Factorial is not defined for negative number."
    elif n==0 or n==1:
        return 1
         
    else:
        return n*factorial(n-1)



number=int(input("Enter a number : "))
result=factorial(number)


print(f"The Factorial Of {number} is : {result}")
