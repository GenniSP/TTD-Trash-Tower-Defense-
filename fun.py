#import pygame

def click_card(x_pos, y_pos, screen_height, screen_width, card_width, card_height):
    space_between = ((screen_width - card_width*3))/4
    y_offset = 10
    if (space_between < x_pos < space_between+card_width) and (screen_height-card_height-y_offset < y_pos < screen_height-y_offset):
        return 0
    elif (space_between*2+card_width < x_pos < space_between*2+card_width*2) and (screen_height-card_height-y_offset < y_pos < screen_height-y_offset):
        return 1
    elif (space_between*3+card_width*2 < x_pos < space_between*3+card_width*3) and (screen_height-card_height-y_offset < y_pos < screen_height-y_offset):
        return 2
    else:
        return -1
    
def good_position(x_pos, y_pos):
    if x_pos<=102 and y_pos<=554 and y_pos>=510 and x_pos>=58:
        return 0
    if x_pos<=252 and y_pos<=554 and y_pos>=510 and x_pos>=208:   
        return 1
    if x_pos<=406 and y_pos<=554 and y_pos>=510 and x_pos>=362:
        return 2
    return -1