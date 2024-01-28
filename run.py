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


drinks = ["Coke", "Sprite", "Fanta", "Beer", "Cider", "Wine", "champagne", "Water"]


def order_drink(drinks_number):
    """
    An input to ask the user which drink they'd like
    """
    print("Pick What drink would you like")
    list_drinks = enumerate(drinks)

    for drink in list_drinks:
        print(drink)

    while True:
        try:
            drinks_number = input("Choose a number:\n")
            drinks_number = int(drinks_number)
            if type(drinks_number) == int:
                if drinks_number >= 8:
                    print(f"You picked: '{drinks_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{drinks[drinks_number]}'\n")
                    break
        except ValueError:
            print(f"You typed: '{drinks_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return drinks_number    


main_dish = ["Salmon", "Steak", "Chicken", "Lamb", "Beef"]


def order_food():
    """
    An input to ask the user what main they'd like
    """
    print("Are you vegan?")

    while True:
        vegan = input("Please enter y or n.\n")
        if vegan == "y":
            print("Heres our vegan options")
            vegan_food()
        elif vegan == "n":
            print("Great heres our meat options")
            meat_food()
            break
        else:
            print(f"you picked '{vegan}'.")
            print("please pick 'y' or 'n'.\n") 
            continue
        break

def vegan_food():
    """
    Vegan options
    """
    print("Vegannnsss")

def meat_food():
    """
    Meat options
    """
    print("Meatttttt")




def main():
    """
    Runs all program functions
    """
    enter_name()
    order_drink(drinks)
    order_food()
    
    

main()