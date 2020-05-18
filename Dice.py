"""
the dice
generate number from 1 t0 6
enter to roll

"""
import random
import sys



def display(num):
    if num == 1:
        dice_1()
    elif num == 2:
        dice_2()
    elif num == 3:
        dice_3()
    elif num == 4:
        dice_4()
    elif num == 5:
        dice_5()
    else:
        dice_6()


def dice_1():
    print("[-----------]")
    print("[           ]")
    print("[     o     ]")
    print("[           ]")
    print("[-----------]")


def dice_2():
    print("[-----------]")
    print("[         o ]")
    print("[           ]")
    print("[ o         ]")
    print("[-----------]")


def dice_3():
    print("[-----------]")
    print("[         o ]")
    print("[     o     ]")
    print("[ o         ]")
    print("[-----------]")


def dice_4():
    print("[-----------]")
    print("[ o       o ]")
    print("[           ]")
    print("[ o       o ]")
    print("[-----------]")


def dice_5():
    print("[-----------]")
    print("[ o       o ]")
    print("[     o     ]")
    print("[ o       0 ]")
    print("[-----------]")


def dice_6():
    print("[-----------]")
    print("[ o       o ]")
    print("[ o       o ]")
    print("[ o       o ]")
    print("[-----------]")


while True:
    num = random.randint(1, 6)
    display(num)
    repeat = input("Press y to roll again ")
    while repeat.lower() != "y":
        if repeat.lower() == "n":
            sys.exit()
        repeat = input("Press y to roll again ")

    # listener is working beter
