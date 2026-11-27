print("----- FOOD MENU -----")
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Pasta")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You ordered Pizza")
    case 2:
        print("You ordered Burger")
    case 3:
        print("You ordered Sandwich")
    case 4:
        print("You ordered Pasta")
    case _:
        print("Invalid choice")