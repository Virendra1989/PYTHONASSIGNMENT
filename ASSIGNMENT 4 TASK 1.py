def read_file(filename):
        try:
            with open(filename,"r")as file:
             print(f"Reading file content:{filename}\n")

             for line_number,line in enumerate(file,start=1):
              print(f"Line {line_number}:{line.strip()}")
        except FileNotFoundError:    
                 print(f"Error: The file '{filename}' was not found.")

        except Exception as e:
                 print(f"An Unexpectec Error Occured")


read_file("sample.txt")
