import pygame
import sys
import os
import subprocess

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
BG_IMAGE = os.path.join(ASSETS_DIR, 'background2_menu.png')

def rounded_rect(surface, rect, color, radius=20):
    x, y, w, h = rect
    pygame.draw.rect(surface, color, (x+radius, y, w-2*radius, h))
    pygame.draw.rect(surface, color, (x, y+radius, w, h-2*radius))
    pygame.draw.circle(surface, color, (x+radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+w-radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+radius, y+h-radius), radius)
    pygame.draw.circle(surface, color, (x+w-radius, y+h-radius), radius)

class Button:
    def __init__(self, rect, text, font, action=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.action = action

    def draw(self, surf, hover=False):
        base = (230, 190, 30)
        light = (255, 220, 80)
        color = light if hover else base
        rounded_rect(surf, self.rect, color, radius=24)
        pygame.draw.rect(surf, (200,160,20), self.rect, 4, border_radius=24)
        txt = self.font.render(self.text, True, (30, 30, 30))
        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)

def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 800))
    pygame.display.set_caption('YOU WON!!')
    clock = pygame.time.Clock()

    bg = pygame.image.load(BG_IMAGE).convert() if os.path.exists(BG_IMAGE) else pygame.Surface(screen.get_size())
    bg = pygame.transform.scale(bg, screen.get_size())

    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Blue Water.otf')
    font = pygame.font.Font(font_path, 40)
    title_font = pygame.font.Font(font_path, 60)



    w, h = 420, 90
    cx = screen.get_width()//2 - w//2
    retry_btn = Button((cx, 300, w, h), 'Replay', font, action='Replay')
    quit_btn = Button((cx, 420, w, h), 'Quit', font, action='quit')
    buttons = [retry_btn, quit_btn]

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for b in buttons:
                    if b.is_hover(mouse):
                        if b.action == 'replay':
                            subprocess.run(f'{sys.executable} main.py')
                            pygame.quit(); return
                        if b.action == 'quit':
                            running = False

        screen.blit(bg, (0, 0))
        title = title_font.render('YOU WON!!!', True, (0, 250, 0))
        screen.blit(title, title.get_rect(center=(screen.get_width()//2, 180)))
        for b in buttons:
            b.draw(screen, hover=b.is_hover(mouse))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
