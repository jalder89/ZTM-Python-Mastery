#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
salem = Cat('Salem', 3)
meowser = Cat('Meowser', 2)
pip = Cat('Pip', 4)

# 2 Create a function that finds the oldest cat
def findOldest(*cat_ages):
    return max(cat_ages)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {findOldest(salem.age, meowser.age, pip.age)} years old.')