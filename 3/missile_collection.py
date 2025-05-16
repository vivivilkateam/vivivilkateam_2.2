from units import Missile
_missiles = []
_canvas = None


def initialize(canvas):
    global _canvas
    _canvas = canvas


def fire(owner):
    x = owner.get_x() + owner.get_size() // 2
    y = owner.get_y() + owner.get_size() // 2
    m = Missile(_canvas, owner)
    _missiles.append(m)
    return m

def update(game_paused):  # Принимаем game_paused как аргумент
    if game_paused:  # Проверяем, находится ли игра на паузе
        return  # Если да, то выходим из метода

    start = len(_missiles) - 1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def destroy_missile(self, missile):
    missile.destroy()  # Вызываем метод destroy() у ракеты
    self._missiles.remove(missile)  # Удаляем ракету из списка

# missile_collection.py
def check_missiles_collision(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersect(tank):
            missile.destroy()
            damage = 25
            if hasattr(missile.get_owner(), 'bullet_ability') and missile.get_owner().bullet_ability:
                damage *= 2
            return damage  # Добавляем ретурн, возвращаем damage
    return 0