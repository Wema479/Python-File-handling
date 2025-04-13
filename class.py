# Open the file in read mode
with open("example.txt", "r") as file: 
    data =file.read() 
    print(data)


with open("output.txt", "w") as file: 
    file.write("Hello, Python!" *10) # Write "Hello, Python!" 10 times to the file)c