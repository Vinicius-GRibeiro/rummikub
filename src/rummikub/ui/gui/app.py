import pygame
from src.rummikub.core.tile import Tile, Color
from src.rummikub.core.meld import Group, Run
from src.rummikub.core.game import Game
from src.rummikub.ui.gui.board_view import BoardView
from src.rummikub.ui.gui.rack_view import RackView
from src.rummikub.ui.gui.widgets import Button

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 760
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rummikub - Obsidian Noir Edition")

clock = pygame.time.Clock()

TABLE_BG = (15, 17, 22)
HEADER_BG = (20, 23, 30)
HEADER_BORDER = (38, 43, 55)
BOARD_PANEL_BG = (20, 23, 30)
BOARD_PANEL_BORDER = (38, 43, 55)
TEXT_LIGHT = (230, 235, 245)
TEXT_MUTED = (110, 120, 140)

game = Game(["Jogador 1", "Jogador 2"])
game.start_game()

board_rect = pygame.Rect(40, 75, SCREEN_WIDTH - 80, 350)
board_view = BoardView(
    screen,
    game.board,
    pygame.Rect(board_rect.x + 20, board_rect.y + 35, board_rect.w - 40, board_rect.h - 50)
)

rack_y = 445
rack_rect = pygame.Rect(40, rack_y, SCREEN_WIDTH - 80, 280)
rack_view = RackView(
    screen,
    game.current_player,
    pygame.Rect(rack_rect.x, rack_rect.y + 35, rack_rect.w, rack_rect.h - 90)
)

btn_sort_color = Button(pygame.Rect(60, rack_rect.bottom - 45, 130, 32), "Ordenar Cor")
btn_sort_value = Button(pygame.Rect(200, rack_rect.bottom - 45, 140, 32), "Ordenar Número")
btn_clear_sel = Button(pygame.Rect(350, rack_rect.bottom - 45, 120, 32), "Limpar Seleção")

btn_draw_tile = Button(
    pygame.Rect(SCREEN_WIDTH - 420, rack_rect.bottom - 45, 150, 32),
    "Comprar Peça",
    bg_color=(45, 52, 68),
    hover_color=(60, 70, 92),
    border_color=(80, 92, 120)
)

btn_play_meld = Button(
    pygame.Rect(SCREEN_WIDTH - 250, rack_rect.bottom - 45, 150, 32),
    "Baixar Jogo",
    bg_color=(34, 90, 60),
    hover_color=(45, 120, 80),
    border_color=(60, 160, 110)
)

buttons = [btn_sort_color, btn_sort_value, btn_clear_sel, btn_draw_tile, btn_play_meld]

font_header = pygame.font.SysFont("segoeui,trebuchetms,arial", 15, bold=True)
font_label = pygame.font.SysFont("segoeui,trebuchetms,arial", 12, bold=True)
font_feedback = pygame.font.SysFont("segoeui,trebuchetms,arial", 13, bold=True)
font_winner = pygame.font.SysFont("segoeui,trebuchetms,arial", 32, bold=True)

status_message = "Bem-vindo ao Rummikub! Selecione peças ou compre para jogar."
status_color = (130, 180, 240)
status_timer = 240

