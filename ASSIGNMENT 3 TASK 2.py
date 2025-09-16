import math

try:
    number=float(input("Enter a number : "))

    if number>=0:
        sqrt=math.sqrt(number)
        log=math.log(number)
        sin=math.sin(number)

        print("\nResults :")
        print(f"Square Root : {sqrt} ")
        print(f"Logarithm : {log} ")
        print(f"Sine : {sin} ")

except:
        print("Invalid input. Please enter a numeric value.")

