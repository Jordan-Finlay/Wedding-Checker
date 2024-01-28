def enter_name():
    """
    Asks user to input name to check he/she is on the wedding list
    """
    while True:
        print("Please enter your name")

        name_str = input("Enter your name here.\n")

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
        
    else:
        return True


def main():
    """
    Runs all program functions
    """
    enter_name()

main()