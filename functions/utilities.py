#!/usr/bin/env python3

""" utilities.py provides general purpose utilities used by MixScraper.
"""


# Defining utility functions
def assertion(entry, message):
    """ assertion                   Asserts if the input entered by the user is correct.
        ----------------------------------------------------------------------------------------------------------------
        Variable(s)
            entry                   The string entered by the user.
            message                 A string message to be displayed to the user.

        Output(s)
                                    Returns true or false based on the users assertion.
        ================================================================================================================
    """

    while True:
        user_input = input(f"{message}: '{entry}'. Is this correct? (y/n)")
        if user_input.upper() == "Y":
            return True
        elif user_input.upper() == "N":
            return False
        else:
            print(f"I'm sorry, but {user_input} is not a valid input. Please try again.")
            continue

if __name__ == "__main__":
    pass
