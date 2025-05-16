import random
from abilities import UltimateAbility, DamageUpAbility  # Импортируем DamageUpAbility

# Увеличение HP
def _hp_apply(tank: object):  # Изменяем аннотацию типа
    tank._max_hp += 50  # Увеличиваем максимальное HP на 50
    tank._hp = tank._max_hp  # Восстанавливаем здоровье до максимума
    print(f"Tank HP increased to {tank._max_hp}")

hp_upgrade = UltimateAbility( # используем UltimateAbility
    name="Увеличенное здоровье",
    description="Увеличивает максимальное здоровье танка.",
    cooldown = 0,
    icon_name="hp_icon"  # Название файла для иконки
)

# Рывок (Dash)
def _dash_apply(tank: object):  # Изменяем аннотацию типа
    tank.dash()
    print("Dash ability unlocked!")

dash_upgrade = UltimateAbility( # используем UltimateAbility
    name="Dash",
    description="Allows the tank to dash forward a short distance. Press SHIFT to activate.",
    cooldown = 0,
    icon_name="dash_icon"
)

# Увеличение магазина (Ammo)
def _ammo_apply(tank: object):  # Изменяем аннотацию типа
    tank._ammo += 50  # Добавляем 50 патронов к текущему боезапасу
    if tank._ammo > tank._max_ammo: # Проверяем, не превышает ли текущий боезапас максимальный
        tank._ammo = tank._max_ammo  # Если превышает, устанавливаем равным максимальному

    print(f"Tank ammo increased by 50. Current ammo: {tank._ammo}")

ammo_upgrade = UltimateAbility(  # используем UltimateAbility
    name="Увеличенный магазин",
    description="Увеличивает текущий боезапас танка.",
    cooldown = 0,
    icon_name="ammo_icon"  # Название файла для иконки
)

# Увеличение урона (X2)
def _damage_up_apply(tank: object):  # Изменяем аннотацию типа
    tank.bullet_ability = damage_up_ability
    print("Damage up ability unlocked!")

damage_up_upgrade = UltimateAbility(
    name="X2 урон",
    description="Увеличивает урон от выстрелов вдвое.",
    cooldown = 0,
    icon_name="damage_icon"
)

# Двойной выстрел
double_shot_upgrade = UltimateAbility(
    name="Двойной выстрел",
    description="Выстреливает двумя пулями одновременно.",
    cooldown=0,
    icon_name="double_shot_icon"
)

#Регенерация
def _regen_apply(tank: object):  # Изменяем аннотацию типа
    tank.regen()
    print("Регенерация ability unlocked!")

regen_upgrade = UltimateAbility(
    name="Регенерация",
    description="Восстанавливает 10 хп раз в 5 секунд.",
    cooldown = 0,
    icon_name="regen_icon" #ДОБАВЬТЕ КАРТИНКУ В main.py
)
def get_random_upgrades(num_upgrades=3):
    all_upgrades = [hp_upgrade, dash_upgrade, ammo_upgrade, damage_up_upgrade, double_shot_upgrade, regen_upgrade]  # Все улучшения!
    if len(all_upgrades) <= num_upgrades:
        return all_upgrades
    return random.sample(all_upgrades, num_upgrades)