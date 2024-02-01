from colorama import Fore, Style

"""
Globals
"""
user_choices = [] #Empty list for user choices

drinks = ["Coke", "Sprite", "Fanta", "Beer", "Cider",
          "Wine", "champagne", "Water", "Tea", "Coffee"]

desserts = ["Sticky Toffee Pudding",
            "Chocolate Cake", "Strawberry Cheese Cake"]
vegan_desserts = ["Coconut Cheesecake",
                  "Vegan Meringue Pie", "Vegan Chocolate brownies"]

meat_dishes = ["Salmon", "Steak", "Chicken", "Lamb", "Beef"]
vegan_dishes = ["Vegan Alfredo", "Vegan Chicken", "Vegan Stew",
                "Vegan Meatball Pasta", "Vegan Tofu Stirfry"]


def enter_name():
    """
    Asks user to input name to check he/she is on the wedding list
    Checks for first and last name
    """
    while True:
        print(Fore.BLUE + "Welcome to the wedding!")
        print("You are using our automated system")
        print("We will log you in whilst taking your drinks and food order")
        print("To start we will ask for your first then second name" + Style.RESET_ALL)

        name_str = input(Fore.GREEN + "Please enter your first name here;\n" + Style.RESET_ALL) #Checks first name
        last_str = input(Fore.GREEN + "Please enter your last name here;\n" + Style.RESET_ALL) #Checks second name

        if validate_name(name_str, last_str): #If both checks are fine - continue
            print(Fore.GREEN + f"Welcome to the wedding '{name_str} {last_str}'")
            print("We hope you have a fantastic time!\n" + Style.RESET_ALL)
            break

    return name_str


def validate_name(name_str, last_str):
    """
    This is used to check the name inputted is correct
    Validate checks for input With only characters
    Validate checks for input with no numbers
    """
    if not name_str.isalpha(): #A check to insure no numbers are used
        print(Fore.RED + f"You entered : '{name_str}'.")
        print("You cannot use numbers")
        print("This is not a valid name.\n")
        return False
    elif not last_str.isalpha(): #A check to insure no numbers are used
        print(f"You entered : '{last_str}'.")
        print("You cannot use numbers")
        print("This is not a valid name.\n")
        return False
    elif len(name_str) == 1: #A check to insure name isn't too short
        print(f"You entered : '{name_str}'.")
        print("Name is too short")
        print("Please try again with a full name")
        return False
    elif len(last_str) == 1: #A check to insure name isn't too short
        print(f"You entered : '{last_str}'.")
        print("Name is too short")
        print("Please try again with a full name" + Style.RESET_ALL)
        return False
    else:
        return True


def order_drink(drinks_number):
    """
    An input to ask the user which drink they'd like
    Allowing the user to select from a list 
    """
    print(Fore.BLUE + "Pick What drink would you like" + Style.RESET_ALL)
    list_drinks = enumerate(drinks)

    for drink in list_drinks: #A loop to generate a list of drinks
        print(drink)

    while True:
        try:
            drinks_number = input(Fore.GREEN + "Choose a number:\n" + Style.RESET_ALL)
            drinks_number = int(drinks_number)
            if type(drinks_number) == int:
                if drinks_number >= 10: #A check so the user can't pick outside the list
                    print(Fore.RED + f"You picked: '{drinks_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE +
                        f"You choose '{drinks[drinks_number]}'. Great choice!\n" + Style.RESET_ALL)
                    user_choices.append(drinks[drinks_number])
                    for item in user_choices: #Returns the user choice to global
                        break
        except ValueError:
            print(Fore.RED + f"You typed: '{drinks_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n" + Style.RESET_ALL)
            continue
        break

    return drinks_number


def order_food():
    """
    An input to ask the user what main they'd like
    It will ask if the user is vegan and will generate a menu accordingly
    """
    print(Fore.BLUE + "We shall go onto our main menu now")
    print("Would you like to see the vegan menu?" + Style.RESET_ALL)

    while True:
        vegan = input(Fore.GREEN + "Please enter y or n.\n" + Style.RESET_ALL)
        if vegan == "y":
            vegan_food() #Runs vegan menu
        elif vegan == "n":
            meat_food() #Runs non vegan menu
            break
        else:
            print(Fore.RED + f"you picked '{vegan}'.")
            print("please pick 'y' or 'n'.\n" + Style.RESET_ALL)
            continue
        break


def vegan_food():
    """
    A function for vegan options/menu
    """
    print(Fore.BLUE + "Great! Here's our vegan options;" + Style.RESET_ALL)
    list_vegan_dishes = enumerate(vegan_dishes)

    for vegan_dish in list_vegan_dishes: #A loop to generate a vegan menu
        print(vegan_dish)

    while True:
        try:
            vegan_number = input(Fore.GREEN + "Choose a number:\n" + Style.RESET_ALL)
            vegan_number = int(vegan_number)
            if type(vegan_number) == int:
                if vegan_number >= 5: #A check so the user can't pick outside the list
                    print(Fore.RED + f"You picked: '{vegan_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE + 
                        f"You choose '{vegan_dishes[vegan_number]}'. Great choice!\n" + Style.RESET_ALL)
                    user_choices.append(vegan_dishes[vegan_number])
                    for item in user_choices: #Returns the user choice to global
                        break
        except ValueError:
            print(Fore.RED + f"You typed: '{vegan_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n" + Style.RESET_ALL)
            continue
        break

    return vegan_number


