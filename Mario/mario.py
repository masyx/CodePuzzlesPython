height = int(input("What is the pyramid height? "))

for i in range(0, height):
    countSpace = height - i - 1
    
    for i in range(0, countSpace):
        print(" ", end="")
    for i in range(0, height - countSpace):
            print("#", end="") 
    
    print(" ", end="")

    for i in range(0, height - countSpace):
        print("#", end="")
    for i in range(0, countSpace):
            print(" ", end="")
    print()