from random import randint

# тренажер для Марьиванны

student = input('представтесь,пожалуйста:')
try:
    level = int(input('Выберете уровень сложности 1-5:'))
except:
    level = 1
    print('установлен первый уровень сложности.')
if level < 1 or level > 5:
    print('установлен первый уровень сложности.')
print(f'Хорошо,{student}.Тебе задачка')

min = 1**(level - 1)
max = 10**(level - 1)
points = 0

for i in range(5):
    a = randint(min, max)
    b = randint(min, max)
    print(f'{student},сколько будет {a} + {b}?', end='')
    correct_answer = a + b
    student_answer = input()
    if student_answer == str(correct_answer):
        points += 1
        print(f'Правильно.')
    else:
        print(f'Не правильно.Правильный ответ {correct_answer}!')
if points == 5:
    print(f'Ах, ну какой умница,{student}.Это пять!')
if points == 4:
    print(f'Молодец, {student}, но можно лучше.Четыре')
if points == 3:
    print(f'Так себе,{student}.Садись, три.')
else:
    print(f'Два,{student},можешь садиться!')