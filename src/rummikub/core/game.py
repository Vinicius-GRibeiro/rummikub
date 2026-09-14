from itertools import cycle
from .board import Board
from .bag import TileBag
from .player import Player

class Game:
    def __init__(self, players_names: list[str], bag: TileBag | None = None, board: Board | None = None):
        if not(2 <= len(players_names) <= 4):
            raise ValueError("Min 2 players and max 4 players")

        self.players = [Player(name) for name in players_names]
        self.bag = bag if bag is not None else TileBag()
        self.board = board if board is not None else Board()

        self._iter_players = cycle(self.players)
        self.current_player = next(self._iter_players)

        self.winner: Player | None = None

    def next_player(self):
        self.current_player = next(self._iter_players)

    def start_game(self):
        for player in self.players:
            player.add_tiles(self.bag.draw_many(14))

    def player_draw_tile(self):
        self.current_player.add_tiles([self.bag.draw()])
        self.next_player()

    def has_winner(self):
        for player in self.players:
            if player.is_winner:
                self.winner = player
                return True
        return False
