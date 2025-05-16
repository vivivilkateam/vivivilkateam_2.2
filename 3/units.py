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
from abilities import dash_ability
from keys import KEY_W, KEY_S, KEY_A, KEY_D, KEY_SHIFT
class Unit:
    def __init__(self, canvas, x, y, speed, padding, bot, default_image, has_hp_bar=False):
        self._destroyed = False
        self._speed = speed
        self._x = x
        self._y = y
        self._vx = 0
        self._vy = 0
        self._canvas = canvas
        self._hp = 100
        self._dx = 0
        self._dy = 0
        self._bot = bot
        self._hitbox = Hitbox(x, y, world.BLOCK_SIZE, world.BLOCK_SIZE, padding=padding)
        self._default_image = default_image
        self._id = self._canvas.create_image(self._x, self._y, image=skin.get(self._default_image), anchor=NW)
        self._hp_bar_id = None  # Изначально полоски нет
        self._max_hp = 100
        self._has_hp_bar = has_hp_bar  # Флаг, есть ли полоска
        self._fuel = 10000 #добавляем

        if self._has_hp_bar:
            self._create_hp_bar()
        self._dx = 0  # Текущее направление по X (-1, 0, 1)
        self._dy = 0  # Текущее направление по Y (-1, 0, 1)
        self._moving = False  # Движется ли танк в данный момент
        self._heading = 0
    def set_movement(self, keycode, is_pressed):
        if keycode == KEY_W:
            self._vy = -1 if is_pressed else 0
            self.forward()
        elif keycode == KEY_S:
            self._vy = 1 if is_pressed else 0
            self.backward()
        elif keycode == KEY_A:
            self._vx = -1 if is_pressed else 0
            self.left()
        elif keycode == KEY_D:
            self._vx = 1 if is_pressed else 0
            self.right()
        # units.py

    def damage(self, value):
        print(f"Получен урон {value}")  # отладочный принт
        self._hp -= value
        if self._hp < 0:
            self._hp = 0
        if self._hp <= 0:
            self.destroy()
        elif self._has_hp_bar:
            self._update_hp_bar()

    def _create_hp_bar(self):
         x = world.get_screen_x(self._x)
         y = world.get_screen_y(self._y) - 10

         self._hp_bar_id = self._canvas.create_rectangle(
             x, y, x + world.BLOCK_SIZE, y + 5, fill="green", outline=""
         )
         self._update_hp_bar()

    def _update_hp_bar(self):
        if self._has_hp_bar:
            hp_percentage = max(0, self._hp) / self._max_hp
            bar_width = int(world.BLOCK_SIZE * hp_percentage)
            x = world.get_screen_x(self._x)
            y = world.get_screen_y(self._y) - 10

            self._canvas.coords(self._hp_bar_id, x, y, x + bar_width, y + 5)
            if hp_percentage > 0.5:
                color = "green"
            elif hp_percentage > 0.25:
                color = "yellow"
            else:
                color = "red"

            self._canvas.itemconfig(self._hp_bar_id, fill=color)


    def destroy(self):
        self._destroyed = True
        self._speed = 0
        if isinstance(self, Tank):
            self._canvas.itemconfig(self._id, image=skin.get(self._tank_destroy))
        else:
            self._canvas.delete(self._id)

        if self._hp_bar_id:
            self._canvas.delete(self._hp_bar_id)
        # Добавляем начисление опыта
        if self.is_bot():
            player = tank_collection.get_player()
            if player:
                player.gain_xp(50)
  # Например, 50 опыта за убийство врага

    def _repaint(self):  # Переопределяем, чтобы обновлять полоску HP
        screen_x = world.get_screen_x(self._x)
        screen_y = world.get_screen_y(self._y)
        self._canvas.moveto(self._id, x=screen_x, y=screen_y)
        if self._has_hp_bar:
            self._update_hp_bar()  # Обновляем положение полоски при движении танка

    def _undo_move(self):  # Переопределяем для полоски
        if self._dx == 0 and self._dy == 0:
            return
        self._x -= self._dx
        self._y -= self._dy
        self._update_hitbox()
        self._repaint()
        self._dx = 0
        self._dy = 0
        if self._has_hp_bar:
             self._update_hp_bar() # Обновляем положение полоски при отмене движения


    def __del__(self):
        try:
            self._canvas.delete(self._id)
        except Exception:
            pass
        if self._hp_bar_id:  # Проверяем наличие полоски
            self._canvas.delete(self._hp_bar_id)




    def is_destroyed(self):
        return self._destroyed




    def _create(self):
        self._id = self._canvas.create_image(self._x, self._y, image=skin.get(self._default_image), anchor=NW)

    def forward(self):
        self._vx = 0
        self._vy = -1
        self._canvas.itemconfig(self._id,  #Убрал canvas
                               image=skin.get(self._forward_image))
        self._heading = 0  # Угол для движения вперед

    def backward(self):
        self._vx = 0
        self._vy = 1
        self._canvas.itemconfig(self._id,
                               image=skin.get(self._backward_image))
        self._heading = 180  # Угол для движения назад

    def left(self):
        self._vx = -1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                               image=skin.get(self._left_image))
        self._heading = 90  # Угол для движения влево

    def right(self):
        self._vx = 1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                               image=skin.get(self._right_image))
        self._heading = 270  # Угол для движения вправо
    def stop(self):
        self._vx = 0
        self._vy = 0

    def update(self):
        if self._bot:
            self._AI()
        self._dx = self._vx * self._speed
        self._dy = self._vy * self._speed
        self._x += self._dx
        self._y += self._dy
        self._update_hitbox()
        self._check_map_collision()
        self._repaint()


    def _AI(self):
        pass

    def _update_hitbox(self):
        self._hitbox.moveto(self._x, self._y)

    def _check_map_collision(self):
        details = {}
        result = self._hitbox.check_map_collision(details)
        if result:
            self._on_map_collision(details)
        else:
            self._no_map_collision()

    def _no_map_collision(self):
        pass

    def _on_map_collision(self, details):
        pass



    def intersect(self, other_unit):
        value = self._hitbox.intersects(other_unit._hitbox)
        if value:
            self._on_intersect(other_unit)
        return value

    def _on_intersect(self, other_unit):
        self._undo_move()

    def _change_orientation(self):
        rand = randint(0, 3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.forward()
        if rand == 2:
            self.right()
        if rand == 3:
            self.backward()

    def get_hp(self):
        return self._hp

    def get_speed(self):
        return self._speed

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_vx(self):
        return self._vx

    def get_vy(self):
        return self._vy

    def get_size(self):
        return world.BLOCK_SIZE

    def is_bot(self):
        return self._bot


class Tank(Unit):
    def __init__(self, canvas, row, col, bot=True, w=None):
        super().__init__(canvas, col * world.BLOCK_SIZE, row * world.BLOCK_SIZE, 5, 8,
                         bot, 'player', has_hp_bar=True)
        self.w = w
        self._chosen_upgrade = None
        self.dash_ability = None  # Добавляем атрибут dash_ability
        # Инициализация атрибутов Tank
        self._xp = 0
        self._xp_to_level_up = 100
        self._level = 1
        self._tank_destroy = 'tank_destroy'
        self._max_ammo = 10
        self._ammo = self._max_ammo
        self._max_fuel = 100
        self.double_shot = False
        self._heading = 0  # Инициализируем атрибут _heading
        self._regen_timer = 0 # Таймер для регенерации
        self._regen_cooldown = 5000  # 5 секунд в миллисекундах
        self._has_regen = False # Есть ли регенерация
        # Инициализация изображений
        if bot:
            self._forward_image = 'tank_up'
            self._backward_image = 'tank_down'
            self._left_image = 'tank_left'
            self._right_image = 'tank_right'
        else:
            self._forward_image = 'player'
            self._backward_image = 'player'
            self._left_image = 'player'
            self._right_image = 'player'
            self._tank_destroy = 'player' # Добавляем атрибут _tank_destroy
        self._100 = '100'
        self._75 = '75'
        self._50 = '50'
        self._25 = '25'
        self._0 = '0'

        # Дополнительные инициализации
        self.forward()
        self._ammo = 80
        self._usual_speed = self._speed
        self._water_speed = self._speed // 2
        self._target = None

        # Атрибуты для отображения окна уровня (перенесены из LevelUpWindow)
        self.level_up_rect_id = None
        self._level_up_text_ids = []
        self._level_up_display_time = 0
        self._xp_bar_id = None

    def regen(self):
        self._has_regen = True

    def apply_upgrade(self):
        print("apply_upgrade called")  # Проверяем вызов метода
        print(f"Applying upgrade: {self._chosen_upgrade.name}")
        if self._chosen_upgrade:
            if self._chosen_upgrade.name == "Dash":
                self.dash_ability = True  # теперь танк имеет эту способность
                print("Dash ability unlocked!")  # Добавляем отладочный вывод
            elif self._chosen_upgrade.name == "Увеличенное здоровье":  # Добавлено условие
                self._hp_apply()
            elif self._chosen_upgrade.name == "X2 урон":
                self.bullet_ability = True  # Говорим, что есть эта способность
            elif self._chosen_upgrade.name == "Двойной выстрел":
                self.double_shot = True
            elif self._chosen_upgrade.name == "Регенерация":  # Добавляем регенерацию
                self.regen()  # Активируем функцию
            else:
                self.dash_ability = None
                print("Dash ability locked!")

        self.hide_level_up_message()
    def _hp_apply(self):
        print("_hp_apply called")
        print(f"Tank's HP before: {self.get_hp()}/{self._max_hp}")  # Вывод HP до
        self._max_hp += 50  # Увеличиваем максимальное HP на 50
        self._hp = self._max_hp  # Восстанавливаем здоровье до максимума
        print(f"Tank's HP after: {self.get_hp()}/{self._max_hp}")  # Вывод HP после

    def show_level_up_message(self, w):
        print("show_level_up_message called")
        self.hide_level_up_message()  # Скрываем старое окно, если оно есть
        self._level_up_display_time = 1000  # Паузим игру
        rect_width = 600
        rect_height = 300
        x = world.SCREEN_WIDTH // 2 - rect_width // 2
        y = 50

        self.level_up_rect_id = self._canvas.create_rectangle(
            x, y, x + rect_width, y + rect_height,
            fill="black", outline="white", width=3
        )

        # Отображение уровня
        level_text = f"Уровень {self._level}"
        text_x = x + rect_width // 2
        text_y = y + 20
        level_text_id = self._canvas.create_text(
            text_x, text_y, text=level_text, font=("Arial", 16), fill="white"
        )
        self._level_up_text_ids.append(level_text_id)

        w.unbind("<KeyPress-1>")
        w.unbind("<KeyPress-2>")
        w.unbind("<KeyPress-3>")
        available_upgrades = tank_collection.get_random_upgrades(3)
        print(f"Available upgrades: {[upgrade.name for upgrade in available_upgrades]}")  # Проверяем список
        self._chosen_upgrade = None  # Сбрасываем выбор при открытии меню

        # Отображение улучшений
        image_x = x + 20  # Задаем x для иконки
        text_x = x + 100  # Задаем x для текста
        for i, upgrade in enumerate(available_upgrades):
            print(f"Отрисовываю улучшение: {upgrade.name}, icon_name: {upgrade.icon_name}")
            image_y = y + 50 + i * 90  # Изменяем только y для иконки
            image_id = self._canvas.create_image(
                image_x, image_y, image=skin.get(upgrade.icon_name), anchor="nw"
            )
            self._level_up_text_ids.append(image_id)

            text_y1 = y + 50 + i * 90  # Изменяем только y для первой строки текста
            text_y2 = text_y1 + 20  # Изменяем только y для второй строки текста

            description_lines = upgrade.description.split(' ')
            line1 = " ".join(description_lines[:4])
            line2 = " ".join(description_lines[4:])

            upgrade_text_id1 = self._canvas.create_text(
                text_x, text_y1, text=f"{upgrade.name}: {line1}", font=("Arial", 12), fill="white", anchor="w"
            )
            self._level_up_text_ids.append(upgrade_text_id1)

            upgrade_text_id2 = self._canvas.create_text(
                text_x, text_y2, text=line2, font=("Arial", 12), fill="white", anchor="w"
            )
            self._level_up_text_ids.append(upgrade_text_id2)

        #  Сохраняем выбранный апгрейд в зависимости от нажатой клавиши

        if len(available_upgrades) > 0:
            self.w.bind("<KeyPress-1>", lambda event, up=available_upgrades[0]: self._choose_upgrade(up))
        if len(available_upgrades) > 1:
            self.w.bind("<KeyPress-2>", lambda event, up=available_upgrades[1]: self._choose_upgrade(up))
        if len(available_upgrades) > 2:
            self.w.bind("<KeyPress-3>", lambda event, up=available_upgrades[2]: self._choose_upgrade(up))

    def _choose_upgrade(self, upgrade):
        print("_choose_upgrade called")
        self._chosen_upgrade = upgrade  # Сохраняем выбранное улучшение
        print(f"Chosen upgrade: {self._chosen_upgrade}")
        self.apply_upgrade()  # Применяем


    def update(self):
        if self._bot:
            self._AI()
        self._dx = self._vx * self._speed
        self._dy = self._vy * self._speed
        self._x += self._dx
        self._y += self._dy
        self._update_hitbox()
        self._check_map_collision()
        self._repaint()
        # Проверяем и скрываем окно (если оно отображено)
        if self._level_up_display_time > 0:
            self._level_up_display_time -= 1
            if self._level_up_display_time == 0:
                self.hide_level_up_message()
        damage = missile_collection.check_missiles_collision(self)  # Получаем урон
        if damage > 0:
            self.damage(damage)
        if self._level_up_display_time > 0:
            self._level_up_display_time -= 1
            return
        if self._has_regen:  # Если у нас есть регенерация
            self._regen_timer += world.get_dt() # Увеличиваем таймер на время, прошедшее с последнего кадра
            if self._regen_timer >= self._regen_cooldown:  # Если таймер превысил кулдаун
                self._regen_timer = 0  # Сбрасываем таймер
                if self._hp < self._max_hp:  # Если здоровье неполное
                    self._hp = min(self._hp + 10, self._max_hp)  # Восстанавливаем 10 HP, но не больше максимума
                    print("Регенерация! HP:", self._hp) # Выводим сообщение о регенерации
                    self._update_hp_bar()  # Обновляем полоску здоровья

    def _update_xp_bar(self):
        if self._xp_bar_id is not None:
            x = world.SCREEN_WIDTH // 2 - 600 // 2
            xp_percentage = min(1.0, self._xp / self._xp_to_level_up)
            bar_width = int((600 - 20) * xp_percentage)
            self._canvas.coords(
                self._xp_bar_id,
                x + 10,
                50 + 80,
                x + 10 + bar_width,
                50 + 90,
            )

    def hide_level_up_message(self):
        if self.level_up_rect_id:
            self._canvas.delete(self.level_up_rect_id)
            self.level_up_rect_id = None
        for text_id in self._level_up_text_ids:
            if text_id:
                self._canvas.delete(text_id)
        if self._xp_bar_id:
            self._canvas.delete(self._xp_bar_id)
            self._xp_bar_id = None
        self._level_up_text_ids = []
        self._level_up_display_time = 0  # Обнуляем display_time при скрытии

    def gain_xp(self, amount):
        self._xp += amount
        while self._xp >= self._xp_to_level_up:
            self.level_up()
            self._xp -= self._xp_to_level_up
            self._xp_to_level_up = int(self._xp_to_level_up * 3)
        self._update_xp_bar()

    def level_up(self):
        self._level += 1
        self._speed *= 1.1
        self._usual_speed = self._speed
        self._water_speed = self._speed // 2
        print(f"Tank leveled up! Level: {self._level}, Speed: {self._speed}")
        self.show_level_up_message(self.w)  # Передаём w

    def dash(self):
        print("Tank.dash() called")
        jump_x = self._vx * world.BLOCK_SIZE * 3
        jump_y = self._vy * world.BLOCK_SIZE * 3
        if jump_x == 0 and jump_y == 0:
            print("jump_x and jump_y are 0, returning")
            return
        print(f"jump_x: {jump_x}, jump_y: {jump_y}")
        new_x = self._x + jump_x
        new_y = self._y + jump_y

        # Ограничиваем перемещение, чтобы не выходить за границы карты
        new_x = max(0, min(new_x, world.get_widht() - world.BLOCK_SIZE))
        new_y = max(0, min(new_y, world.get_height() - world.BLOCK_SIZE))

        temp_hitbox = Hitbox(new_x, new_y, world.BLOCK_SIZE, world.BLOCK_SIZE, padding=self._hitbox.padding)
        details = {}
        collision = temp_hitbox.check_map_collision(details)
        print(f"Collision: {collision}")  # Проверяем столкновение
        print(f"Details: {details}")  # Выводим детали столкновения
        # Если нет столкновения, перемещаем танк
        if not collision:
            self._x = new_x
            self._y = new_y
            self._update_hitbox()
            self._repaint()
            print("Tank moved successfully!")
        else:
            print("Collision detected, dash aborted.")

    def hp_damage(self):
        if self._hp == 100:
            print('100')
        elif 100 > self._hp > 75:
            print('75')
        elif 75 > self._hp > 50:
            print('50')
        elif 50 > self._hp > 25:
            print('25')
        elif 25 > self._hp > 0:
            print('0')

    def set_target(self, target):
        self._target = target

    # Добавим методы для получения информации о патронах и топливе
    def get_ammo(self):
        return self._ammo

    def get_fuel(self):
        return self._fuel

    def _AI_goto_target(self):
        if randint(1, 2) == 1:
            if self._target.get_x() < self.get_x():
                self.left()
            else:
                self.right()
        else:
            if self._target.get_y() < self.get_y():
                self.forward()
            else:
                self.backward()

    def _take_ammo(self):
        self._ammo += 10
        if self._ammo > 100:
            self._ammo1 = 100

        # units.py
        # units.py

    def fire(self):
        if self._ammo > 0:
            self._ammo -= 1
            missile = missile_collection.fire(self)  # Первый выстрел
            print("Первый выстрел создан")
            if missile and self._chosen_upgrade and self._chosen_upgrade.name == "Двойной выстрел":
                print("Двойной выстрел активирован")
                if self._ammo > 0:
                    self._ammo -= 1
                    angle = math.radians(self._heading)  # Преобразуем угол в радианы
                    offset = 20  # Величина смещения
                    x = self.get_x() + self.get_size() // 2 + offset * math.cos(angle)  # Смещение по x
                    y = self.get_y() + self.get_size() // 2 + offset * math.sin(angle)  # Смещение по y
                    missile = Missile(self._canvas, self)
                    #  Как вариант
                    # missile.set_coords(x - missile.get_width() // 2, y - missile.get_height() // 2,
                    #                    x + missile.get_width() // 2, y + missile.get_height() // 2)
                    missile_collection._missiles.append(missile)
                    print("Второй выстрел создан и добавлен")
        return

    def _set_usual_speed(self):
        self._speed = self._usual_speed

    def _set_water_speed(self):
        self._speed = self._water_speed

    def _on_map_collision(self, details):
        if world.WATER in details and len(details) == 1:
            self._set_water_speed()
        elif world.MISSLE in details:
            pos = details[world.MISSLE]
            if world.take(pos['row'], pos['col']) != world.AIR:
                self._take_ammo()
        else:
            self._undo_move()
            if self._bot:
                self._change_orientation()

    def _no_map_collision(self):
        self._set_usual_speed()

    def _on_intersect(self, other_unit):
        super()._on_intersect(other_unit)
        if self._bot:
            self._change_orientation()

    def _AI(self):
        if randint(1, 30) == 1:
            if randint(1, 10) < 9 and self._target is not None:
                self._AI_goto_target()
            else:
                self._change_orientation()
        elif randint(1, 30) == 1:
            self._AI_fire()
        elif randint(1, 100) == 1:
            self.fire()

    def _AI_fire(self):
        if self._target is None:
            return

        center_x = self.get_x() + self.get_size()//2
        center_y = self.get_y() + self.get_size() // 2

        target_center_x = (self._target.get_x() + self._target.get_size() // 2)
        target_center_y = (self._target.get_y() + self._target.get_size() // 2)

        row = world.get_row(center_y)
        col = world.get_row(center_x)

        row_target = world.get_row(target_center_y)
        col_target = world.get_col(target_center_x)

        if row == row_target:
            if col < col_target:
                self.right()
                self.fire()
            else:
                self.left()
                self.fire()

        elif col == col_target:
            if row < row_target:
                self.backward()
                self.fire()
            else:
                self.forward()
                self.fire()
class Missile(Unit):
    def __init__(self, canvas, owner):
        super().__init__(canvas, owner.get_x(), owner.get_y(),
                         8, 20, False,
                         'missile_up', has_hp_bar=False)  # Отключаем полоску

        self._forward_image = 'missile_up'
        self._backward_image = 'missile_down'
        self._left_image = 'missile_left'
        self._right_image = 'missile_right'
        self._owner = owner
        self._damage = 25 # Установите базовый урон пули
        # ... остальной код ...

        if owner.get_vx() == 1 and owner.get_vy() == 0:
            self.right()
        if owner.get_vx() == -1 and owner.get_vy() == 0:
            self.left()
        if owner.get_vx() == 0 and owner.get_vy() == -1:
            self.forward()
        if owner.get_vx() == 0 and owner.get_vy() == 1:
            self.backward()

        self._x += owner.get_vx() * self.get_size() // 2
        self._y += owner.get_vy() * self.get_size() // 2

        self._hitbox.set_blacklist([world.CONCRETE, world.BRICK])

    def get_owner(self):
        return self._owner

    def _on_map_collision(self, details):
        if world.BRICK in details:
            row = details[world.BRICK]['row']
            col = details[world.BRICK]['col']
            world.destroy(row, col)
            self.destroy()

        if world.CONCRETE in details:
            self.destroy()