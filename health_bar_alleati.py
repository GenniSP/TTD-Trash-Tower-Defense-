import pygame
import fun

pygame.font.init()
max_health = 150
current_health = max_health

health_bar_x = 10
health_bar_y = 33
health_bar_width = 150
health_bar_height = 25

def current_health_alleati(subtract_health):
    if subtract_health == 25 :
        current_health = current_health - 25
    return (current_health, subtract_health)
    

color_red = (0, 255, 0)
color_gray = (200, 200, 200)
color_black = (0, 0, 0)

game_font = pygame.font.Font(None, 25)  

def draw_health_bar(myScreen):
    current_width = (current_health / max_health) * health_bar_width
    
    pygame.draw.rect(myScreen, color_gray, 
                     (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
    pygame.draw.rect(myScreen, color_red, 
                     (health_bar_x, health_bar_y, current_width, health_bar_height))
    pygame.draw.rect(myScreen, color_black, 
                     (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)
    
    hp_text = game_font.render(str(current_health), True, color_black)
    text_rect = hp_text.get_rect(center=(health_bar_x + health_bar_width // 2, 
                                          health_bar_y + health_bar_height // 2))

    myScreen.blit(hp_text,text_rect)