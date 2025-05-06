import random

class Player:
    def __init__(self, name, health, moves, attack_func):
        self.name = name
        self.health = health
        self.moves = moves
        self.attack_func = attack_func

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
bot_names = ["Azula", "Ozai", "Iroh", "Zuko", "Ty Lee", "Mai", "sir bob", "Long Feng", "sir billy", "sir joe, sir billybodjoe", "sir billybob", "phill"]
bot_name = random.choice(bot_names)
bot = Player(name=bot_name, health=150, moves={
    "attack": 20,
    "block": 10,
    "dodge": 5,
    "heal": bot_heal,
    "fireball": bot_fireball
}, attack_func=bot_attack)

player_name = input("Enter your name: ")
print("Select a class (please type the number):")
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

# Add a difficulty system that increases the bot's health and damage based on the player's choice
difficulty = None
while difficulty not in ["easy", "medium", "hard", "insane"]:
    difficulty = input("Select a difficulty (easy, medium, hard, insane): ").lower()
    if difficulty == "easy":
        bot_health = 100
        bot_moves = {
            "attack": 5,
            "block": 3.5,
            "dodge": 1.5,
            "heal": bot_heal,
            "fireball": bot_fireball
        }
    elif difficulty == "medium":
        bot_health = 150
        bot_moves = {
            "attack": 6,
            "block": 4.5,
            "dodge": 2.5,
            "heal": bot_heal,
            "fireball": bot_fireball
        }
    elif difficulty == "hard":
        bot_health = 200
        bot_moves = {
            "attack": 7.5,
            "block": 5,
            "dodge": 3.5,
            "heal": bot_heal,
            "fireball": bot_fireball
        }
    elif difficulty == "insane":
        bot_health = 250
        bot_moves = {
            "attack": 10,
            "block": 6.5,
            "dodge": 5,
            "heal": bot_heal,
            "fireball": bot_fireball
        }
    else:
        print("Invalid choice.")

bot = Player(name=bot_name, health=bot_health, moves=bot_moves, attack_func=bot_attack)

while player.health > 0 and bot.health > 0:
    print(player.moves)
    print("========================================")
    move_name = input("What move do you want to use, {}? ".format(player.name))
    
    player.perform_move(move_name, enemy=bot)

    if bot.health <= 0:
        print(f"You defeated {bot.name}!")
        break

    # Bot's turn
    moves = ["attack", "block", "dodge"]
    if bot.health < 30:
        moves.append("heal")
    move_name = random.choice(moves)
    bot.perform_move(move_name, enemy=player)

    if player.health <= 0:
        print(f"{bot.name} defeated you!")
        break
