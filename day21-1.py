#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict

def return_dice_rolls(value):
    return 3 * ((value+1)%100)

if __name__ == '__main__':
    deterministic_dice = 1
    total_player_1 = 0
    position_player_1 = 7
    total_player_2 = 0
    position_player_2 = 3
    dice_roll_count = 0
    loser_value = 0
    while (total_player_1 < 1000 and total_player_2 < 1000):
        dice_roll_count += 6
        new_position_player_1 = (position_player_1 + return_dice_rolls(deterministic_dice))% 10
        new_position_player_2 = (position_player_2 + return_dice_rolls(deterministic_dice + 3)) % 10
        if new_position_player_1 == 0:
            new_position_player_1 = 10
        if new_position_player_2 == 0:
            new_position_player_2 = 10
        total_player_1 += new_position_player_1
        if (total_player_1 >= 1000):
            break
        total_player_2 += new_position_player_2
        deterministic_dice += 6
        position_player_1 = new_position_player_1
        position_player_2 = new_position_player_2
    print (dice_roll_count - 3 , min(total_player_1,total_player_2))
    print ((dice_roll_count -3)* min(total_player_1,total_player_2))
