import tkinter as tk
import random

# --- Константы и настройки ---
WORLD_LENGTH = 20
PLAYER_START_POSITION = 5
PLAYER_SPEED = 1  # Целые значения для простоты
SCREEN_WIDTH = 600
TILE_SIZE = 30  # Предположим, что все плитки имеют одинаковый размер

# --- Создание окна Tkinter ---
window = tk.Tk()
window.title("Простая левая граница")

# --- Холст ---
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=100, bg="lightblue")
canvas.pack()

# --- Позиция игрока (целые значения) ---
player_x = PLAYER_START_POSITION

# --- Функция для отрисовки ---
def draw_world():
    canvas.delete("all")
    # Отрисовка игрока (просто прямоугольник)
    x = player_x * TILE_SIZE
    canvas.create_rectangle(x, 20, x + TILE_SIZE, 50, fill="red")

# --- Движение ---
def move_left(event):
    global player_x
    player_x = max(0, player_x - PLAYER_SPEED) # Ограничение слева
    draw_world()

def move_right(event):
    global player_x
    player_x = min(WORLD_LENGTH - 1, player_x + PLAYER_SPEED) #Ограничение справа
    draw_world()

# --- Привязка клавиш ---
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

# --- Начальная отрисовка ---
draw_world()

# --- Запуск ---
window.mainloop()