import random


class Hero:
    def __init__(self, name, health, armor, strength, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.strength = strength
        self.weapon = weapon
    
    def print_info(self):
        print('Имя:', self.name)
        print('Здоровье:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.strength)
        print('Оружие:', self.weapon)

    def strike(self, hero):
        hero.health -= self.strength
        print(hero.name, 'получил урон', self.strength)
        print('Его здоровье:', hero.health)

knight = Hero('Добрыня', 120, 60, 25, 'меч')
knight.print_info()
bandit = Hero('Соловей Разбойник', 200, 15, 8, 'лук')
bandit.print_info()
dragon = Hero('Змей Горыныч', 300, 40, 30, 'Огонь')
dragon.print_info()



while knight.health > 0 and bandit.health >0 and dragon.health > 0:
    number = random.randint(1, 3)
    if number == 1:
        knight.strike(bandit)
        knight.strike(dragon)
    if number == 2:
        bandit.strike(knight)
        bandit.strike(dragon)
    if number == 3:
        dragon.strike(knight)
        dragon.strike(bandit)


if knight.health > bandit.health and knight.health > dragon.health:
    print(knight.name, 'победил!')
if dragon.health > bandit.health and dragon.health > knight.health:
    print(dragon.name, 'победил!')
if bandit.health > knight.health and bandit.health > dragon.health:
    print(bandit.name, 'победил!')


