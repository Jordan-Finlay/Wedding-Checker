def enter_name():
    """
    Asks user to input name to check he/she is on the wedding list
    """
    while True:
        print("Welcome to the wedding!")
        print("You are using our automated system")
        print("We will log you in whilst taking your drinks and food selections")
        print("First we will ask for your first then second name")

        name_str = input("Please enter your first name here;\n")
        last_str = input("Please enter your last name here;\n")

        if validate_name(name_str, last_str):
            print(f"Welcome to the wedding '{name_str} {last_str}'")
            print("We hope you have a fantastic time!\n")
            break

    return name_str


def validate_name(name_str, last_str):
    """
    This is used to check the name inputted is correct
    """
    if not name_str.isalpha():
        print(f"You entered : '{name_str}'.")
        print("You cannot use numbers")
        print("This is not a valid name.\n")
        return False
    elif not last_str.isalpha():
        print(f"You entered : '{last_str}'.")
        print("You cannot use numbers")
        print("This is not a valid name.\n")
        return False
    elif len(name_str) == 1:
        print(f"You entered : '{name_str}'.")
        print("Name is too short")
        print("Please try again with a full name")
        return False
    elif len(last_str) == 1:
        print(f"You entered : '{last_str}'.")
        print("Name is too short")
        print("Please try again with a full name")
        return False
    else:
        return True


drinks = ["Coke", "Sprite", "Fanta", "Beer", "Cider", 
          "Wine", "champagne", "Water", "Tea", "Coffee"]


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
                if drinks_number >= 10:
                    print(f"You picked: '{drinks_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{drinks[drinks_number]}'. Great choice!\n")
                    break
        except ValueError:
            print(f"You typed: '{drinks_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return drinks_number


meat_dishes = ["Salmon", "Steak", "Chicken", "Lamb", "Beef"]
vegan_dishes = ["Vegan Alfredo", "Vegan Chicken", "Vegan Stew",
                "Vegan Meatball Pasta", "Vegan Tofu Stirfry"]


def order_food():
    """
    An input to ask the user what main they'd like
    """
    print("We shall go onto our main menu now")
    print("Would you like to see the vegan menu?")

    while True:
        vegan = input("Please enter y or n.\n")
        if vegan == "y":
            vegan_food()
        elif vegan == "n":
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
    print("Great! Heres our vegan options;")
    list_vegan_dishes = enumerate(vegan_dishes)

    for vegan_dish in list_vegan_dishes:
        print(vegan_dish)

    while True:
        try:
            vegan_number = input("Choose a number:\n")
            vegan_number = int(vegan_number)
            if type(vegan_number) == int:
                if vegan_number >= 5:
                    print(f"You picked: '{vegan_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{vegan_dishes[vegan_number]}'. Great choice!\n")
                    break
        except ValueError:
            print(f"You typed: '{vegan_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return vegan_number


def meat_food():
    """
    Meat options
    """
    print("Great! Heres our meat options;")
    list_meat_dishes = enumerate(meat_dishes)

    for meat_dish in list_meat_dishes:
        print(meat_dish)

    while True:
        try:
            meat_number = input("Choose a number:\n")
            meat_number = int(meat_number)
            if type(meat_number) == int:
                if meat_number >= 5:
                    print(f"You picked: '{meat_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{meat_dishes[meat_number]}'. Great choice!\n")
                    break
        except ValueError:
            print(f"You typed: '{meat_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return meat_number


def second_round():
    """
    A function to let the user order a second drink for dessert
    """
    print("How about another drink for dessert?")
    print("Would you like to see our drinks menu again?")
    print("Press 'y' to see our drinks menu")
    print("or 'n' to move onto the dessert menu")

    while True:
        second_drink = input("Please enter y or n.\n")
        if second_drink == "y":
            order_drink(drinks)
        elif second_drink == "n":
            break
        else:
            print(f"you picked '{second_drink}'.")
            print("please pick 'y' or 'n'.\n")
            continue
        break


desserts = ["Sticky Toffee Pudding", "Chocolate Cake", "Strawberry Cheese Cake"]
vegan_desserts = ["Coconut Cheesecake", "Vegan Meringue Pie", "Vegan Chocolate brownies"]


def order_dessert():
    """
    A function that allows the user to order a dessert
    """
    print("We shall go onto our dessert menu now")
    print("Would you like to see the vegan menu?")

    while True:
        vegan = input("Please enter y or n.\n")
        if vegan == "y":
            vegan_dessert()
        elif vegan == "n":
            milk_dessert()
            break
        else:
            print(f"you picked '{vegan}'.")
            print("please pick 'y' or 'n'.\n")
            continue
        break


def milk_dessert():
    """
    A function for non vegan desserts
    """
    list_desserts = enumerate(desserts)

    for dessert in list_desserts:
        print(dessert)

    while True:
        try:
            dessert_number = input("Choose a number:\n")
            dessert_number = int(dessert_number)
            if type(dessert_number) == int:
                if dessert_number >= 3:
                    print(f"You picked: '{dessert_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{desserts[dessert_number]}'. Great choice!\n")
                    break
        except ValueError:
            print(f"You typed: '{dessert_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return dessert_number


def vegan_dessert():
    """
    A function for vegan desserts
    """
    list_vegan_desserts = enumerate(vegan_desserts)

    for vegan_dessert in list_vegan_desserts:
        print(vegan_dessert)

    while True:
        try:
            dessert_number = input("Choose a number:\n")
            dessert_number = int(dessert_number)
            if type(dessert_number) == int:
                if dessert_number >= 3:
                    print(f"You picked: '{dessert_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n")
                    continue
                else:
                    print(f"You choose '{desserts[dessert_number]}'. Great choice!\n")
                    break
        except ValueError:
            print(f"You typed: '{dessert_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n")
            continue
        break

    return dessert_number


def song_request():
    """
    A function to allow the user to request a song
    """
    print("Do you have any song requests?")
    print("Due to our large number of requests we will try our best to play as many as we can")

    song = input("Choose any song you'd like;\n")

    print(f"You have selected '{song}' Great song choice!\n")


def results():
    """
    A final review of all the selected options from the user
    """
    print("To sum up - you have selected;")
    
    print(f'{order_food}')
    print(order_dessert)
    print("Great choices!")
    print("Go into the wedding hall and enjoy the night!")
    print("We hope you have the best time!")
    print("Thanks for using our automated system!")
    print("If you have any idea for improvements")
    print("Talk to Jordan Finlay in the wedding hall")
    print("He's in the black suit and probably dancing poorly")
    print("Thanks for coming!")


def main():
    """
    Runs all program functions
    """
    enter_name()
    order_drink(drinks)
    order_food()
    second_round()
    order_dessert()
    song_request()
    results()


main()

print(f'{order_food}')
print(f'{dessert_number}')