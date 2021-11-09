def getNameAgeAdd():
    name_ = input("Name: ")
    age_ = int(input("Age: "))
    add_ = input("Address: ")
    return name_, age_, add_

def display(namef, agef, addf):
    print(f"Hi, my name is {namef}. I am {agef} years old and I live in {addf}.")

name, age, add = getNameAgeAdd()

display(name, age,add)