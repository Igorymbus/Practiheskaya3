import time
import random

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


monsters = [
    {"name": "Flowey", "hp": 50, "attack": 10},
    {"name": "Toriel", "hp": 100, "attack": 15},
    {"name": "Sans", "hp": 200, "attack": 20},
]


def choose_monster():
    return random.choice(monsters)


def start_battle(player_name):
    print(f"Вы встречаете монстра! Бой начинается!")
    monster = choose_monster()
    print(f"{monster['name']} появляется перед вами.")

    while monster["hp"] > 0:
        print(f"{monster['name']} (HP: {monster['hp']})")
        action = input("Выберите действие (атаковать/убежать): ").lower()

        if action == "атаковать":
            player_attack = random.randint(5, 20)
            monster["hp"] -= player_attack
            print(f"Вы атакуете {monster['name']} и наносите {player_attack} урона!")
            if monster["hp"] <= 0:
                print(f"{monster['name']} погиб!")
                break

            monster_attack = random.randint(5, 15)
            print(f"{monster['name']} атакует вас и наносит {monster_attack} урона!")
        elif action == "убежать":
            print(f"Вы пытаетесь убежать от {monster['name']}!")
            if random.random() < 0.5:
                print("Вы убежали успешно!")
                break
            else:
                print(f"{monster['name']} не позволил вам убежать!")
                monster_attack = random.randint(5, 15)
                print(f"{monster['name']} атакует вас и наносит {monster_attack} урона!")
        else:
            print("Неверное действие. Попробуйте еще раз.")


def main():
    player_name = input("Введите имя вашего персонажа: ")
    print(f"Добро пожаловать, {player_name}!")
    while True:
        action = input("Что вы хотите сделать (начать бой/выйти из игры): ").lower()
        if action == "начать бой":
            start_battle(player_name)
        elif action == "выйти из игры":
            print("Спасибо за игру!")
            break
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()