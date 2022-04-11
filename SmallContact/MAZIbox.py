# The module containing the basic and most needed functions.


def mazi_text(prompt):
    """
    Displays a prompt and reads in a string of text.
    Keyboard itnerrups (Ctrl+C) are ignored.
    Returns a string containing the string input by the user.
    """
    while True:
        try:
            result = input(prompt)
            break
        except KeyboardInterrupt:
            print("Please enter text ")
    return result


def mazi_float(prompt):
    """
    Displays a prompt and reads in a number (eg. 1.001).
    Keyboard interrupt (Ctrl+C) are ignored.
    Invalid numbers are ignored.
    Returns a float containing the value input by user.
    """
    while True:
        try:
            number_text = mazi_text(prompt)
            result = float(number_text)
            break
        except ValueError:
            print("Please enter a number")
    return result


def mazi_int(prompt):
    """
    Displays a prompt and reads in a number (eg. 1).
    Keybord interrupts (Crtl+C) are ignored.
    Invalid numbers are rejected.
    Returns an integer containing the value input by the user.
    """
    while True:
        try:
            number_text = mazi_text(prompt)
            result = int(number_text)
            break
        except ValueError:
            print("Please enter a number ")
    return result


def mazi_float_ranged(prompt, min_value, max_value):
    """
    Displays a prompt and reads in a number (eg. 1.002).
    Min_value gives the inclusive minimum value.
    Max_value gives the inclusive maximum value.
    Does detect if the min and max values are wrong way round.
    Keyboard interrups(Ctrl+C) are ignored.
    Invalid numbers are rejected.
    Returns a float containing the value input by the user.
    """
    if min_value > max_value:
        raise Exception("Min value is bigger than max value. Please check the data ")
    while True:
        result = mazi_float(prompt)
        if result < min_value:
            print("The number is too low ")
            print("Minimum value is ", min_value)
            continue
        if result > max_value:
            print("The number is too high ")
            print("Maximum value is ", max_value)
            continue
        break
    return result


def mazi_int_ranged(prompt, min_value, max_value):
    """
    Displays a prompt and reads in a number (eg. 2).
    Min_value gives the inclusive minimum value.
    Max_value gives the inclusive maximium value.
    Does detect if min and max are wrong way round.
    Keyboard interrupts (Ctrl+C) are ignored.
    Invalid numbers are rejected.
    Returns an integer containing the value input by the user.
    """
    if min_value > max_value:
        raise Exception("Min value is bigger than max value. Please check the data. ")
    while True:
        result = mazi_int(prompt)
        if result < min_value:
            print("The number is too low ")
            print("Minimum value is: ", min_value)
            continue
        if result > max_value:
            print("The number is too big ")
            print("The maximium value is: ", max_value)
            continue
        break
    return result


def introduction():
    print(
        """ Welcome to the MAZIbox functions. Version 1.0.
    You can use these to read numbers and strings in your programs.
    The functions are used as fallows:
    text=mazi_text(prompt)
    float_value=mazi_float(prompt)
    int_value=mazi_int(prompt)
    float_ranged=mazi_float_ranged(prompt, min_value, max_value)
    int_ranged=mazi_int_ranged(prompt, min_value, max_value)

    Enjoy your coding.

    Mariusz Mazur aka. Mazi """
    )


if __name__ == "__main__":
    # Let MAZIbox module introduce itself
    introduction()
