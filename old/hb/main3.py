from hitbox import Hitbox


#1
hb1 = Hitbox(0,100,100,100)

#2
hb2 = Hitbox(90,100,100,100)

#3
hb3 = Hitbox(220,100,100,100)

print(f'верхняя граница hb1: {hb1.top},'
      f'верхняя граница hb2: {hb2.top},'
      f'верхняя граница hb3: {hb3.top},')
print(f'нижния граница hb1: {hb1.bottom},'
      f'нижния граница hb2: {hb2.bottom},'
      f'нижния граница hb3: {hb3.bottom},')
print(f'левая граница hb1: {hb1.left},'
      f'левая граница hb2: {hb2.left},'
      f'левая граница hb3: {hb3.left},')
print(f'правая граница hb1: {hb1.right},'
      f'правая граница hb2: {hb2.right},'
      f'правая граница hb3: {hb3.right},')

intersects = hb1.intersects(hb2)
intersects1 = hb1.intersects1(hb3)
intersects2 = hb2.intersects(hb3)

print(intersects)
print(intersects2)
print(intersects1)