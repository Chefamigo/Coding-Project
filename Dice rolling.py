import random

dice_side = int(input("Enter dice wanting to roll:"))
dice_amount = int(input("Enter amount of dice:"))

while dice_amount >= 1 and dice_side == 100:
    print(random.randrange(1 , 100))
    dice_amount = dice_amount - 1

while dice_amount >= 1 and dice_side == 20:
    print(random.randrange(1 , 20))
    dice_amount = dice_amount - 1

while dice_amount >= 1 and dice_side == 12:
    print(random.randrange(1 , 12))
    dice_amount = dice_amount - 1

while dice_amount >= 1 and dice_side == 6:
    print(random.randrange(1 , 6))
    dice_amount = dice_amount - 1

while dice_amount >= 1 and dice_side == 3:
    print(random.randrange(1 , 3))
    dice_amount = dice_amount - 1
