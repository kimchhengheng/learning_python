import json
import re
from difflib import get_close_matches

# get the input of what want to search ignore the case
# return it
# closer word supermann fruti

# open the file and store to data
import sys

data = json.load(open('data.json'))


def get_the_answer(want):
    if want in data:
        return data[want]

    elif want.upper() in data:
        return data[want.upper()]

    elif want.title() in data:
        return data[want.title()]
        # the closest match can have or not so check the length
    elif len(get_close_matches(want, data.keys())) > 0:
        print("did you mean %s instead" % get_close_matches(want, data.keys())[0])
        print(get_close_matches(want, data.keys()))
        decide = input("press y for yes or n for no \n")
        if decide.lower() == "y":
            # get closest match we do not consider about the upper lower
            return data[get_close_matches(want, data.keys())[0]]
        elif decide.lower() == "n":
            print("you have enter the wrong key")
        else:
            print("you have enter the wrong choice")
    else:

        print("there is no " + want + " in the dictionary")

    return


while True:
    want = input("enter the word you want to find \n").lower()
    while re.search('[@_!#$%^&*()<>?/}{~:|0-9]', want):
        print("your word you enter contain special character which is not available")
        want = input("enter the world you want to find \n").lower()
    # we make it lower first since they can screw up by input word in messy case like TaMil

    out = get_the_answer(want)
    if out is not None:
        for var in out:
            print(var)


    repeat = input("Do you want to find any other word? press enter to continue else system will stop \n")
    if repeat != "":
        sys.exit(0)
