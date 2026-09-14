import pytest

from src.rummikub.core.game import Game

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

