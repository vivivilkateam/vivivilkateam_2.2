from random import randint

student = input('представтесь, пожалуйста:')
try:
    level = int(input('Выберите уровень сложнасти 1-5:'))
except:
    level = 1
    print('установлен первый уровень сложности.')
if level < 1 or level > 5:
    level = 1
    print("установлен первый уровень сложности:")

print(f'Хорошо,{student}.Проверь свои знания географии.')

questions = [('Столица Фрнанции?', 'Париж'),
             ('Самая длинная река в мире?', 'Амазонка'),
             ('Самая высокая гора в мире?', "Эверест"),
             ("Какой океан самый большой?", "Тихий океан"),
             ("Какой контенент самый большой?", 'Австралия')]

points = 0
for i in range(5):
    question = questions[randint(0, len(questions) - 1)]
    print(f'{student},{question[0]}')
    answer = input('Твой ответ:')

    if answer.lower() == question[1].lower():
        points += 1
        print('Правильно!')
    else:
        print(f'Неправильно.Правильный ответ:{question[1]}')

if points == 5:
    print(f'Удевительно,{student},ты настоящий знаток географии!')
elif points >= 3:
    print(f'Молодец,{student}.Ты справился на {points} правильных ответов.')
else:
    print(f'Плохо,{student}.Всего {points} правильны ответов')