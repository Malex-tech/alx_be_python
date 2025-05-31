# pattern_drawing.py

# Ask the user for the size of the square pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in one row
    for col in range(size):
        print("*", end="")  # print * without moving to the next line
    print()  # move to the next line after printing one row
    row += 1
