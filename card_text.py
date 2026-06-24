import pygame
import carte

# initialize pygame
pygame.init()

# screen settings
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800
CARD_WIDTH = 137
CARD_HEIGHT = 216
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),display=1)
pygame.display.set_caption('Card Text Demo')


# fonts
TITLE_FONT = pygame.font.Font(None, 28)
VALUE_FONT = pygame.font.Font(None, 28)

# coordinate variables for 3 cards and 9 text slots
CARD_POSITIONS = [(8, 575), (157, 575), (306, 575)]
CARD_VALUE_POSITIONS = [
    [
        (card_x + 40, card_y + 200),
        (card_x + 65, card_y + 180),
        (card_x + 90, card_y + 200),
    ]
    for card_x, card_y in CARD_POSITIONS
]


# card image names by tipo
CARD_IMAGES = {
    0: 'assets/carta_debole.png',
    1: 'assets/carta_media.png',
    2: 'assets/carta_forte.png',
}

BACKGROUND_COLOR = (30, 30, 40)
TEXT_COLOR = (0, 0, 0)


def draw_card_values(screen, card, card_index):
    positions = CARD_VALUE_POSITIONS[card_index]
    texts = [str(card.costo), str(card.power), str(card.vita)]

    for value_text, pos in zip(texts, positions):
        text_surface = VALUE_FONT.render(value_text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=pos)
        screen.blit(text_surface, text_rect)


def load_card_image(tipo):
    path = CARD_IMAGES.get(tipo, CARD_IMAGES[0])
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))


def make_cards():
    return [carte.spawn_carte() for _ in range(3)]


def main():
    clock = pygame.time.Clock()
    cards = make_cards()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cards = make_cards()

        SCREEN.fill(BACKGROUND_COLOR)

        for index, card in enumerate(cards):
            card_pos = CARD_POSITIONS[index]
            image = load_card_image(card.tipo)
            SCREEN.blit(image, card_pos)
            draw_card_values(SCREEN, card, index)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()

