import random
import json

# Player class to manage stats and inventory
class Player:
    def __init__(self, name, health=100, attack=10, defense=5, inventory=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory if inventory else []

    def show_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\n")

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory
        }

    @staticmethod
    def from_dict(data):
        return Player(
            name=data["name"],
            health=data["health"],
            attack=data["attack"],
            defense=data["defense"],
            inventory=data["inventory"]
        )

# Enemy class for combat encounters
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

# Function for combat
def combat(player, enemy):
    print(f"\nA wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == 'a':
            # Player attacks enemy
            damage = max(1, player.attack - random.randint(0, 5))
            enemy.health -= damage
            print(f"You hit the {enemy.name} for {damage} damage.")

            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                return True

            # Enemy attacks player
            damage = max(1, enemy.attack - player.defense)
            player.health -= damage
            print(f"The {enemy.name} hits you for {damage} damage.")
        elif action == 'r':
            print("You run away safely!")
            return False

    if player.health <= 0:
        print("You have been defeated!")
        return False

# Exploration function
def explore(player):
    print("\nExploring...")
    event = random.choice(['enemy', 'treasure', 'nothing'])

    if event == 'enemy':
        enemy = Enemy("Goblin", 30, 5)
        combat(player, enemy)
    elif event == 'treasure':
        item = random.choice(['Health Potion', 'Sword', 'Shield'])
        player.inventory.append(item)
        print(f"You found a {item}!")
        if item == 'Health Potion':
            player.health += 20
        elif item == 'Sword':
            player.attack += 5
        elif item == 'Shield':
            player.defense += 3
    else:
        print("You found nothing of interest.")

# Save game function
def save_game(player):
    with open("savegame.json", "w") as f:
        json.dump(player.to_dict(), f)
    print("Game saved successfully!")

# Load game function
def load_game():
    try:
        with open("savegame.json", "r") as f:
            data = json.load(f)
            print("Game loaded successfully!")
            return Player.from_dict(data)
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None

# Game loop
def main():
    print("Welcome to the Text Adventure Game!")
    player = load_game()

    if not player:
        name = input("Enter your character's name: ")
        player = Player(name)

    while player.health > 0:
        player.show_stats()
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check Stats")
        print("3. Save Game")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            explore(player)
        elif choice == '2':
            player.show_stats()
        elif choice == '3':
            save_game(player)
        elif choice == '4':
            print("Thanks for playing!")
            save_game(player)
            break
        else:
            print("Invalid choice. Please try again.")

    if player.health <= 0:
        print("Game Over! Better luck next time.")

if __name__ == "__main__":
    main()
