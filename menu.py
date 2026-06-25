import pygame
import sys
import os
import subprocess


# Optional moviepy for video playback
try:
    from moviepy.editor import VideoFileClip
    MOVIEPY_AVAILABLE = True
except Exception:
    MOVIEPY_AVAILABLE = False


ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
BG_IMAGE = os.path.join(ASSETS_DIR, 'background2_menu.png')
TUTORIAL_VIDEO = os.path.join(ASSETS_DIR, 'tutorial_video.mp4')


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
        # yellowy gradient
        base = (230, 190, 30)
        light = (255, 220, 80)
        color = light if hover else base
        rounded_rect(surf, self.rect, color, radius=24)
        # border
        pygame.draw.rect(surf, (200,160,20), self.rect, 4, border_radius=24)
        # text
        txt = self.font.render(self.text, True, (30, 30, 30))
        txt_r = txt.get_rect(center=self.rect.center)
        surf.blit(txt, txt_r)

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)


def play_tutorial(screen, clock):
    if not MOVIEPY_AVAILABLE or not os.path.exists(TUTORIAL_VIDEO):
        # simple fallback message
        font = pygame.font.SysFont(None, 36)
        t = 0
        while t < 2000:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if ev.type == pygame.KEYDOWN:
                    return
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load(BG_IMAGE).convert(), (0, 0))
            msg = font.render('Tutorial unavailable. ', True, (255,255,255))
            msg1 = font.render('Press any key to return.', True, (255,255,255))
            screen.blit(msg, msg.get_rect(center=screen.get_rect().center))
            pygame.display.flip()
            clock.tick(30)
            t += clock.get_time()
        return

    clip = VideoFileClip(TUTORIAL_VIDEO)
    clip = clip.resize(height=screen.get_height())
    for frame in clip.iter_frames(fps=24, dtype='uint8'):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                clip.close()
                return
        # moviepy frames are RGB; pygame wants (w,h,3)
        surf = pygame.surfarray.make_surface(frame.swapaxes(0,1))
        screen.blit(surf, (0,0))
        pygame.display.flip()
        clock.tick(24)
    clip.close()


def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 800))
    pygame.display.set_caption('Menu')
    clock = pygame.time.Clock()

    # load background
    if os.path.exists(BG_IMAGE):
        bg = pygame.image.load(BG_IMAGE).convert()
        bg = pygame.transform.scale(bg, screen.get_size())
    else:
        bg = pygame.Surface(screen.get_size())
        bg.fill((40, 40, 60))

    font = pygame.font.SysFont(None, 40)

    w = 420
    h = 90
    cx = screen.get_width()//2 - w//2
    start_btn = Button((cx, 180, w, h), 'Start Game', font, action='start')
    tut_btn = Button((cx, 300, w, h), 'Play Tutorial', font, action='tutorial')
    quit_btn = Button((cx, 420, w, h), 'Quit', font, action='quit')

    buttons = [start_btn, tut_btn, quit_btn]

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for b in buttons:
                    if b.is_hover(mouse):
                        if b.action == 'start':
                            # try to run main.py in same folder
                            mp = os.path.join(os.path.dirname(__file__), 'main.py')
                            if os.path.exists(mp):
                                subprocess.Popen([sys.executable, mp])
                                pygame.quit(); return
                        if b.action == 'tutorial':
                            play_tutorial(screen, clock)
                        if b.action == 'quit':
                            running = False

        screen.blit(bg, (0, 0))
        title_font = pygame.font.SysFont(None, 62)
        title = title_font.render('Trash Tower Defense', True, (250, 240, 200))
        screen.blit(title, title.get_rect(center=(screen.get_width()//2, 80)))

        for b in buttons:
            b.draw(screen, hover=b.is_hover(mouse))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
