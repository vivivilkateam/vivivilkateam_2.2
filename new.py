class Animal:
    def speak(self):
        print('издавать звуки')

class Dog(Animal):
    def speak(self):
        print('Гав-Гав')
class BigDog(Dog):
    def speak(self):
        print('Вау-Вау')


class SmallDog(Dog):
    def speak(self):
        print('Тяф-Тяф')

class ToyDog(SmallDog):
    def speak(self):
        print('игрушка собачка')

class RoboDog(ToyDog):
    def speak(self):
        print('Г-А-В Г-А-В')

class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print('БОЛЬШАЯ СОБАКА')
        print('БОЙСЯ МЕНЯ')

class Cat(Animal):
    def _meow(self):
        print('Мяу-Мяу')
    def speak(self):
        self._meow()

class Cat001(Cat):
    def _meow(self):
        print('мяу 1')



animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

big_dog = BigDog()
big_dog.speak()

small_dog = SmallDog()
small_dog.speak()

toy_dog = ToyDog()
toy_dog.speak()

robo_dog = RoboDog()
robo_dog.speak()

big_angry_dog = BigAngryDog()
big_angry_dog.speak()

cat = Cat()
cat.speak()

cat001 = Cat001()
cat001.speak()
print("--------------------------------------")
def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()



druzok = BigAngryDog()
say_n_times(druzok, 3)

kotik_Vasua = Cat()
say_n_times(kotik_Vasua, 5)
print("--------------------------------------")


list_of_animal = [Cat(),Dog(),Cat001(),SmallDog(),BigAngryDog(),RoboDog()]
for animal in list_of_animal:
    animal.speak()
print("--------------------------------------")
for animal in list_of_animal:
    say_n_times(animal, 2)
