def getAppleOrange():
    apple_ = int(input("How many apples will you buy? "))
    orange_ = int(input("How many orange will you buy? "))
    return apple_, orange_

def getPrctotal():
    applePrc_ = apple * 20
    orangePrc_ = orange * 25
    return applePrc_, orangePrc_,

def display(totalf):
    print(f"The total amount is {totalf} pesos.")

def gettotal():
    _total = applePrc + orangePrc
    return _total

def display(totalf):
    print(f"The total amount is {totalf} pesos.")

apple, orange = getAppleOrange()

applePrc, orangePrc, = getPrctotal()

total = gettotal()

display(total)