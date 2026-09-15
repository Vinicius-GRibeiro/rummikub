import pygame
from src.rummikub.core.tile import Tile, Color
from src.rummikub.ui.gui.tile_view import TileRender, THEMES

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rummikub")

clock = pygame.time.Clock()

TABLE_BG = (15, 17, 22)
TABLE_BORDER = (34, 38, 48)
TEXT_TITLE = (220, 225, 235)
TEXT_MUTED = (110, 120, 140)

sample_group = [
    Tile(Color.RED, 8),
    Tile(Color.BLUE, 8),
    Tile(Color.YELLOW, 8),
    Tile(Color.BLACK, 8),
]

sample_run = [
    Tile(Color.BLUE, 7),
    Tile(Color.BLUE, 8),
    Tile.create_joker(),
    Tile(Color.BLUE, 10),
    Tile(Color.BLUE, 11),
]

sample_hand = [
    Tile(Color.RED, 1),
    Tile(Color.RED, 13),
    Tile(Color.YELLOW, 5),
    Tile(Color.BLACK, 12),
    Tile(Color.BLUE, 3),
    Tile.create_joker(),
]

font_title = pygame.font.SysFont("segoeui,trebuchetms,arial", 20, bold=True)
font_label = pygame.font.SysFont("segoeui,trebuchetms,arial", 12, bold=True)
font_help = pygame.font.SysFont("segoeui,trebuchetms,arial", 12)

current_theme = 'obsidian'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                current_theme = 'ivory' if current_theme == 'obsidian' else 'obsidian'

    screen.fill(TABLE_BG)
    table_rect = pygame.Rect(25, 25, SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50)
    pygame.draw.rect(screen, TABLE_BORDER, table_rect, width=1, border_radius=16)

    lbl_group = font_label.render("", True, TEXT_MUTED)
    screen.blit(lbl_group, (50, 120))
    spacing = 76
    for i, tile in enumerate(sample_group):
        renderer = TileRender(screen, tile, 50 + i * spacing, 145, theme=current_theme)
        renderer.draw()

    lbl_run = font_label.render("", True, TEXT_MUTED)
    screen.blit(lbl_run, (450, 120))
    for i, tile in enumerate(sample_run):
        renderer = TileRender(screen, tile, 450 + i * spacing, 145, theme=current_theme)
        renderer.draw()

    rack_y = 440
    rack_rect = pygame.Rect(40, rack_y - 20, SCREEN_WIDTH - 80, 170)
    pygame.draw.rect(screen, (22, 25, 33) if current_theme == 'obsidian' else (30, 33, 42), rack_rect, border_radius=12)
    pygame.draw.rect(screen, (40, 45, 58), rack_rect, width=1, border_radius=12)

    lbl_rack = font_label.render("SUA MÃO:", True, TEXT_MUTED)
    screen.blit(lbl_rack, (60, rack_y - 5))

    for i, tile in enumerate(sample_hand):
        renderer = TileRender(screen, tile, 60 + i * spacing, rack_y + 25, theme=current_theme)
        renderer.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()