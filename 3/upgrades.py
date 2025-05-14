# upgrades.py
import random


class Upgrade:
    def __init__(self, name, description, apply_func):
        self.name = name
        self.description = description
        self.apply_func = apply_func

    def apply(self, tank):
        self.apply_func(tank)

# Примеры улучшений:
def get_random_upgrades(num_upgrades=3):
    """Возвращает список случайных улучшений."""
    all_upgrades = [dash_upgrade]  # Замените на полный список улучшений
    if len(all_upgrades) <= num_upgrades:
        return all_upgrades
    return random.sample(all_upgrades, num_upgrades)
def _dash_apply(tank):
    tank.has_dash = True # Добавляем флаг, что рывок доступен
    print("Dash ability unlocked!")

dash_upgrade = Upgrade(
    name="Dash",
    description="Allows the tank to dash forward a short distance. Press SHIFT to activate.",
    apply_func=_dash_apply
)

# Другие улучшения можно добавить аналогично
def level_up(self):
    self._level += 1
    #self._speed *= 1.1
    #self._usual_speed = self._speed
    #self._water_speed = self._speed // 2
    #print(f"Tank leveled up! Level: {self._level}, Speed: {self._speed}")
    tank_collection.show_upgrade_menu(self)  # Вызываем функцию из tank_collection

def choose_upgrade(self):
    # Выбираем случайные улучшения (пока только одно)
    available_upgrades = [upgrades.dash_upgrade] # Замените на случайный выбор в будущем
    chosen_upgrade = available_upgrades[0] # Берем первое (пока не реализован выбор)

    # Применяем улучшение
    chosen_upgrade.apply(self)