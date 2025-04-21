from units import Missile
_missiles = []
_canvas = None


def initialize(canvas):
    global _canvas
    _canvas = canvas


def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)


def update():
    start = len(_missiles)-1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def destroy_missile(self, missile):
    missile.destroy()  # Вызываем метод destroy() у ракеты
    self._missiles.remove(missile)  # Удаляем ракету из списка

def check_missiles_collision(tank):
    global _missiles # Указываем, что используем глобальную переменную _missiles

    # Создаем новый список ракет для итерации, чтобы избежать проблем при удалении элементов из _missiles
    missiles_to_remove = []
    for missile in _missiles:
        if missile.get_owner() != tank and tank.intersect(missile):
            tank.damage(25)  # Наносим урон танку
            missiles_to_remove.append(missile) # Добавляем ракету в список на удаление

    # Удаляем ракеты после завершения итерации
    for missile in missiles_to_remove:
        missile.destroy()  # Вызываем destroy() у объекта Missile
        _missiles.remove(missile) # Удаляем ракету из списк


