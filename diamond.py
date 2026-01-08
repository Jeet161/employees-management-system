rows = int(input("Enter number of rows: "))
# Upper half of the diamond
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Print leading spaces
    for j in range(i, 0, -1):
        print(j, end="")  # Print numbers in descending order
    for k in range(2, i + 1):
        print(k, end="")  # Print numbers in ascending order
    print()

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")  # Print leading spaces
    for j in range(i, 0, -1):
        print(j, end="")  # Print numbers in descending order
    for k in range(2, i + 1):
        print(k, end="")  # Print numbers in ascending order
    print()