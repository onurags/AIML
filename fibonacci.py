# Input number of rows
rows = int(input("Enter no. of rows: "))

# Starting numbers
num1, num2 = 0, 1
count = 0

# Check for valid input
if rows <= 0:
    print("Please enter a positive integer")
elif rows == 1:
    print("Fibonacci sequence up to", rows, "is:")
    print(num1)
else:
    print("Fibonacci sequence:")
    while count < rows:
        print(num1)  # Print current number
        num_next = num1 + num2  # Calculate next number
        num1 = num2  # Shift values
        num2 = num_next
        count += 1  # Increase counter
