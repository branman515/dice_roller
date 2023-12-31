import random
import os


class Dice_roller:
    #Asks for input on how many dice you wish to roll. 
    #In future iterations, I want to ask for number and type of die (4,6,8,10,12,100)
    def num_die(self):
        while True:
            try:
                num_dice = input('Number of dice: ')
                valid_responses = ['1', '2']
                if num_dice not in valid_responses:
                    raise ValueError('1 or 2 only')
                else:
                    return int(num_dice)
            except ValueError as err:
                print(err)

    #Rolls all dice to return array of all rolls
    def roll(self, num_dice):
        min_val = 1
        max_val = 6
        roll_again = 'y'
        total = 0
        dice_rolls = []

        print("Rolling dice")
        for i in range(num_dice):
            die_num = random.randint(min_val, max_val)
            total += die_num
            dice_rolls.append(die_num)
            
    
        return dice_rolls
