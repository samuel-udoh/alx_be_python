size = int(input("Enter the size of the pattern: "))
iteration = 0
while iteration < size:
    for i in range(0, size):
        print("*", end="")
    iteration += 1;
    print()