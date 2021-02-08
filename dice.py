# roll the dice
from random import randint 

print('roll the dice')
roll=(randint(1,7))
print(roll)
print(' _______')
if roll ==1:
    print('|       |\n|   o   |\n|       |')
elif roll ==2:
    print('|      o|\n|       |')
    print('|o      |')
elif roll ==3:
    print('|      o|')
    print('|   o   |')
    print('|o      |')
elif roll ==4:
    print('|o     o|\n|       |')
    print('|o     o|')
elif roll ==5:
    print('|o     o|')
    print('|   o   |')
    print('|o     o|')
elif roll ==6:
    print('|o     o|')
    print('|o     o|')
    print('|o     o|')
else: 
    roll ==7
    print('Try again - is not possible!')
print(' _______\n\n')
