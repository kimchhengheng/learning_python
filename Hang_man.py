"""
your have 10 attempt
if you guest wrong draw the man
guess right it fill in the
check function then if it is not call decrease the value can call the figure
figure can do if else but waste
"""
import random

words = ["pugger", "littlepugger","tiger", "superman", "thor", "pokemon","avengers"]

def display():
    print("Guest the word: {}".format("".join(correct)))


def check(charinput):
    global avail
    global correct
    if charinput not in word:
        avail -= 1
    else:
        for var in range(len(word)):
            if charinput == word[var]:
               correct[var] = charinput

def figure():
    print("{} turns are left".format(avail))
    if avail == 9:
        print("----------")
    elif avail == 8:
        print("----------")
        print("    O     ")
    elif avail == 7:
        print("----------")
        print("    O     ")
        print("    |     ")
    elif avail == 6:
        print("----------")
        print("    O     ")
        print("    |     ")
        print("   /      ")
    elif avail == 5:
        print("----------")
        print("    O     ")
        print("    |     ")
        print("   / \    ")
    elif avail == 4:
        print("----------")
        print("   \O     ")
        print("    |     ")
        print("   / \    ")
    elif avail == 3:
        print("----------")
        print("   \O/    ")
        print("    |     ")
        print("   / \    ")
    elif avail == 2:
        print("----------")
        print("   \O/ |  ")
        print("    |     ")
        print("   / \    ")
    elif avail == 1:
        print("it is your last chance")
        print("----------")
        print("   \O_|/  ")
        print("    |     ")
        print("   / \    ")
    elif avail == 0:
        print("it is your last chance")
        print("----------")
        print("    O_|  ")
        print("   /|\    ")
        print("   / \    ")


name = input("Enter your name \n").lower()
print("Welcome " + name.title())
print("-------")
avail = 10
print("Try to guess the word in less than {} attempts".format(avail))
#word = list(words[random.randint(0, len(words)-1)])
word = list(random.choice(words))
#word = list(name)
correct = []
choosen = []
for var in word:
    correct.append("-")
# while loop until no more avail

while True:
    display()
    inval = input().lower()
    if len(inval) == 1:
        if inval in choosen:
            print("you already chosed that character")
        else:
            choosen.append(inval)
        print("your choosen char are {}".format(" , ".join(choosen)))
        check(inval)
        figure()
        if avail == 0:
            print("You have losed the game the word is ", "".join(word))
            break
        if "-" not in correct:
            print("Congratulation you got the word")
            break
    else:
        print("you can choose only one char at a time")
"""
we have to define the function first before we call it

        elif avail ==0 & "-" in correct:
        print("lose")

"""
