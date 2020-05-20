"""
monthly payment depend on the interest and number
loan amount
interest rate 5 % 10 %
number of payment
"""

loan = input("please enter the loan amount that you want? \n")
while True:
    try:
        loan = float(loan)
        break
    except ValueError:
        loan = input("make sure you input the number. Please re-enter the loan amount that you want? \n")
choice = input("please enter the interest you want \n")
while True:
    try:
        interest = float(choice)
        break
    except ValueError:

        interest = input("make sure you input the number. Please re-enter the  that you want? \n")
while True:
    try:
        number = input("please enter the number of payments \n")
        number = int(number)
        break
    except ValueError:
        number = input("Make sure you enter number and no decimal, please re-enter the number of payments \n")

interest = interest / 100
monthly = "{:.2f}".format((loan * (interest * (1 + interest) * number)) / ((1 + interest) * number - 1))
print("your monthly playment with {} loan and interest {} and {} number of payment is {}".format(loan, interest, number,
                                                                                                 monthly))