import pygame
import carte

# fonts
TITLE_FONT = pygame.font.Font(None, 36)
VALUE_FONT = pygame.font.Font(None, 28)

# coordinate variables for 3 cards and 9 text slots
CARD_POSITIONS = [(8, 575), (157, 575), (306, 575)]
CARD_VALUE_POSITIONS = [
    [
        (card_x + 64, card_y + 167),
        (card_x + 38, card_y + 187),
        (card_x + 90, card_y + 187),
    ]
    for card_x, card_y in CARD_POSITIONS
]

# optional: flatten all 9 slots in a single variable
ALL_SLOT_COORDINATES = [pos for card in CARD_VALUE_POSITIONS for pos in card]

# card image names by tipo
CARD_IMAGES = {
    0: 'assets/carta_debole.png',
    1: 'assets/carta_media.png',
    2: 'assets/carta_forte.png',
}

TEXT_COLOR = (255, 255, 255)

# Colori delle box per ogni slot: costo, potere, vita
SLOT_COLORS = [
    (255, 255, 0),    # slot 0 (costo) = giallo
    (255, 0, 0),      # slot 1 (potere) = rosso
    (0, 255, 0),      # slot 2 (vita) = verde
]

BOX_BORDER_RADIUS = 6


def draw_card_values(screen, card, card_index):
    positions = CARD_VALUE_POSITIONS[card_index]
    texts = [str(card.costo), str(card.power), str(card.vita)]

    for slot_i, (value_text, pos) in enumerate(zip(texts, positions)):
        text_surface = VALUE_FONT.render(value_text, True, (0, 0, 0))
        box = pygame.Rect(pos[0] - 24, pos[1] - 2, text_surface.get_width() + 42, text_surface.get_height() + 1)
        # disegna box con angoli smussati e colore specifico per ogni slot
        box_color = SLOT_COLORS[slot_i]
        pygame.draw.rect(screen, box_color, box, border_radius=BOX_BORDER_RADIUS)
        # blit del testo centrato sulla box
        text_rect = text_surface.get_rect(center=box.center)
        screen.blit(text_surface, text_rect)

