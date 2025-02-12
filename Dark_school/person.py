import tkinter
import random

class Units:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def __str__(self):
        return (f'координаты: x={self.x}, y={self.y}, '
                f'Скорость: {self.speed}')


class game_player(Units):
    def __init__(self, world, start_x, texture_path, speed, lerp_speed, world_width): #Добавили world_width
        super().__init__(0, 0, speed)
        self.world = world
        self.x = start_x  # дробная координата
        self.target_x = start_x # целевая позиция
        self.texture_path = texture_path
        self.dx = 0
        self.lerp_speed = lerp_speed
        self.world_width = world_width # Добавили ширину мира


    def move_left(self):
        self.dx = -1

    def move_right(self):
        self.dx = 1

    def stop(self):
        self.dx = 0

    def update(self):
        self.target_x += self.dx * self.speed
        # Изменили ограничение на world_width
        self.target_x = max(0, min(self.target_x, self.world_width))
        self.x += (self.target_x - self.x) * self.lerp_speed


    def __str__(self):
        return f'Позиция на линии: {self.x}'

class game_enemy(Units):
    def __init__(self, x, y, health, speed, damage, shield, drope_xp, inventory_loot):
        super().__init__(x, y, speed)
        self.health = health
        self.damage = damage
        self.shield = shield
        self.xp = drope_xp
        self.loot = inventory_loot
        self.vx = 0
        self.vy = 0
        self.dx = 0
        self.dy = 0
        if self.x < 0:
            self.x = 0
        self.y= 0
    def fire(self):
        pass
    def forvard(self):
        self.vx = 0
        self.vy = -1
    def backward(self):
        self.vx = 0
        self.vy = 1
    def left(self):
        self.vx = -1
        self.vy = 0
    def right(self):
        self.vx = 1
        self.vy = 0
    def stop(self):
        self.vx = 0
        self.vy = 0
        self.__undo_move()
    def update(self):
        self.dx = self.vx * self.speed
        self.dy = self.vy * self.speed
        self.x += self.dx
        self.y += self.dy
    def __undo_move(self):
        if self.dx==0 and self.dy==0:
            return
        self.x-=self.dx
        self.y-=self.dy
        self.dx=0
        self.dy=0
    def __str__(self):
        return (f'координаты: x={self.x}, y={self.y}, '
                    f'здоровье: {self.health}, Скорость: {self.speed}, Урон: {self.damage},'
                f' Защита:{self.shield}, Выпадаемый опыт:{self.xp}, Лут:{self.loot}')