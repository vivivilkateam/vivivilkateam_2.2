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
