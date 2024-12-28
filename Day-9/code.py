# --------------------------------------------- #
# -------   Opening and Reading Files   ------- #
# --------------------------------------------- #
file = open("Day-9\example.text", "r")

# Read the content of the file
content = file.read()
print(content)

# close the file
file.close()  # Always close the file after opening it to free system resources


# -------------------------------------------------------- #
# -------   Using "with" for Safer File Handling   ------- #
# -------------------------------------------------------- #
# Open and read file using context manager
with open("Day-9\example.text", "r") as data_file:
    data = data_file.read()
    print(data)
# File automatically closes after the block


# ------------------------------------- #
# -------   Writing to a File   ------- #
# ------------------------------------- #
# Open a file in write mode (overwrites if exists)
with open("new_example.text", "w") as file:
    file.write("This is a new line.\n")
    file.write("Learning Python is fun!")
    

# --------------------------------------- #
# -------   Appending to a File   ------- #
# --------------------------------------- #
# Open a file in append mode
with open("example.txt", "a") as file:
    file.write("\nAppending new content.")


# ---------------------------------------- #
# -------   Reading Line by Line   ------- #
# ---------------------------------------- #
# Open file and read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove trailing newlines


