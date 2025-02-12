import random

class World:
    def __init__(self, length, locations):
        """
        Инициализация мира, представленного линией.

        Args:
            length: Длина линии (количество плиток).
            locations: Словарь, связывающий имя текстуры с путем к файлу изображения.
        """
        self.length = length
        self.locations = locations
        self.line = self.generate_world()

    def generate_world(self):
        """
        Создает случайную линию мира, используя доступные текстуры.

        Returns:
            Список, представляющий линию мира (пути к изображениям).
        """
        world_line = []
        available_textures = list(self.locations.keys())  # Получаем список ключей (имен текстур)
        for _ in range(self.length):
            random_texture_name = random.choice(available_textures)  # Случайное имя текстуры
            world_line.append(self.locations[random_texture_name])  # Сохраняем путь к изображению
        return world_line

    def get_tile(self, x):
        """
        Возвращает путь к текстуре по заданному индексу.

        Args:
            x: Индекс плитки в линии.

        Returns:
            Путь к текстуре, расположенной по заданному индексу.
        """
        if 0 <= x < self.length:
            return self.line[x]
        else:
            return None

    def __str__(self):
        """
        Возвращает строковое представление мира (не используется, но может пригодиться для отладки).
        """
        return str(self.line) # Просто выводим список путей к изображениям

