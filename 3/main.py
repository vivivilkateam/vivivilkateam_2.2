
import missile_collection
import menu
import time
import abilities
import tkinter as tk
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
game_start_time = 0  # Время начала игры
total_fives = 0

def format_time(seconds):
    """Форматирует время в строку вида MM:SS."""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

def start_game():
    global game_start_time, total_fives  # Добавляем global
    print("Запуск игры...")
    # Очищаем холст от элементов меню
    canv.delete("all")
    world.initialize(canv)
    tank_collection.initialize(canv, w)
    missile_collection.initialize(canv)
    game_start_time = time.time()  # Запоминаем время начала игры
    update()

def exit_game():
    print("Выход из игры...")
    w.destroy()  # Закрываем окно tkinter
    exit()
def show_shop(total_fives):
    print("Открытие магазина...")
    # Очищаем холст
    canv.delete("all")

    # Отображаем фоновое изображение
    shop_background_id = canv.create_image(
        -275, -375,
        image=texture.get('shop_background'),
        anchor="nw"
    )

    # Отображаем текст таблички
    shop_sign_text = canv.create_text(
        world.SCREEN_WIDTH // 2, 200,  # Позиция рядом с дедом
        text="Нажми E, чтобы открыть магазин",
        font=("Arial", 16),
        fill="white",  # Цвет текста
        anchor="center"  # Якорь в центре текста
    )

    # Надпись количества пятерок
    fives_label = canv.create_text(
        world.SCREEN_WIDTH // 2, 300,
        text=f"У вас {total_fives} пятерок",
        font=("Arial", 20),
        fill="white",
        anchor="center"
    )

    # Заголовок
    title_text = canv.create_text(
        world.SCREEN_WIDTH // 2, 100,
        text="Магазин",
        font=("Arial", 32),
        fill="black"
    )

    # Кнопка "Назад"
    back_button = tk.Button(
        w, text="Назад",
        command=show_main_menu,
        font=("Arial", 16),
        bg="lightblue",
        activebackground="blue"
    )
    back_button_window = canv.create_window(
        50, world.SCREEN_HEIGHT - 50,  # Позиция в нижнем левом углу
        window=back_button,
        anchor="sw"  # Якорь в нижнем левом углу
    )
def show_shop_menu(total_fives):
    # Очищаем холст
    canv.delete("all")

    # Размеры и положение меню
    rect_width = 800
    rect_height = 600
    x = world.SCREEN_WIDTH // 2 - rect_width // 2
    y = world.SCREEN_HEIGHT // 2 - rect_height // 2

    # Создаем черный прямоугольник для фона меню
    menu_rect_id = canv.create_rectangle(
        x, y, x + rect_width, y + rect_height,
        fill="blue", outline="white", width=3
    )

    # Текст "Магазин"
    shop_text_id = canv.create_text(
        world.SCREEN_WIDTH // 2, y + 50,
        text="Магазин",
        font=("Arial", 24),
        fill="blue"
    )
    fives_text = canv.create_text(
        world.SCREEN_WIDTH // 2, y + 100,
        text=f"У вас {total_fives} пятерок",
        font=("Arial", 16),
        fill="white",
        anchor="center"
    )
    # Кнопка "Назад"
    back_button = tk.Button(
        w, text="Назад",
        command=show_main_menu,
        font=("Arial", 16),
        bg="lightblue",
        activebackground="blue"
    )
    back_button_window = canv.create_window(
        x + 50, y + rect_height - 50,  # Позиция в нижнем левом углу
        window=back_button,
        anchor="sw"  # Якорь в нижнем левом углу
    )

def show_main_menu():
    # Очищаем холст
    canv.delete("all")

    button_width = 15  # Ширина кнопок (в символах)

    # Заголовок
    title_text = canv.create_text(
        world.SCREEN_WIDTH // 2, 100,
        text="Dark school Roguelike",
        font=("Arial", 32),
        fill="black"
    )

    # Кнопка "Играть"
    play_button = tk.Button(
        w, text="Играть",
        command=start_game,
        font=("Arial", 16),
        bg="lightgreen",
        activebackground="green",
        width=button_width  # Фиксированная ширина
    )
    play_button_window = canv.create_window(
        world.SCREEN_WIDTH // 2, 300,  # Используем константы world
        window=play_button,
        anchor="center"  # Якорь в центре кнопки
    )

    # Кнопка "Магазин"
    shop_button = tk.Button(
        w, text="Магазин",
        command=lambda: show_shop(total_fives),  # Передаем total_fives
        font=("Arial", 16),
        bg="lightyellow",
        activebackground="yellow",
        width=button_width  # Фиксированная ширина
    )
    shop_button_window = canv.create_window(
        world.SCREEN_WIDTH // 2, 400,  # Используем константы world
        window=shop_button,
        anchor="center"  # Якорь в центре кнопки
    )

    # Кнопка "Выход"
    exit_button = tk.Button(
        w, text="Выход",
        command=exit_game,
        font=("Arial", 16),
        bg="lightcoral",
        activebackground="red",
        width=button_width  # Фиксированная ширина
    )
    exit_button_window = canv.create_window(
        world.SCREEN_WIDTH // 2, 500,  # Используем константы world
        window=exit_button,
        anchor="center"  # Якорь в центре кнопки
    )
def update():
    global game_paused, game_start_time, total_fives

    if game_start_time != 0:  # Проверяем, была ли запущена игра
        elapsed_time = time.time() - game_start_time
        if elapsed_time >= 180:  # 5 минут = 300 секунд
            print("Время вышло! Возвращаемся в меню.")
            total_fives += 500  # Начисляем пятерки
            print(f"Начислено 500 пятерок. Всего: {total_fives}")
            game_start_time = 0  # Сбрасываем время начала игры
            show_main_menu()  # Возвращаемся в меню
            return  # Важно выйти из функции update()

        formatted_time = format_time(elapsed_time)  # Форматируем время
        tank_collection.update(game_paused, formatted_time)  # Передаем game_paused и время

    else:
        tank_collection.update(game_paused, None)  # Передаем None, если игра не запущена

    if not game_paused:  # Обновляем только если игра не на паузе
        missile_collection.update(game_paused)  # Передаем game_paused
        player = tank_collection.get_player()
        world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                            player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
        world.update_map()
    if tank_collection.get_player()._level_up_display_time > 0:
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
    if tank_collection._tanks: # Добавляем проверку
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
        elif event.keycode == 69: # Код клавиши "E"
            print("Открываем магазин по нажатию 'E'")
            show_shop_menu(total_fives)

        if event.keycode == 32:
            player.fire()
def key_release(event):
    if tank_collection._tanks: # Добавляем проверку
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
    texture.load('shop_background', '../img/magasin.png')
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
    texture.load('monster', '../img/monster.png')

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
w.title('Dark school Roguelike')
w.geometry(f"{world.SCREEN_WIDTH}x{world.SCREEN_HEIGHT}")


load_textures()

canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='gray20')



canv.pack()

w.bind("<p>", toggle_pause) #или любую другую клавишу


# Привязка клавиш
w.bind("<KeyPress>", key_press) # Меняем привязку, чтобы обрабатывать все нажатия в key_press
w.bind("<KeyRelease>", key_release) # Добавляем обработку отпускания клавиш

# Оставляем старые привязки, чтобы ничего не сломать.  Их можно будет удалить.
show_main_menu()


w.mainloop()