current_theme = 'obsidian'

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    is_any_hovered = False
    for btn in buttons:
        if btn.update(mouse_pos):
            is_any_hovered = True

    if rack_view.update_hover(mouse_pos):
        is_any_hovered = True

    if not is_any_hovered:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                current_theme = 'ivory' if current_theme == 'obsidian' else 'obsidian'
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game.winner is not None:
                continue

            if btn_sort_color.is_clicked(event.pos):
                game.current_player.sort_rack_by_color()
                rack_view.clear_selection()
            elif btn_sort_value.is_clicked(event.pos):
                game.current_player.sort_rack_by_value()
                rack_view.clear_selection()
            elif btn_clear_sel.is_clicked(event.pos):
                rack_view.clear_selection()
            elif btn_draw_tile.is_clicked(event.pos):
                try:
                    game.player_draw_tile()
                    rack_view.player = game.current_player
                    rack_view.clear_selection()
                    status_message = f"Peça comprada! Vez de {game.current_player.name}."
                    status_color = (130, 180, 240)
                    status_timer = 180
                except IndexError:
                    status_message = "O monte está vazio! Nenhuma peça restante."
                    status_color = (230, 80, 80)
                    status_timer = 180
            elif btn_play_meld.is_clicked(event.pos):
                selected = rack_view.get_selected_tiles()
                if len(selected) < 3:
                    status_message = "Selecione no mínimo 3 peças para formar um jogo!"
                    status_color = (230, 80, 80)
                    status_timer = 180
                else:
                    group_candidate = Group(selected)

                    sorted_for_run = sorted(
                        selected,
                        key=lambda t: 99 if t.is_joker else t.value
                    )
                    run_candidate = Run(sorted_for_run)

                    candidate_meld = None
                    if group_candidate.is_valid():
                        candidate_meld = group_candidate
                    elif run_candidate.is_valid():
                        candidate_meld = run_candidate

                    if candidate_meld is None:
                        status_message = "Combinação inválida! Não forma Grupo nem Sequência."
                        status_color = (230, 80, 80)
                        status_timer = 180
                    else:
                        try:
                            game.play_melds([candidate_meld])
                            board_view.board = game.board
                            rack_view.player = game.current_player
                            rack_view.clear_selection()

                            if game.winner is not None:
                                status_message = f"VITÓRIA! {game.winner.name} venceu a partida!"
                                status_color = (255, 215, 0)
                                status_timer = 600
                            else:
                                status_message = f"Jogada realizada com sucesso (+{candidate_meld.points} pts)! Vez de {game.current_player.name}."
                                status_color = (80, 200, 120)
                                status_timer = 180
                        except ValueError as err:
                            board_view.board = game.board
                            rack_view.player = game.current_player
                            rack_view.clear_selection()
                            status_message = f"Jogada recusada: {err}"
                            status_color = (230, 80, 80)
                            status_timer = 180
            else:
                rack_view.handle_click(event.pos)

    screen.fill(TABLE_BG)

    header_rect = pygame.Rect(40, 15, SCREEN_WIDTH - 80, 48)
    pygame.draw.rect(screen, HEADER_BG, header_rect, border_radius=10)
    pygame.draw.rect(screen, HEADER_BORDER, header_rect, width=1, border_radius=10)

    lbl_turn = font_header.render(f"VEZ: {game.current_player.name.upper()}", True, (251, 191, 36))
    screen.blit(lbl_turn, (header_rect.x + 20, header_rect.y + 14))

    lbl_bag = font_header.render(f"MONTE: {len(game.bag)} peças", True, TEXT_LIGHT)
    screen.blit(lbl_bag, (header_rect.centerx - 70, header_rect.y + 14))

    if game.current_player.has_initial_meld:
        status_badge_text = "Saída: OK"
        status_badge_color = (80, 200, 120)
    else:
        status_badge_text = "Saída: Mín. 30 pts"
        status_badge_color = (230, 150, 40)

    lbl_initial = font_header.render(status_badge_text, True, status_badge_color)
    screen.blit(lbl_initial, (header_rect.right - 180, header_rect.y + 14))

    pygame.draw.rect(screen, BOARD_PANEL_BG, board_rect, border_radius=14)
    pygame.draw.rect(screen, BOARD_PANEL_BORDER, board_rect, width=1, border_radius=14)

    lbl_board = font_label.render("MESA DE JOGO (TABULEIRO):", True, TEXT_MUTED)
    screen.blit(lbl_board, (board_rect.x + 20, board_rect.y + 12))

    board_view.draw(theme=current_theme)

    pygame.draw.rect(screen, (22, 25, 33) if current_theme == 'obsidian' else (30, 33, 42), rack_rect, border_radius=14)
    pygame.draw.rect(screen, (40, 45, 58), rack_rect, width=1, border_radius=14)

    lbl_rack = font_label.render(
        f"MÃO DE {game.current_player.name.upper()} ({len(game.current_player.rack)} peças) - SELECIONADAS: {len(rack_view.selected_indices)}",
        True,
        TEXT_MUTED
    )
    screen.blit(lbl_rack, (rack_rect.x + 25, rack_rect.y + 14))

    if status_timer > 0:
        status_timer -= 1
        txt_status = font_feedback.render(status_message, True, status_color)
        screen.blit(txt_status, (rack_rect.x + 480, rack_rect.y + 12))

    rack_view.draw(theme=current_theme)

    for btn in buttons:
        btn.draw(screen)

    if game.winner is not None:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        win_card = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 100, 500, 200)
        pygame.draw.rect(screen, (28, 33, 44), win_card, border_radius=16)
        pygame.draw.rect(screen, (251, 191, 36), win_card, width=2, border_radius=16)

        win_title = font_winner.render("R U M M I K U B !", True, (251, 191, 36))
        win_title_rect = win_title.get_rect(center=(win_card.centerx, win_card.y + 60))
        screen.blit(win_title, win_title_rect)

        win_sub = font_header.render(f"Parabéns, {game.winner.name} venceu a partida!", True, TEXT_LIGHT)
        win_sub_rect = win_sub.get_rect(center=(win_card.centerx, win_card.y + 120))
        screen.blit(win_sub, win_sub_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()