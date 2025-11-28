import random

class Player:
    def __init__(self, name, health, moves, attack_func):
        self.name = name
        self.health = health
        self.moves = moves
        self.attack_func = attack_func

    def perform_move(self, move_name, enemy):
        if move_name not in self.moves:
            print("{} does not know the move {}.".format(self.name, move_name))
            return
        damage = self.moves[move_name]
        if self.attack_func:
            move_name = self.attack_func()
        print("{} uses {}!".format(self.name, move_name))
        enemy.take_damage(damage)
        print("{}'s remaining health: {}".format(self.name, self.health))

    def take_damage(self, damage):
        print("{} takes {} damage!".format(self.name, damage))
        self.health -= damage


def player_attack():
    return input("Which attack move do you want to use? ")


def player_block():
    return "block"


def player_dodge():
    return "dodge"


def bot_attack():
    return "fireball"


def bot_heal():
    return "heal"


def bot_fireball():
    return "fireball"


# Create a bot and start the game
bot_names = ["Azula", "Ozai", "Iroh", "Zuko", "Ty Lee", "Mai", "Csir bob", "Long Feng", "sir billy", "sir joe, sir billybodjoe", "sir billybob", "phill"]
bot_name = random.choice(bot_names)
bot = Player(name=bot_name, health=150, moves={
    "attack": 20,
    "block": 10,
    "dodge": 5,
    "heal": bot_heal,
    "fireball": bot_fireball
}, attack_func=bot_attack)

player_name = input("Enter your name: ")
print(" Select a class( please type the number ) :")
print("=========================================")
print("1. Knight")
print("2. Archer")
print("3. Wizard")
while True:
    try:
        choice = int(input("> "))
        if choice == 1:
            player = Player(name=player_name, health=200, moves={
                "attack": 7.5,
                "block": 5,
                "dodge": 2.5
            }, attack_func=player_attack)
            break
        elif choice == 2:
            player = Player(name=player_name, health=150, moves={
                "attack": 5,
                "block": 2,
                "dodge": 1
            }, attack_func=player_attack)
            break
        elif choice == 3:
            player = Player(name=player_name, health=100, moves={
                "attack": 6.5,
                "block": 3,
                "dodge": 2
            }, attack_func=player_attack)
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

print("Player moves:")
print("========================================")

while player.health > 0 and bot.health > 0:
    print(player.moves)
    print("========================================")
    move_name = input("What move do you want to use, {}? ".format(player.name))
    player.perform_move(move_name, enemy=bot)

    if bot.health <= 0:
        print("You defeated", bot_name)
        break

    # Bot's turn
    moves = ["attack", "block", "dodge"]
    if bot.health < 30:
        moves.append("heal")
    move_name = random.choice(moves)
    bot.perform_move(move_name, enemy=player)

    if player.health <= 0:
        print("Azula defeated you!")
        break
