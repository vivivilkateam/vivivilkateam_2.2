import tkinter
class Units:
    def __init__(self, x, y, hp, speed, damage):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.damage = damage
    def __str__(self):
        return (f'координаты: x = {self.x}, y = {self.y}, '
                f'здоровье: {self.hp}, Скорость: {self.speed}, Урон: {self.damage}')
class game_player(Units):
    def __init__(self, x, y, hp, speed, damage, shield, armor, weapons, xp):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.shield = shield
        self.armor = armor
        self.weapons = weapons
        self.xp = xp

    def __str__(self):
        return (f'координаты: x = {self.x}, y = {self.y}, '
                    f'здоровье: {self.hp}, Скорость: {self.speed}, Урон: {self.damage},'
                f' Защита:{self.shield}, Броня:{self.armor}, Оружие:{self.weapons}, Опыт:{self.xp}')
class game_enemy(Units):
    def __init__(self, x, y, hp, speed, damage, shield, drope_xp,inventory_loot):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.shield = shield
        self.xp = drope_xp
        self.loot = inventory_loot

    def __str__(self):
        return (f'координаты: x = {self.x}, y = {self.y}, '
                    f'здоровье: {self.hp}, Скорость: {self.speed}, Урон: {self.damage},'
                f' Защита:{self.shield}, Выпадаемый опыт:{self.xp}, Лут:{self.loot}')