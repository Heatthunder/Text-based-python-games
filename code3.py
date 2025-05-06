import random

#buff and debuff classes based on class and strength
class knight:
    def __init__(self, health):
        self.health = health
    defenses={
            "block":-2
    }
    attacks={
            "punch":3,
            "kick":4.5,
            "slap":2.5,
            "shield bash":5
            # "taunt":1
            # "distract":1
    }
    def create_damage(self, action):
        damage = self.defenses.get(action)
        if damage == None:
            damage = self.attacks.get(action)
        if damage == None:
            print("unreconized action")
        else:
            return damage
    def recive_damage(self, receive, reduce):
        actual_damage = receive + reduce
        if actual_damage < 0:
            actual_damage = 0
        self.health = self.health - actual_damage

class wizard:
    def __init__(self, health):
        self.health = health
    defenses={
            "heal":-2
    }
    attacks={
            "punch":2.5,
            "kick":3,
            "slap":1.5,
            "fireball":6
            # "taunt":1
            # "distract":1
    }
    def create_damage(self, action):
        damage = self.defenses.get(action)
        if damage == None:
            damage = self.attacks.get(action)
        if damage == None:
            print("unreconized action")
        else:
            return damage
    def recive_damage(self, receive, reduce):
        actual_damage = receive + reduce
        self.health = self.health - actual_damage

class archer:
    def __init__(self, health):
        self.health = health
    defenses={
            "dodge":-10
    }
    attacks={
            "punch":2.5,
            "kick":3,
            "slap":2.5,
            "volly":6.5
            # "taunt":1
            # "distract":1
        }
    def create_damage(self, action):
        damage = self.defenses.get(action)
        if damage == None:
            damage = self.attacks.get(action)
        if damage == None:
            print("unreconized action")
        else:
            return damage
    def recive_damage(self, receive, reduce):
        if reduce < 0:
            actual_damage = 0
        else:
            actual_damage = receive
        self.health = self.health - actual_damage

class player:
    name = ""
    classType = []

p1 = player()
p1.name = input("player 1 user name: ")
print(" sleect a class ")
print("===========================")
print("1. knight")
print("2. wizard")
print("3. archer")
while True:
    choice = input()
    if choice == "knight":
        p1.classType = knight(health=162)
        break
    elif choice == "wizard":
        p1.classType = wizard(health=150)
        break
    elif choice == "archer":
        p1.classType = archer(health=100)
        break
    else:
        print("class does not exist")

p2 = player()
p2.name = input("player 2 user name: ")
print(" sleect a class ")
print("===========================")
print("1. knight")
print("2. wizard")
print("3. archer")
while True:
    choice = input()
    if choice == "knight":
        p2.classType = knight(health=162)
        break
    elif choice == "wizard":
        p2.classType = wizard(health=150)
        break
    elif choice == "archer":
        p2.classType = archer(health=100)
        break
    else:
        print("class does not exist")

while p1.classType.health > 0 and p2.classType.health > 0:
    p1damage = None
    while p1damage == None:
        print("===========================")
        print("player 1's attacks")
        print("===========================")
        print(p1.classType.attacks)
        print("===========================")
        print("player 1's defenses")
        print("===========================")
        print(p1.classType.defenses)
        print("===========================")
        print(p1.classType.health)
        print("===========================")
        response = input(p1.name + " choose an attack or ability: ")
        p1damage = p1.classType.create_damage(response)
#handle p1damage = none
        print(p1damage)

    p2damage = None
    while p2damage == None:
        print("===========================")
        print("player 2's attacks")
        print("===========================")
        print(p2.classType.attacks)
        print("===========================")
        print("player 2's defenses")
        print("===========================")
        print(p2.classType.defenses)
        print("===========================")
        print(p2.classType.health)
        print("===========================")
        response = input(p2.name + " choose an attack or ability: ")
        p2damage = p2.classType.create_damage(response)
#handle p2damage = none
        print(p2damage)

#damage receiving and defending

    if p1damage > 0:
        p1attack = p1damage
        p1defense = 0
    else:
        p1attack = 0
        p1defense = p1damage

    if p2damage > 0:
        p2attack = p2damage
        p2defense = 0
    else:
        p2attack = 0
        p2defense = p2damage
    p1.classType.recive_damage(p2attack, p1defense)
    
    p2.classType.recive_damage(p1attack, p2defense)
