"""

# -*- coding: utf-8 -*-
Created on          30 Jan 2019 at 3:11 PM
@author:            Arvind Sachidev Chilkoor
Created using:      PyCharm
Name of Project:    Dictionary Project

"""
import json
from difflib import get_close_matches
from sys import *

data = json.load(open("data.json"))


"""
The below code is method of converting a JSON into a PYTHON Dictionary in-order that the total number of words can be
counted and displayed for the user, just as a statistical information.
"""

dict_count = {}

"""
Using TRY EXCEPT method to identfiy any errors, if there is an error it will break and exit
"""
try:
    with open("data.json") as data_dict_file:  # opens the JSON file
        dict_count = json.load(data_dict_file)  # loads the JSON file into the previously created dictionary variable
except IOError as e:
    print(e)
    raise
    exit()


def formatted_answer(fans):
    """
    This function returns a serialized numbering for the user input, if there is more than one definition for the word.
    :param fans:        # short for formatted answer
    :return: fans       # serialized if more than one definition exists
    """
    if isinstance(fans, list):  # isinstance checks if the fans has list of definition
        for index, item in enumerate(fans,
                                     start=1):  # enumerate lists through the number of definitions for "fans", start paramater indexes from 1 instead of 0
            print("\n%d. " % index, item)  # using string formatting %d for decimal/numbers

    else:
        print("\n" + fans)


def translate(w):
    """
    This function tanslate(w) takes in the input from the user as an arguement "word" and checks for the corresponding meaning in the
    JSON file data.json and passes it to formatted_answer as an arguement for output/display
    :param w:
    :return: formatted_answer(output)
    """

    if w in data:
        print("\n")
        output = data[w]
        return formatted_answer(output)
    elif w == (int or float):
        print("\nYou have entered a number, please enter a word!")
        return
    elif w.title() in data:  # if user entered "texas", this will also check for "Texas"
        output = data[w.title()]
        return formatted_answer(output)
    elif w.upper() in data:  # if user entered USA or NATO or UN shortforms or acronyms
        output = data[w.upper()]
        return formatted_answer(output)
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input(
            "Did you mean %s instead? Please enter Y/y for Yes, or N/n for No:  " % get_close_matches(w, data.keys())[
                0])
        if ans == ("y" or "Y"):
            output = data[get_close_matches(w, data.keys())[0]]
            return formatted_answer(output)
        elif ans == ("n" or "Y"):
            return "The word does not exist, Please check the word."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist, Pls check the word"


choice = None
while True:                 # The while TRUE loop checks for input choice of 1 or q, anything else it will repeat.
    print("\n \n[1] Enter 1 to find out the meaning of a word: ")
    print("[2] Enter 'q' or 'Q' to quit: ")
    print("Statistics: The DICTIONARY file contains %d words" % len(dict_count))  # Provides statistical information of the number of words in the Dictionary Database
    choice = input("\nWhat would you like to do: ")
    if choice == '1':
        word = input("\n \nEnter the word for which you would like to know the meaning of:  ")
        translate(word)
    elif choice == ('q' or 'Q'):
        print("\n \nThank you, see you soon!")
        exit()
