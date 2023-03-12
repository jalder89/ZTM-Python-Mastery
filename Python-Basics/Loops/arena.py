# A simple arena fighting game that allows the player to set their name, class, and
# loops through a combat scenario with an enemy. The combat continues automatically until either the player or the enemy is defeated.
import random

player = {
    "name": None,
    "class": None,
    "weapon": None,
    "armor": None,
    "skills": None,
    "is_alive": True
}

weapons = {
    "iron_broadsword": {
    "name": "Iron Broadsword",
    "attk": 5,
    "mag_attk": 0
    },
    "ash_staff": {
    "name": "Ash Staff",
    "attk": 3,
    "mag_attk": 5
    }
}

armors = {
    "iron_platemail": {
    "name": "Iron Platemail",
    "def": 5,
    "mag_def": 0
    },
    "mages_cloth_robe": {
    "name": "Mages Cloth Robe",
    "def": 2,
    "mag_def": 5
    }
}

skills = {
    "cleave": {
    "name": "Cleave",
    "attk": 10,
    "mag_attk": 0,
    "target": "line"
    },
    "fireball": {
    "name": "Fireball",
    "attk": 0,
    "mag_attk": 10,
    "target": "single"
    },
    "bite": {
    "name": "Bite",
    "attk": 3,
    "mag_attk": 0,
    "target": "single"
    }
}

classes = {
    "knight": {
    "name": "Knight",
    "desc": "A strong and noble warrior out to make their mark on the world.",
    "hp": 15,
    "mp": 0,
    "attk": 7,
    "def": 7,
    "mag_attk": 0,
    "mag_def": 0,
    "dex": 3,
    "starter_weapon": weapons["iron_broadsword"],
    "starter_armor": armors["iron_platemail"],
    "starter_skill": skills["cleave"]
    },
    "mage": {
    "name": "Mage",
    "desc": "A clever mage seeking to become powerful and reknowned for their magical prowess.",
    "hp": 7,
    "mp": 15,
    "def": 2,
    "attk": 3,
    "mag_attk": 7,
    "mag_def": 5,
    "dex": 5,
    "starter_weapon": weapons["ash_staff"],
    "starter_armor": armors["mages_cloth_robe"],
    "starter_skill": skills["fireball"]
    }
}

enemies = {
    "wolf": {
    "name": "Wolf",
    "hp": 7,
    "attk": 3,
    "def": 2,
    "dex": 7,
    "skill": skills["bite"],
    "is_alive": True
    }
}

print("\nHello player, welcome to the arena!\n")

player["name"] = input("What is your name? ")
print(f'\nYour name is {player.get("name")}, wonderful! We have a great experience waiting for you!')


player["class"] = classes.get(input("\nWhat is your class, Knight or Mage? ").lower())
player["weapon"] = player["class"].get("starter_weapon")
player["armor"] = player["class"].get("starter_armor")
player["skills"] = [player["class"].get("starter_skill")]

print(f'\n Ah, A knight! {player["class"].get("desc")} You will do well as a {player["class"].get("name")}!')
print("\nEntering the arena...")

print(f'\nWelcome, {player["class"].get("name")}!\n')
input("This is the arena, press enter when you are ready for your first fight!")
enemy = enemies["wolf"]

print(f'A wild {enemy.get("name")} appeared!')
is_fighting = True

while is_fighting:
    attack_damage = 0

    if random.randint(0, player["class"].get("dex")) >= random.randint(0, enemy["dex"]):
        print(f"Player attacks with {player['skills'][0].get('name')}")
        attack_damage = random.randint(1, player["skills"][0].get("attk") + player["skills"][0].get("mag_attk"))
        enemy["hp"] -= attack_damage
        print(f"You did {attack_damage} damage!")
        if enemy["hp"] <= 0:
            enemy["is_alive"] = False
        else:
            print(f"{enemy['name']} attacks the player with {enemy['skill'].get('name')}!")
            attack_damage = random.randint(1, enemy["skill"].get("attk") + enemy["skill"].get("mag_attk"))
            player["class"]["hp"] -= attack_damage
            print(f"The {enemy['name']} did {attack_damage} damage!")
            if player["class"].get("hp") <= 0:
                player["is_alive"] = False
    else:
        print(f"{enemy['name']} attacks the player with {enemy['skill'].get('name')}!")
        attack_damage = random.randint(1, enemy["skill"].get("attk") + enemy["skill"].get("mag_attk"))
        player["class"]["hp"] -= attack_damage
        print(f"The {enemy['name']} did {attack_damage} damage!")
        if player["class"].get("hp") <= 0:
            player["is_alive"] = False
        else:
            print(f"Player attacks with {player['skills'][0].get('name')}")
            attack_damage = random.randint(1, player["skills"][0].get("attk") + player["skills"][0].get("mag_attk"))
            enemy["hp"] -= attack_damage
            print(f"You did {attack_damage} damage!")
    
    if not player["is_alive"]:
        print("\nYou have died!")
        is_fighting = False
    elif not enemy["is_alive"]:
        print("You've won!")
        is_fighting = False