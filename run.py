def enter_name():
    """
    Asks user to input name to check he/she is on the wedding list
    """
    while True:
        print("Please enter your full name")

        name_str = input("Enter your full name here.\n")

        if validate_name(name_str):
            print(f"Welcome to the wedding '{name_str}'")
            break

    order_drink(drinks)

    return name_str


def validate_name(name_str):
    """
    This is used to check the name inputted is correct
    """
    if not name_str.isalpha():
        print(f"You entered : '{name_str}'.")
        print("You cannot use numbers")
        print("This is not a valid name.\n")
        return False
    elif len(name_str) == 1:
        print(f"You entered : '{name_str}'.")
        print("Name is too short")
        print("Please try again with a full name")
        return False
    else:
        return True

drinks = ["Coke", "Sprite", "Water", "Beer", "Cider"]

def order_drink(drinks):
    """
    An input to ask the user which drink they'd like
    """
    print("Pick What drink would you like")
    list_drinks = enumerate(drinks)

    for drinks in list_drinks:
        print(drinks)

        while True:
            try:
                drinks_number = input("Choose a number:\n")
                drinks_number = int(drinks_number)
                if type(drinks_number) == int:
                    if drinks_number >= 4:
                        print(f"You picked: '{drinks_number}'.")
                        print("The number isn't in the list..\n")
                        continue
                    else:
                        print(f"You choose '{drinks[drinks_number]}'\n")
                        break
            except ValueError:
                print(f"You filled in: '{drinks_number}'.")
                print("It is not a number.\nPlease try again.\n")
                continue
                break

        return drinks_number



def main():
    """
    Runs all program functions
    """
    enter_name()
    

main()