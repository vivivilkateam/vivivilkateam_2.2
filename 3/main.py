
import missile_collection


import abilities
from tkinter import *
import units
import world
import tank_collection
import texture
import keys
from abilities import dash_ability
# Код клавиши Shift
FPS = 60
game_paused = False  # Игра не на паузе

# ... (Внутри функции update()) ...
def update():
    global game_paused

    if not game_paused:  # Обновляем только если игра не на паузе
        tank_collection.update()
        missile_collection.update()
        player = tank_collection.get_player()
        world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                            player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
        world.update_map()
    if tank_collection.get_player()._level_up_display_time > 0: # Проверяем display_time
        game_paused = True
    else:
        game_paused = False

    w.after(1000 // FPS, update)
def toggle_pause(event=None):
    global game_paused
    game_paused = not game_paused
    print(f"Game paused: {game_paused}")

    w.after(1000 // FPS, update)


# ... (Внутри функции update()) ...

# def key_press(event):
#     player = tank_collection.get_player()
#
#     if player.is_destroyed():
#         return
#
#     if event.keycode == KEY_W:
#         player.forward()
#     elif event.keycode == KEY_S:
#         player.backward()
#     elif event.keycode == KEY_A:
#         player.left()
#     elif event.keycode == KEY_D:
#         player.right()
#     elif event.keycode == KEY_UP:
#         world.move_camera(0, -5)
#     elif event.keycode == KEY_DOWN:
#         world.move_camera(0, 5)
#     elif event.keycode == KEY_LEFT:
#         world.move_camera(-5, 0)
#     elif event.keycode == KEY_RIGHT:
#         world.move_camera(5, 0)
#     elif event.keycode == 32:
#         player.fire()
#     if player.is_destroyed():
#         return


def key_press(event):
    player = tank_collection.get_player()
    if player.is_destroyed():
        return
 # Передаем нажатую клавишу и True (нажата)

 # Вызываем метод jump() у танка  # Добавим обработчик нажатий клавиш

    # Движение (обработка одновременного нажатия)
    if event.keycode == keys.KEY_W:
        player.forward()
    elif event.keycode == keys.KEY_S:
        player.backward()
    if event.keycode == keys.KEY_A:
        player.left()
    elif event.keycode == keys.KEY_D:
        player.right()

    if event.keycode == 32:
        player.fire()

def key_release(event):
    player = tank_collection.get_player()
    if player.is_destroyed():
        return
    player.set_movement(event.keycode, True)

    if event.keycode == keys.KEY_SHIFT and player.dash_ability is not None:
        print("SHIFT key pressed")
        player.dash()  # вызываем рывок только если способность есть

# main.py
def load_textures():
    # ... (другие текстуры) ...
    texture.load('regen_icon', '../img/regen_icon.png')
    texture.load('double_shot_icon', '../img/duo_missile_icon.png')
    texture.load('damage_icon', '../img/damage_icon.png')
    texture.load('dash_icon', '../img/dash_icon.png')
    texture.load('hp_icon', '../img/hp_icon.png')
    texture.load('ammo_icon', '../img/ammo_icon.png')


    texture.load('tank_up', '../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load('tank_up_player', '../img/tank_up_player.png')
    texture.load('tank_down_player', '../img/tank_down_player.png')
    texture.load('tank_left_player', '../img/tank_left_player.png')
    texture.load('tank_right_player', '../img/tank_right_player.png')

    texture.load('tank_up',
                  '../img/tank_up.png')
    texture.load('tank_down',
                  '../img/tank_down.png')
    texture.load('tank_left',
                  '../img/tank_left.png')
    texture.load('tank_right',
                  '../img/tank_right.png')

    texture.load('tank_up_player',
                  '../img/tank_up_player.png')
    texture.load('tank_down_player',
                  '../img/tank_down_player.png')
    texture.load('tank_left_player',
                  '../img/tank_left_player.png')
    texture.load('tank_right_player',
                  '../img/tank_right_player.png')
    texture.load('player',
                  '../Dark_school/player.png')

    texture.load(world.BRICK, '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')

    texture.load(world.MISSLE, '../img/bonus.png')

    texture.load('missile_up', '../img/missile_up.png')
    texture.load('missile_left', '../img/missile_left.png')
    texture.load('missile_right', '../img/missile_right.png')
    texture.load('missile_down', '../img/missile_down.png')

    texture.load('tank_destroy', '../img/tank_destroy.png')

    texture.load('100', '../img/100.png')
    texture.load('75', '../img/75.png')
    texture.load('50', '../img/50.png')
    texture.load('25', '../img/25.png')
    texture.load('0', '../img/0.png')





    texture.load('missile_up',
                  '../img/missile_up.png')
    texture.load('missile_down',
                  '../img/missile_down.png')
    texture.load('missile_left',
                  '../img/missile_left.png')
    texture.load('missile_right',
                  '../img/missile_right.png')





w = Tk()
w.title('Танки на минималках 2.0')
w.geometry(f"{world.SCREEN_WIDTH}x{world.SCREEN_HEIGHT}")


load_textures()

canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='gray20')



canv.pack()
world.initialize(canv)
tank_collection.initialize(canv,w)
#main.py

missile_collection.initialize(canv)



w.bind("<p>", toggle_pause) #или любую другую клавишу
update()


# Привязка клавиш
w.bind("<KeyPress>", key_press) # Меняем привязку, чтобы обрабатывать все нажатия в key_press
w.bind("<KeyRelease>", key_release) # Добавляем обработку отпускания клавиш

# Оставляем старые привязки, чтобы ничего не сломать.  Их можно будет удалить.

w.mainloop()
