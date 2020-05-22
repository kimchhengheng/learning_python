import datetime
# datetime module class date method today
import sys

currentDate = datetime.date.today() # this is date object already
while True:
    while True:
        try:
            userInput = input("enter the dateline date, mm/dd/yyyy \n")
            # datetime.dateime.strp .date mean that we interest only in date but time is 0:00:00 it is type of datetime or datetime delta
            # .days mean only day
            # when we make the different is become int type
            deadline = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
            diff = (deadline- currentDate).days
            if diff>0:
                break
            else:
                print("make sure your deadline is ahead current day, the current day is {}".format(currentDate))
        except ValueError:
            print("make sure the input date is in the correct format")
    month =int(diff/30)
    day = diff % 30
    print("you have {} monthes and {} days left from the dateline".format(month, day))
    while True:
        repeat = input("do you want to repeat it again(y/n) \n")
        if repeat == "y":
            break
        elif repeat =="n":
            sys.exit(0)
        print("please check your input again")
"""
    if repeat == "n":
        break
"""