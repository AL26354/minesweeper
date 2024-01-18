
print("Welcome to minesweeper!")
while True:
    selection = str(input("Please choose a grid size; (S)mall, (M)edium, (L)arge: "))
    if selection[0].upper() == "S":
        size = 8
        mines = 10
        break
    elif selection[0].upper() == "M":
        size = 12
        mines = 22
        break
    elif selection[0].upper() == "L":
        size = 16
        mines = 40
        break
    else:
        print("Invalid input.")

