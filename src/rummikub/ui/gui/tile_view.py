from src.rummikub.core.tile import Tile, Color
import pygame

THEMES = {
    'obsidian': {
        'name': 'Obsidian Noir',
        'table_bg': (15, 17, 22),
        'table_center': (24, 27, 36),
        'tile_body': (25, 27, 34),
        'tile_border': (56, 62, 76),
        'bevel_light': (72, 79, 96),
        'bevel_dark': (10, 11, 15),
        'inner_groove': (35, 38, 48),
        'joker': (244, 114, 182),
        'joker_accent': (251, 191, 36),
        Color.RED: (248, 79, 88),
        Color.BLUE: (56, 189, 248),
        Color.YELLOW: (251, 191, 36),
        Color.BLACK: (241, 245, 249),
    },
    'ivory': {
        'name': 'Marfim Nobre',
        'table_bg': (15, 17, 22),
        'table_center': (24, 27, 36),
        'tile_body': (246, 244, 238),
        'tile_border': (212, 206, 194),
        'bevel_light': (255, 255, 255),
        'bevel_dark': (180, 174, 160),
        'inner_groove': (235, 230, 220),
        'joker': (146, 64, 14),
        'joker_accent': (180, 83, 9),
        Color.RED: (186, 26, 36),
        Color.BLUE: (26, 68, 130),
        Color.YELLOW: (184, 115, 9),
        Color.BLACK: (26, 28, 32),
    }
}

colors = {
    'background': THEMES['obsidian']['tile_body'],
    'border': THEMES['obsidian']['tile_border'],
    'joker': THEMES['obsidian']['joker'],
    Color.RED: THEMES['obsidian'][Color.RED],
    Color.BLUE: THEMES['obsidian'][Color.BLUE],
    Color.YELLOW: THEMES['obsidian'][Color.YELLOW],
    Color.BLACK: THEMES['obsidian'][Color.BLACK],
}


class TileRender:
    def __init__(self, screen, tile: Tile, x: int, y: int, width: int = 62, height: int = 90, theme: str = 'obsidian'):
        self.screen = screen
        self.tile = tile
        self.x = int(x)
        self.y = int(y)
        self.coords = (self.x, self.y)
        self.w = int(width)
        self.h = int(height)
        self.theme_key = theme
        self.theme = THEMES.get(theme, THEMES['obsidian'])

        self.font = pygame.font.SysFont("segoeui,trebuchetms,helvetica,arial", 34, bold=True)
        self.mini_font = pygame.font.SysFont("segoeui,trebuchetms,helvetica,arial", 9, bold=True)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        th = self.theme

        shadow_surf = pygame.Surface((self.w + 20, self.h + 20), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 35), (10, 12, self.w, self.h), border_radius=10)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 70), (10, 9, self.w, self.h), border_radius=9)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 110), (10, 6, self.w, self.h), border_radius=8)
        self.screen.blit(shadow_surf, (self.x - 10, self.y - 4))

        light_rect = pygame.Rect(self.x - 1, self.y - 1, self.w + 2, self.h + 2)
        pygame.draw.rect(self.screen, th['bevel_light'], light_rect, border_radius=9)

        dark_rect = pygame.Rect(self.x, self.y + 1, self.w + 1, self.h + 1)
        pygame.draw.rect(self.screen, th['bevel_dark'], dark_rect, border_radius=9)

        body_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, th['tile_body'], body_rect, border_radius=8)

        pygame.draw.rect(self.screen, th['tile_border'], body_rect, width=1, border_radius=8)

        inner_rect = pygame.Rect(self.x + 3, self.y + 3, self.w - 6, self.h - 6)
        pygame.draw.rect(self.screen, th['inner_groove'], inner_rect, width=1, border_radius=5)

        if self.tile.is_joker:
            accent_color = th['joker']
            self._draw_joker(accent_color)
        else:
            accent_color = th[self.tile.color]
            text_str = str(self.tile.value)
            text_surf = self.font.render(text_str, True, accent_color)
            text_rect = text_surf.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2 - 5))
            self.screen.blit(text_surf, text_rect)

        bar_w = 20
        bar_h = 2
        bar_x = self.x + (self.w - bar_w) // 2
        bar_y = self.y + self.h - 13

        bar_surf = pygame.Surface((bar_w, bar_h), pygame.SRCALPHA)
        bar_surf.fill((*accent_color[:3], 160))
        self.screen.blit(bar_surf, (bar_x, bar_y))

    def _draw_joker(self, color):
        cx = self.x + self.w // 2
        cy = self.y + self.h // 2 - 9

        crown_points = [
            (cx - 14, cy + 6),
            (cx + 14, cy + 6),
            (cx + 15, cy - 5),
            (cx + 7, cy + 1),
            (cx, cy - 12),
            (cx - 7, cy + 1),
            (cx - 15, cy - 5),
        ]
        pygame.draw.polygon(self.screen, color, crown_points)

        pygame.draw.circle(self.screen, color, (cx - 15, cy - 5), 2.5)
        pygame.draw.circle(self.screen, color, (cx, cy - 12), 3)
        pygame.draw.circle(self.screen, color, (cx + 15, cy - 5), 2.5)

        band_rect = pygame.Rect(cx - 13, cy + 8, 26, 2.5)
        pygame.draw.rect(self.screen, color, band_rect, border_radius=1)

        caption = self.mini_font.render("J O K E R", True, color)
        caption_rect = caption.get_rect(center=(cx, cy + 19))
        self.screen.blit(caption, caption_rect)