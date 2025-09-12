try:
    number = int(input("Enter Number: "))

    if number % 2 == 0:
        print("Number is an even number.")
    else:
        print("Number is an odd number.")
except ValueError:
    print("Please enter a valid number.")

