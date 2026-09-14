from itertools import cycle
from .board import Board, Meld
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
        self._current_player_rack_snapshot = None
        self._current_player_has_initial_meld_state = False

    def next_player(self):
        self.current_player = next(self._iter_players)
        self.start_turn()

    def start_game(self):
        for player in self.players:
            player.add_tiles(self.bag.draw_many(14))

        self.start_turn()

    def player_draw_tile(self):
        self.current_player.add_tiles([self.bag.draw()])
        self.next_player()

    def has_winner(self):
        for player in self.players:
            if player.is_winner:
                self.winner = player
                return True
        return False

    def start_turn(self):
        self.board.take_snapshot()
        self._current_player_rack_snapshot = list(self.current_player.rack)
        self._current_player_has_initial_meld_state = self.current_player.has_initial_meld

    def rollback_turn(self):
        self.board.rollback()
        if self._current_player_rack_snapshot is not None:
            self.current_player.rack = list(self._current_player_rack_snapshot)
            self._current_player_rack_snapshot = None
            self.current_player.has_initial_meld = self._current_player_has_initial_meld_state

    def commit_turn(self):
        self.board.commit()
        self._current_player_rack_snapshot = None

    def play_melds(self, new_melds: list[Meld]):
        for meld in new_melds:
            # if not all([tile in self.current_player.rack for tile in meld.tiles]):
            #     raise ValueError("Player does not have the intended Tile in Rack")

            for tile in meld.tiles:
                if tile not in self.current_player.rack:
                    self.rollback_turn()
                    raise ValueError("Player does not have the intended Tile in Rack")

                self.current_player.remove_tile(tile)

            self.board.add_meld(meld)

        if not self.current_player.has_initial_meld:
            total_points = sum(meld.points for meld in new_melds)
            if total_points < 30:
                self.rollback_turn()
                raise ValueError("Initial meld must be at least 30 points")
            else:
                self.current_player.has_initial_meld = True

        if not self.board.is_valid():
            self.rollback_turn()
            raise ValueError("Invalid final table")

        self.commit_turn()
        self.has_winner()
        self.next_player()

