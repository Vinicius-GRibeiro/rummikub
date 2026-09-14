import pytest
from rummikub.core.game import Game
from rummikub.core.meld import Group
from rummikub.core.tile import Tile, Color

def test_game_initial_state():
    game = Game(["Joao", "Luiza"])

    assert len(game.players) == 2
    assert game.current_player.name == "Joao"
    assert game.winner is None

def test_game_invalid_player_count():
    with pytest.raises(ValueError, match="Min"):
        game = Game(["Joao"])

def test_start_game_deals_14_tiles():
    game = Game(["Joao", "Luiza"])
    game.start_game()

    assert all([len(player.rack) == 14 for player in game.players])
    assert len(game.bag) == 78

def test_next_player_rotation():
    game = Game(["Joao", "Luiza", "Carlos"])
    assert game.current_player.name == "Joao"

    game.next_player()
    assert game.current_player.name == "Luiza"

    game.next_player()
    assert game.current_player.name == "Carlos"

    game.next_player()
    assert game.current_player.name == "Joao"

def test_player_draw_tile():
    game = Game(["Joao", "Luiza"])
    game.start_game()

    game.player_draw_tile()
    assert len(game.players[0].rack) == 15
    assert game.current_player.name == "Luiza"

def test_has_winner():
    game = Game(["Joao", "Luiza"])
    game.start_game()

    assert not game.has_winner()
    game.players[0].rack.clear()

    assert game.has_winner()
    assert game.winner == game.players[0]

def test_rollback_turn_restores_board_and_rack():
    game = Game(["Joao", "Luiza"])
    game.start_game()

    first_player = game.current_player

    first_player.rack.pop()
    first_player.rack.pop()
    first_player.rack.pop()

    assert len(first_player.rack) == 11

    game.board.add_meld(Group([Tile(Color.BLACK, 6)]))

    assert len(game.board) == 1
    assert not game.board.is_valid()

    game.rollback_turn()

    assert len(first_player.rack) == 14
    assert len(game.board) == 0
    assert game.board.is_valid()

def test_play_melds_valid_initial_meld():
    game = Game(["Joao", "Luiza"])
    meld = Group([Tile(Color.RED, 10), Tile(Color.BLUE, 10), Tile(Color.BLACK, 10)])
    game.current_player.rack = list(meld.tiles)

    game.start_turn()
    game.play_melds([meld])

    assert len(game.players[0].rack) == 0
    assert meld in game.board.melds
    assert game.players[0].has_initial_meld
    assert game.current_player.name == "Luiza"

def test_play_melds_initial_meld_less_than_30_points_fails():
    game = Game(["Joao", "Luiza"])
    meld = Group([Tile(Color.RED, 7), Tile(Color.BLUE, 7), Tile(Color.BLACK, 7)])
    game.current_player.rack = list(meld.tiles)

    game.start_turn()

    with pytest.raises(ValueError, match="30 points"):
        game.play_melds([meld])

    assert not game.players[0].has_initial_meld
    assert game.players[0].rack == list(meld.tiles)
    assert len(game.board) == 0

def test_play_melds_with_tiles_not_in_rack_fails():
    game = Game(["Joao", "Luiza"])
    meld = Group([Tile(Color.RED, 1), Tile(Color.BLUE, 1), Tile(Color.BLACK, 1)])
    game.current_player.rack = list(meld.tiles)

    game.start_turn()
    with pytest.raises(ValueError, match="Rack"):
        game.play_melds([Group([Tile(Color.RED, 10), Tile(Color.BLUE, 10), Tile(Color.BLACK, 10)])])

    assert game.players[0].rack == list(meld.tiles)
    assert len(game.board) == 0

def test_play_melds_winning_game():
    game = Game(["Joao", "Luiza"])
    meld = Group([Tile(Color.RED, 10), Tile(Color.BLUE, 10), Tile(Color.BLACK, 10)])
    game.current_player.rack = list(meld.tiles)

    game.start_turn()
    game.play_melds([meld])

    assert game.has_winner()
    assert game.winner.name == "Joao"

