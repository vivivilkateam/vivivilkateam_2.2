class Animal:
    def speak(self):
        print('издавать звуки')

class Dog(Animal):
    def speak(self):
        print('гав-гав!')

class BigDog(Dog):
    def speak(self):
        print('ГАВ!!')

class SmallDog(Dog):
    def speak(self):
        print('гав-гав-гав-гав-гав-гав')

class ToyDog(SmallDog):
    def speak(self):
        print('игрушка звучит как гав гав')

class RobotDog(ToyDog):
    def speak(self):
        print('робо собака звучит как гав гав')


class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print('очень злой взгляд')


class Cat(Animal):
    def _meow(self):
        print('мяу-мяу!')
    def speak(self):
        self._meow()


class CuteCat(Cat):
    def _meow(self):
        print('мяууу')


def say_n_times(animal,times):
    for  _ in range(times):
        animal.speak()


list = [Cat(),Dog(),BigDog(),CuteCat()]
for animal in list:
    say_n_times(animal,2)
    print('-------------')

angry = BigAngryDog()
say_n_times(angry,5)


animal = Animal()
animal.speak()

dog = Dog()
say_n_times(dog,5)

bobik = BigDog()
bobik.speak()

small_bobik = SmallDog()
small_bobik.speak()

Toy = ToyDog()
Toy.speak()

rodot = RobotDog()
rodot.speak()

angry = BigAngryDog()
say_n_times(angry,5)

cat = Cat()
say_n_times(cat,5)

cute = CuteCat()
say_n_times(cute,5)
