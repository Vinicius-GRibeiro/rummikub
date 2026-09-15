import pygame
from src.rummikub.core.player import Player
from src.rummikub.core.tile import Tile
from src.rummikub.ui.gui.tile_view import TileRender


class RackView:
    def __init__(self, screen: pygame.Surface, player: Player, rect: pygame.Rect):
        self.screen = screen
        self.player = player
        self.rect = rect

        self.tile_w = 60
        self.tile_h = 86
        self.spacing = 68

        self.selected_indices: set[int] = set()
        self.hovered_index: int | None = None
        self._slot_rects: list[tuple[int, Tile, pygame.Rect]] = []

    def handle_click(self, mouse_pos: tuple[int, int]) -> bool:
        for idx, tile, rect in self._slot_rects:
            if rect.collidepoint(mouse_pos):
                if idx in self.selected_indices:
                    self.selected_indices.remove(idx)
                else:
                    self.selected_indices.add(idx)
                return True
        return False

    def update_hover(self, mouse_pos: tuple[int, int]) -> bool:
        self.hovered_index = None
        for idx, tile, rect in self._slot_rects:
            if rect.collidepoint(mouse_pos):
                self.hovered_index = idx
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return False

    def clear_selection(self):
        self.selected_indices.clear()

    def get_selected_tiles(self) -> list[Tile]:
        return [self.player.rack[i] for i in sorted(self.selected_indices) if i < len(self.player.rack)]

    def remove_selected_from_player(self):
        sorted_indices = sorted(self.selected_indices, reverse=True)
        for idx in sorted_indices:
            if idx < len(self.player.rack):
                self.player.rack.pop(idx)
        self.clear_selection()

    def draw(self, theme: str = 'obsidian'):
        self._slot_rects.clear()

        start_x = self.rect.x + 25
        base_y = self.rect.y + 40

        for idx, tile in enumerate(self.player.rack):
            col = idx % 14
            row = idx // 14

            x = start_x + col * self.spacing
            y = base_y + row * (self.tile_h + 14)

            is_selected = idx in self.selected_indices
            is_hovered = (idx == self.hovered_index) and not is_selected

            if is_selected:
                draw_y = y - 12
            elif is_hovered:
                draw_y = y - 4
            else:
                draw_y = y

            renderer = TileRender(
                self.screen,
                tile,
                x=x,
                y=draw_y,
                width=self.tile_w,
                height=self.tile_h,
                theme=theme
            )
            renderer.draw()

            current_rect = pygame.Rect(x, draw_y, self.tile_w, self.tile_h)
            self._slot_rects.append((idx, tile, current_rect))

            if is_selected:
                highlight_rect = pygame.Rect(x - 2, draw_y - 2, self.tile_w + 4, self.tile_h + 4)
                pygame.draw.rect(self.screen, (251, 191, 36), highlight_rect, width=2, border_radius=10)
            elif is_hovered:
                hover_rect = pygame.Rect(x - 1, draw_y - 1, self.tile_w + 2, self.tile_h + 2)
                pygame.draw.rect(self.screen, (130, 150, 180), hover_rect, width=1, border_radius=9)