def meat_food():
    """
    A function for non vegan options/menu
    """
    print(Fore.BLUE + "Great! Here's our meat options;" + Style.RESET_ALL)
    list_meat_dishes = enumerate(meat_dishes)

    for meat_dish in list_meat_dishes: #A loop to generate a non vegan menu
        print(meat_dish)

    while True:
        try:
            meat_number = input(Fore.GREEN + "Choose a number:\n" + Style.RESET_ALL)
            meat_number = int(meat_number)
            if type(meat_number) == int:
                if meat_number >= 5: #A check so the user can't pick outside the list
                    print(Fore.RED + f"You picked: '{meat_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE + 
                        f"You choose '{meat_dishes[meat_number]}'. Great choice!\n" + Style.RESET_ALL)
                    user_choices.append(meat_dishes[meat_number])
                    for item in user_choices: #Returns the user choice to global
                        break
        except ValueError:
            print(Fore.RED + f"You typed: '{meat_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n" + Style.RESET_ALL)
            continue
        break

    return meat_number


def second_round():
    """
    A function to let the user order a second drink for dessert
    """
    print(Fore.BLUE + "How about another drink for dessert?")
    print("Would you like to see our drinks menu again?")
    print("Press 'y' to see our drinks menu")
    print("or 'n' to move onto the dessert menu" + Style.RESET_ALL)

    while True:
        second_drink = input(Fore.GREEN + "Please enter y or n.\n" + Style.RESET_ALL)
        if second_drink == "y":
            order_drink(drinks)
        elif second_drink == "n":
            break
        else:
            print(Fore.RED + f"you picked '{second_drink}'.")
            print("please pick 'y' or 'n'.\n" + Style.RESET_ALL)
            continue
        break


def order_dessert():
    """
    A function that allows the user to order a dessert
    Similar to the first function allowing the user to select a vegan option
    """
    print(Fore.BLUE + "We shall go onto our dessert menu now")
    print("Would you like to see the vegan menu?" + Style.RESET_ALL)

    while True:
        vegan = input(Fore.GREEN + "Please enter y or n.\n" + Style.RESET_ALL)
        if vegan == "y":
            vegan_dessert() #Runs a vegan dessert menu
        elif vegan == "n":
            milk_dessert() #Runs a non vegan dessert menu
            break
        else:
            print(Fore.RED + f"you picked '{vegan}'.")
            print("please pick 'y' or 'n'.\n" + Style.RESET_ALL)
            continue
        break


def milk_dessert():
    """
    A function for non vegan desserts
    """
    print(Fore.BLUE + "Great! Here's our non vegan desserts;" + Style.RESET_ALL)
    list_desserts = enumerate(desserts)

    for dessert in list_desserts: #A loop to generate a non vegan dessert menu
        print(dessert)

    while True:
        try:
            dessert_number = input(Fore.GREEN + "Choose a number:\n" + Style.RESET_ALL)
            dessert_number = int(dessert_number)
            if type(dessert_number) == int:
                if dessert_number >= 3: #A check so the user can't pick outside the list
                    print(Fore.RED + f"You picked: '{dessert_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE + 
                        f"You choose '{desserts[dessert_number]}'. Great choice!\n" + Style.RESET_ALL)
                    user_choices.append(desserts[dessert_number])
                    for item in user_choices: #Returns the user choice to global
                        break
        except ValueError:
            print(Fore.RED + f"You typed: '{dessert_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n" + Style.RESET_ALL)
            continue
        break

    return dessert_number


def vegan_dessert():
    """
    A function for vegan desserts
    """
    print(Fore.BLUE + "Great! Here's our vegan desserts;" + Style.RESET_ALL)
    list_vegan_desserts = enumerate(vegan_desserts)

    for vegan_dessert in list_vegan_desserts: #A loop to generate a vegan dessert menu
        print(vegan_dessert)

    while True:
        try:
            dessert_number = input(Fore.GREEN + "Choose a number:\n" + Style.RESET_ALL)
            dessert_number = int(dessert_number)
            if type(dessert_number) == int:
                if dessert_number >= 3: #A check so the user can't pick outside the list
                    print(Fore.RED + f"You picked: '{dessert_number}'.")
                    print("Sorry that number isnt on the list.")
                    print("Please pick another number.\n" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.BLUE + 
                        f"You choose '{vegan_desserts[dessert_number]}'. Great choice!\n" + Style.RESET_ALL)
                    user_choices.append(vegan_desserts[dessert_number])
                    for item in user_choices: #Returns the user choice to global
                        break
        except ValueError:
            print(Fore.RED + f"You typed: '{dessert_number}'.")
            print("That is not a number.")
            print("Please pick a number on the list.\n" + Style.RESET_ALL)
            continue
        break

    return dessert_number


def song_request():
    """
    A function to allow the user to request a song
    """
    print(Fore.BLUE + "Do you have any song requests?")
    print("Due to our large number of requests we will try our best to play as many as we can" + Style.RESET_ALL)

    song = input(Fore.GREEN + "Choose any song you'd like;\n" + Style.RESET_ALL)

    print(Fore.BLUE + f"You have selected '{song}' Great song choice!\n" + Style.RESET_ALL)


def results():
    """
    A final review of all the selected options from the user
    """
    print(Fore.BLUE + "To sum up - you have selected;" + Style.RESET_ALL)
    print(Fore.GREEN + "[{0}]".format(', '.join(map(str, user_choices))) + Style.RESET_ALL) #Prints the users picks without the quotes
    print(Fore.BLUE + "Great choices!")
    print("Go into the wedding hall and enjoy the night!")
    print("We hope you have the best time!")
    print("Thanks for using our automated system!")
    print("If you have any ideas for improvements")
    print("Talk to Jordan Finlay in the wedding hall")
    print("He's in the black suit and probably dancing poorly")
    print("Thanks for coming!" + Style.RESET_ALL)


def main():
    """
    A function to run all program functions
    """
    enter_name()
    order_drink(drinks)
    order_food()
    second_round()
    order_dessert()
    song_request()
    results()


main()