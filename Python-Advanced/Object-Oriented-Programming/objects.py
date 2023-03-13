# OOP
class PlayerCharacter:
    health = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print(f'{self.name} is running!')
    
    def talk(self):
        print('talking')


player1 = PlayerCharacter('Jess', 33)
print(player1.name + ', you are', str(player1.age) + '.')
print(f'{player1.name}, your health is at {player1.health}%')
player1.run()
