import person
import world
import tkinter as tk
import random

# --- Константы и настройки ---
WORLD_LENGTH = 20
PLAYER_START_POSITION = 5
PLAYER_SPEED = 0.1
PLAYER_TEXTURE = "player.png"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 200
LERP_SPEED = 0.1
CAMERA_SPEED = 0.3  # Увеличиваем скорость камеры

# --- Текстуры мира (словарь: имя -> путь к файлу) ---
AVAILABLE_LOCATIONS = {
    "forest": "tree.png",
    "grass": "grass.png",
    "mountain": "mountain.png",
    "water": "water.png",
    "house": "house.png",
}

# --- Инициализация мира ---
world_instance = world.World(WORLD_LENGTH, AVAILABLE_LOCATIONS)

# --- Создание окна Tkinter ---
window = tk.Tk()
window.title("Правая граница + размер персонажа")

# --- Загрузка изображений ---
tile_images = {}
max_tile_width = 0
max_tile_height = 0

for name, path in AVAILABLE_LOCATIONS.items():
    try:
        image = tk.PhotoImage(file=path)
        tile_images[name] = image
        max_tile_width = max(max_tile_width, image.width())
        max_tile_height = max(max_tile_height, image.height())
    except Exception as e:
        print(f"Ошибка загрузки изображения {path}: {e}")
        tile_images[name] = None

try:
    player_image = tk.PhotoImage(file=PLAYER_TEXTURE)
    player_width = player_image.width()
    player_height = player_image.height()
except Exception as e:
    print(f"Ошибка загрузки изображения персонажа {PLAYER_TEXTURE}: {e}")
    player_image = None
    player_width = 0
    player_height = 0

# --- Размеры Canvas ---
canvas_width = SCREEN_WIDTH
canvas_height = max_tile_height

# --- Создание холста (Canvas) ---
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="lightblue")
canvas.pack()

# --- Смещение камеры ---
camera_x = 0

# --- Функция для обновления смещения камеры ---
def update_camera():
    global camera_x
    camera_target_x = pl1.x * max_tile_width - SCREEN_WIDTH / 2
    camera_x += (camera_target_x - camera_x) * 0.1
    camera_x = max(0, min(camera_x, world_instance.length * max_tile_width - SCREEN_WIDTH))
# --- Функция для отрисовки мира и персонажа ---
def draw_world():
    canvas.delete("all")
    update_camera()

    # Отрисовка мира
    for x in range(WORLD_LENGTH):
        texture_path = world_instance.get_tile(x)
        x1 = x * max_tile_width - camera_x
        y1 = 0
        tile_name = next((name for name, path in AVAILABLE_LOCATIONS.items() if path == texture_path), None)

        if x1 + max_tile_width > 0 and x1 < SCREEN_WIDTH:
            if tile_name and tile_images[tile_name]:
                canvas.create_image(x1, y1, image=tile_images[tile_name], anchor="nw", tags="tile")
            else:
                canvas.create_rectangle(x1, y1, x1 + max_tile_width, y1 + max_tile_height, fill="red", tags="tile")
                canvas.create_text(x1 + max_tile_width / 2, y1 + max_tile_height / 2, text="Missing", fill="white",
                                   tags="tile")

    # Отрисовка персонажа
    player_x = pl1.x * max_tile_width - camera_x # <----
    if player_image:
        canvas.create_image(player_x, 0, image=player_image, anchor="nw", tags="player")
    else:
        canvas.create_rectangle(player_x, 0, player_x + player_width, max_tile_height, fill="blue",
                               tags="player")
        canvas.create_text(player_x + player_width / 2, max_tile_height / 2, text="Missing", fill="white",
                           tags="player")

    # Убеждаемся, что персонаж всегда поверх мира
    canvas.tag_raise("player")

# --- Функции для управления персонажем ---
def move_left(event):
    pl1.move_left()

def move_right(event):
    pl1.move_right()

def stop_move(event):
    pl1.stop()

def game_loop():
    pl1.update()
    draw_world()
    window.after(16, game_loop)

# --- Привязка клавиш ---
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<KeyRelease-Left>", stop_move)
window.bind("<KeyRelease-Right>", stop_move)
window.bind("<KeyRelease-a>", stop_move)
window.bind("<KeyRelease-d>", stop_move)

# --- Инициализация персонажа ---
world_instance.TILE_SIZE = max_tile_width
pl1 = person.game_player(world_instance, PLAYER_START_POSITION, PLAYER_TEXTURE, PLAYER_SPEED, LERP_SPEED, player_width) # Передаем player_width

# --- Начальная отрисовка ---
draw_world()

# --- Запуск основного цикла Tkinter ---
game_loop()
window.mainloop()