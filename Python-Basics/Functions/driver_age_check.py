import math

def check_driver_age(age = 0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

age = input("What is your age?: ")
if not age or not age.isnumeric():
    age = 0

check_driver_age(age)