import pygame
from src.rummikub.core.board import Board
from src.rummikub.ui.gui.tile_view import TileRender


class BoardView:
    def __init__(self, screen: pygame.Surface, board: Board, rect: pygame.Rect):
        self.screen = screen
        self.board = board
        self.rect = rect

        self.tile_w = 54
        self.tile_h = 78
        self.tile_gap = 4
        self.meld_gap = 32
        self.line_gap = 20

        self.empty_font = pygame.font.SysFont("segoeui,trebuchetms,arial", 14, bold=False)

    def draw(self, theme: str = 'obsidian'):
        if len(self.board) == 0:
            self._draw_empty_placeholder()
            return

        cursor_x = self.rect.x
        cursor_y = self.rect.y

        for meld in self.board.melds:
            num_tiles = len(meld)
            meld_width = num_tiles * self.tile_w + (num_tiles - 1) * self.tile_gap

            if cursor_x + meld_width > self.rect.right and cursor_x > self.rect.x:
                cursor_x = self.rect.x
                cursor_y += self.tile_h + self.line_gap

            for tile in meld.tiles:
                renderer = TileRender(
                    self.screen,
                    tile,
                    x=cursor_x,
                    y=cursor_y,
                    width=self.tile_w,
                    height=self.tile_h,
                    theme=theme
                )
                renderer.draw()
                cursor_x += self.tile_w + self.tile_gap

            cursor_x += (self.meld_gap - self.tile_gap)

    def _draw_empty_placeholder(self):
        text_surf = self.empty_font.render(
            "Mesa vazia",
            True,
            (90, 100, 120)
        )
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.screen.blit(text_surf, text_rect)