import random
class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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
    def __init__(self, name, description):
        super().__init__(name, description)

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
    def __init__(self, name, description, cooldown):
        super().__init__(name, description)
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
    def __init__(self, name, description, cooldown):
        super().__init__(name, description, cooldown)

    def apply(self, target):
        print("DashAbility.apply() called")
        target.dash()
dash_ability = DashAbility(
    name="Рывок",
    description="Позволяет танку делать рывок вперед.Нажмите SHIFT для активации.",
    cooldown=5  # Например, кулдаун 5 ходов
)
def get_random_upgrades(num_upgrades=3):
    all_upgrades = [dash_ability]  # Замените на полный список улучшений
    if len(all_upgrades) <= num_upgrades:
        return all_upgrades
    return random.sample(all_upgrades, num_upgrades)