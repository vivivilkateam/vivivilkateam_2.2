import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=20, attack=5)

    def choose_action(self):
        print("\nВыберите действие:")
        print("1. Атаковать")
        print("2. Использовать предмет")
        print("3. Убежать")
        choice = input("Ваш выбор: ")
        return choice

class Monster(Character):
    def __init__(self, name):
        super().__init__(name, health=10, attack=3)

def battle(player, monster):
    while player.is_alive() and monster.is_alive():
        action = player.choose_action()

        if action == '1':  # Атаковать
            print(f"\n{player.name} атакует {monster.name}!")
            monster.health -= player.attack
            print(f"{monster.name} осталось здоровья: {monster.health}")
        elif action == '2':  # Использовать предмет
            heal_amount = random.randint(5, 10)
            player.health += heal_amount
            print(f"{player.name} использует предмет и восстанавливает {heal_amount} здоровья!")
            print(f"Текущее здоровье {player.name}: {player.health}")
        elif action == '3':  # Убежать
            print(f"{player.name} убегает от {monster.name}!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

        if monster.is_alive():
            print(f"{monster.name} атакует {player.name}!")
            player.health -= monster.attack
            print(f"{player.name} осталось здоровья: {player.health}")

    if player.is_alive():
        print(f"\n{player.name} победил {monster.name}!")
    else:
        print(f"\n{player.name} был повержен {monster.name}... Игра окончена.")

def main():
    print("Добро пожаловать в упрощенную версию Undertale!")
    player_name = input("Введите имя вашего персонажа: ")
    player = Player(player_name)
    monster = Monster("Скелет")

    print(f"\n{player.name} встретил {monster.name}!")
    battle(player, monster)

if __name__ == "__main__":
    main()