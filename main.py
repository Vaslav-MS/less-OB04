from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")

# Можно добавить новое оружие без изменения существующего кода
class Axe(Weapon):
    def attack(self):
        print("Боец атакует топором.")

# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, monster):
        self.weapon.attack()
        monster.take_damage()

# Класс монстра
class Monster:
    def __init__(self):
        self.health = 100

    def take_damage(self):
        print("Монстр получает урон!")
        self.health = 0
        if self.health <= 0:
            print("Монстр побежден!")

# Реализация боя
if __name__ == "__main__":
    # Создаем монстра и бойца с мечом
    monster = Monster()
    fighter = Fighter(Sword())

    print("Боец выбирает меч.")
    fighter.attack(monster)

    # Боец меняет оружие на лук и атакует нового монстра
    monster = Monster()
    print("\nБоец выбирает лук.")
    fighter.change_weapon(Bow())
    fighter.attack(monster)

    # Боец меняет оружие на топор и атакует еще одного монстра
    monster = Monster()
    print("\nБоец выбирает топор.")
    fighter.change_weapon(Axe())
    fighter.attack(monster)
