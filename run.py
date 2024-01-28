def enter_name():
    """
    Asks user to input name to check he/she is on the wedding list
    """

    print("Please enter your name")

    name_str = input("Enter your name here.\n")

    print(f"name provided is {name_str}")
    
    validate_name(name_str)


def validate_name(name_str):
    """
    This is used to check the name inputted is correct,
    Making sure there are only letters
    """
    try:
        if len(name_str) == 1:
            raise ValueError(
                f"Name is too short"
            )
    except ValueError as e:
        print(f"Invalid Name: {e}, please try again.\n")

enter_name()
