import pygame


class Button:
    def __init__(
        self,
        rect: pygame.Rect,
        text: str,
        bg_color: tuple[int, int, int] = (35, 40, 52),
        hover_color: tuple[int, int, int] = (50, 58, 76),
        text_color: tuple[int, int, int] = (225, 230, 240),
        border_color: tuple[int, int, int] = (60, 70, 90),
        border_radius: int = 8,
        font_size: int = 13,
    ):
        self.rect = rect
        self.text = text
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_color = border_color
        self.border_radius = border_radius

        self.font = pygame.font.SysFont("segoeui,trebuchetms,arial", font_size, bold=True)
        self.is_hovered = False

    def update(self, mouse_pos: tuple[int, int]) -> bool:
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        return self.is_hovered

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen: pygame.Surface):
        color = self.hover_color if self.is_hovered else self.bg_color

        pygame.draw.rect(screen, color, self.rect, border_radius=self.border_radius)
        if self.border_color:
            pygame.draw.rect(screen, self.border_color, self.rect, width=1, border_radius=self.border_radius)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
