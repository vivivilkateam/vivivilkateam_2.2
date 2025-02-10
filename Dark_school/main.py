import person
import tkinter
pers = person.Units(100,100,100,2,15)
pl1 = person.game_player(100,100,100,2,15,50,'шлем','меч',100)
en1 = person.game_enemy(200,100,75,3,10,25,34,'кинжалы')
en2 = person.game_enemy(100,200,150,1,30,75,97,'дубина')
print(str(pers))
print(str(pl1))
print(str(en1))
print(str(en2))
