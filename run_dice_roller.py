from DiceRoll import dice_roller as Dice_roller
#Main
if __name__ == '__main__':
    dice_roller = Dice_roller.Dice_roller()
    num_dice = dice_roller.num_die()
    dice_rolls = dice_roller.roll(num_dice)
    for i in range(len(dice_rolls)):
        print(f"Die: {i+1}: {dice_rolls[i]}")