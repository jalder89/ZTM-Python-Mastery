# OOP
class Character:
    health = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print(f'{self.name} is running!')
    
    def talk(self):
        print('talking')
    
    def attack(self, target):
        print(f'{self.name} attacks for {self.power} damage!')
        target.health -= self.power
        print(f'{target.name}\'s health is now {target.health}%')


class Player(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.power = 7


class Enemy(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.power = 5
    
    


player1 = Player('Jess', 33)
print(player1.name + ', you are', str(player1.age) + '.')
print(f'{player1.name}, your health is at {player1.health}%')
player1.run()

enemy1 = Enemy('Grognar', 37)
print(enemy1.health)
print(enemy1.name)
enemy1.attack(player1)
player1.attack(enemy1)
enemy1.run()
