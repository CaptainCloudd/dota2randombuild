import random

with open("itemlist.txt", "r") as tf:
    items = tf.read().split(',')

with open("bootslist.txt", "r") as tf:
    boots = tf.read().split(',')

with open("herolist.txt", "r") as tf:
    heroes = tf.read().split(',')

    
buildrandom = random.choices(items, k = 5)
bootsrandom = random.choices(boots)
herorandom = random.choices(heroes)

print('Hero: ' + str(herorandom))
print('Build: ' + str(buildrandom) + str(bootsrandom))

