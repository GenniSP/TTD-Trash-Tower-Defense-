#import pygame

def click_card(x_pos, y_pos, screen_height, screen_width, card_width, card_height):
    space_between = ((screen_width - card_width*3))/4
    if (space_between < x_pos < space_between+card_width) and (screen_height-card_height < y_pos < screen_height):
        return 0
    elif (space_between*2+card_width < x_pos < space_between*2+card_width*2) and (screen_height-card_height < y_pos < screen_height):
        return 1
    elif (space_between*3+card_width*2 < x_pos < space_between*3+card_width*3) and (screen_height-card_height < y_pos < screen_height):
        return 2
    else:
        return "no click"