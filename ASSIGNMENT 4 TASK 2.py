def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print(f"Data successfully written to '{filename}'.")

def append_to_file(filename):
    additional_input = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print(f"Data successfully appended to '{filename}'.")

def read_file(filename):
    print(f"\n Final content of '{filename}':\n")
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"Line Number {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "output.txt"
write_to_file(filename)
append_to_file(filename)
read_file(filename)
 

    
