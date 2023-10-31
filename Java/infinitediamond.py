def print_diamond(n):
    # Print upper part of diamond
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

    # Print lower part of diamond
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

# Number of rows for the diamond (change as needed)
rows = 5

# Infinite loop to print the diamond shape
while True:
    print_diamond(rows)
