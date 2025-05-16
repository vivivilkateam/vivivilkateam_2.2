# menu.py
import tkinter as tk
import world  # Импортируем world

def create_main_menu(master, canv, start_game_callback, exit_game_callback):
    # Очищаем холст
    canv.delete("all")

    button_width = 15  # Ширина кнопок (в символах)

    # Заголовок
    title_text = canv.create_text(
        world.SCREEN_WIDTH // 2, 100,
        text="Танчики",
        font=("Arial", 32),
        fill="black"
    )

    # Кнопка "Играть"
    play_button = tk.Button(
        master, text="Играть",
        command=start_game_callback,
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

    # Кнопка "Выход"
    exit_button = tk.Button(
        master, text="Выход",
        command=exit_game_callback,
        font=("Arial", 16),
        bg="lightcoral",
        activebackground="red",
        width=button_width  # Фиксированная ширина
    )
    exit_button_window = canv.create_window(
        world.SCREEN_WIDTH // 2, 400,  # Используем константы world
        window=exit_button,
        anchor="center"  # Якорь в центре кнопки
    )