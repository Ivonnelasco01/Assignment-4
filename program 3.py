def getMoneyApple():
    money_ = int(input("How much is your money? "))
    apple_ = int(input("How much is the price of 1 apple? "))
    return money_, apple_

def getQuantity():
    quantity_ = money // apple
    return quantity_

def getTotal():
    total_ = quantity * apple
    return total_

def getChange():
    change_ = money - total
    return change_

def display(quantityf, changef):
    print(f"You can buy {quantityf} apples and your change is {changef} pesos.")

money, apple = getMoneyApple()

quantity = getQuantity()

total = getTotal()

change = getChange()

display(quantity, change)