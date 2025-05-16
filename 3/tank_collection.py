import world
import abilities
from hitbox import Hitbox
import texture as skin
from tkinter import NW
from random import randint
import missile_collection
import tank_collection
import math
import upgrades
import units


_upgrade_window = None


_tanks = []
_canvas = None
id_screen_text = 0
enemy_colvo = 100

enemy = None

def initialize(canvas, w):
    global _canvas, id_screen_text
    _canvas = canvas
    print("Spawning tank in init")
    global player
    player = spawn(False, w) # Передаём w
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)

    id_screen_text = _canvas.create_text(10, 10,
                                         text=_get_screen_text(),
                                         font=('TkDefualFont', 20),
                                         fill='black',
                                         anchor=NW)
    for i in range(enemy_colvo):
        spawn(True, w) # Передаём w
def spawn(is_bot=True, w = None):
    print(f"Spawning tank: is_bot={is_bot}")
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols - 1)
        row = randint(1, rows - 1)

        if world.get_block(row, col) != world.GROUND:
            continue

        t = units.Tank(_canvas, row, col, bot=is_bot, w = w) # Передаём w

        if not check_collision(t):
            _tanks.append(t)
            return t
def get_random_upgrades(num_upgrades=3):
    return upgrades.get_random_upgrades(num_upgrades)

def show_upgrade_menu(tank):
    global _upgrade_window

    if _upgrade_window:
        _upgrade_window.destroy()  # Закрываем старое окно, если оно есть

    _upgrade_window = tk.Toplevel(_canvas.master)  # Создаем новое окно
    _upgrade_window.title("Выберите улучшение")

    # Получаем случайные улучшения
    available_upgrades = upgrades.get_random_upgrades(3)

    # Создаем элементы для каждого улучшения
    for i, upgrade in enumerate(available_upgrades):
        label = tk.Label(_upgrade_window, text=f"{upgrade.name}: {upgrade.description}")
        label.pack()

        button = tk.Button(_upgrade_window, text=f"Выбрать {upgrade.name}",
                           command=lambda u=upgrade: _apply_upgrade(tank, u))  # Замыкание!
        button.pack()

    # Функция для применения улучшения и закрытия окна


def _apply_upgrade(tank, upgrade):
    upgrade.apply(tank)
    global _upgrade_window
    _upgrade_window.destroy()
    _upgrade_window = None  # Убираем окно



def show_upgrade_menu_if_level_up(tank):
    global _upgrade_window
    if tank._xp >= tank._xp_to_level_up and not _upgrade_window:
       show_upgrade_menu(tank)
def _get_screen_text():
    player = get_player()
    if player.is_destroyed():
        return 'GAME OVER'
    if len(_tanks) == 1:
        return 'YOU WON'

    ammo = player.get_ammo() # Получаем количество патронов
    fuel = player.get_fuel() # Получаем количество топлива
    enemies = len(_tanks) - 1 # Получаем количество врагов
    level = player._level
    xp = player._xp
    xp_to_level_up = player._xp_to_level_up
    hp = player.get_hp()
    max_hp = player._max_hp

    return f'Враги: {enemies}, Патроны: {ammo}, Топливо: {fuel}, Level: {level}, XP: {xp}/{xp_to_level_up}, HP: {hp}/{max_hp}'
def _update_screen():
    _canvas.itemconfig(id_screen_text, text=_get_screen_text())


def get_player():
    return _tanks[0]



def update():
    _update_screen()
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
            _tanks[i]._canvas.delete(_tanks[i]._hp_bar_id) # Удаляем полоску перед удалением
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            missile_collection.check_missiles_collision(_tanks[i])


def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersect(other_tank):
            return True
    return False


def spawn_enemy():
    pos_x = randint(200, world.WIDTH - 200)
    pos_y = randint(200, world.HEIGHT - 200)
    t = units.Tank(_canvas, x=pos_x, y=pos_y, speed=1)

    t.set_target(get_player())
    _tanks.append(t)