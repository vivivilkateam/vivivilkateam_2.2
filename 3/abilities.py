import random
# abilities.py
class Ability:  # Или UltimateAbility
    def __init__(self, name, description, icon_name="default_icon"): # Добавляем icon_name и значение по умолчанию
        self.name = name
        self.description = description
        self.icon_name = icon_name

    def apply(self, target):
        """
        Применяет способность к цели (например, танку).
        Этот метод должен быть переопределен в подклассах.
        """
        print(f"Применена способность '{self.name}' к {target}")

    def __str__(self):
        return f"{self.name}: {self.description}"


class BulletAbility(Ability):
    """Базовый класс для способностей, связанных с пулями."""
    def __init__(self, name, description, icon_name):
        super().__init__(name, description, icon_name)

    def modify_bullet(self, bullet):
        """Изменяет параметры пули (например, урон, скорость).
        Этот метод должен быть переопределен в подклассах.
        """
        print(f"Способность '{self.name}' изменяет параметры пули")


class BodyAbility(Ability):
    """Базовый класс для способностей, связанных с телом танка."""
    def __init__(self, name, description):
        super().__init__(name, description)

    def modify_tank(self, tank):
        """Изменяет параметры танка (например, броню, скорость).
        Этот метод должен быть переопределен в подклассах.
        """
        print(f"Способность '{self.name}' изменяет параметры танка")


class UltimateAbility(Ability):
    """Базовый класс для супер-способностей."""
    def __init__(self, name, description, cooldown, icon_name="default_icon"):
        super().__init__(name, description, icon_name)
        self.cooldown = cooldown
        self.current_cooldown = 0

    def is_ready(self):
        """Проверяет, готова ли способность к использованию."""
        return self.current_cooldown == 0

    def use(self, target):
        """Использует супер-способность."""
        if self.is_ready():
            self.apply(target)
            self.current_cooldown = self.cooldown
            print(f"Использована супер-способность '{self.name}'")
        else:
            print(f"Способность '{self.name}' еще не готова. Осталось {self.current_cooldown} ходов.")

    def update_cooldown(self):
        """Обновляет кулдаун способности."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
# abilities.py (продолжение)

# abilities.py (продолжение)

class DashAbility(UltimateAbility):
    """Позволяет танку делать рывок вперед."""
    def __init__(self, name, description, cooldown, icon_name="dash_icon"):
        super().__init__(name, description, cooldown, icon_name) # Передаем icon_name в конструктор базового класса

    def apply(self, target):
        target.dash()

# Создаем экземпляр способности "Рывок"
dash_ability = DashAbility(
    name="Рывок",
    description="Позволяет танку делать рывок вперед.",
    cooldown=5,
    icon_name="dash_icon"  # Указываем иконку
)

# Увеличение урона (X2)
class DamageUpAbility(BulletAbility):
    def __init__(self):
        super().__init__(
            name="X2 урон",
            description="Увеличивает урон от выстрелов вдвое.",
            icon_name="damage_icon"
        )

    def modify_bullet(self, bullet):
        #bullet._damage *= 2  # Удваиваем урон пули
        print("Damage doubled!")

damage_up_ability = DamageUpAbility()

#upgrades.py
# Двойной выстрел
double_shot_upgrade = UltimateAbility(
    name="Двойной выстрел",
    description="Выстреливает двумя пулями одновременно.",
    cooldown=0,
    icon_name="double_shot_icon"
)
def get_random_upgrades(num_upgrades=3):
    all_upgrades = [hp_upgrade, dash_upgrade, ammo_upgrade, damage_up_upgrade, double_shot_upgrade]  # Все улучшения!
    if len(all_upgrades) <= num_upgrades:
        return all_upgrades
    return random.sample(all_upgrades, num_upgrades)