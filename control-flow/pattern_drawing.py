# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use nested loops to draw the pattern
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next row
        row += 1
