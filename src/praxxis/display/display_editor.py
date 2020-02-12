"""
This file contains all of the display functions for editors
"""


def display_list_editors(editors):
    """display function for listing editors"""
    print("Editors:")
    i = 0
    library = ""
    for editor in editors:
        i+=1
        print("\t%s.\t%s"  %(i, editor))
