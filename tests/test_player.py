import pytest
from rummikub.core.player import Player
from rummikub.core.tile import Tile, Color

player_name = "Joao"

@pytest.fixture
def sample_tiles():
    return [
        Tile(Color.RED, 10),
        Tile(Color.YELLOW, 2),
        Tile(Color.BLUE, 7),
        Tile.create_joker(),
        Tile(Color.BLACK, 7),
        Tile(Color.BLUE, 11)
    ]

def test_player_initial_state():
    player = Player(player_name)

    assert player.name == player_name
    assert player.rack == []
    assert not player.has_initial_meld
    assert player.rack_points == 0
    assert player.is_winner # Zero tiles in hand, is winner

def test_add_remove_tiles(sample_tiles):
    player = Player(player_name, sample_tiles)

    assert len(player.rack) == 6
    assert not player.is_winner

    player.remove_tile(Tile(Color.YELLOW, 2))

    assert len(player.rack) == 5
    assert player.rack == [
        Tile(Color.RED, 10),
        Tile(Color.BLUE, 7),
        Tile.create_joker(),
        Tile(Color.BLACK, 7),
        Tile(Color.BLUE, 11)
    ]

def test_remove_tile_not_in_rack_error():
    player = Player(player_name, [Tile(Color.RED, 7)])

    with pytest.raises(ValueError, match="RACK"):
        player.remove_tile(Tile(Color.BLUE, 1)) # Removing Tile that is not in player's rack

def test_sort_by_value(sample_tiles):
    player = Player(player_name, sample_tiles)
    player.sort_rack_by_value()

    assert player.rack[0] == Tile(Color.YELLOW, 2)
    assert player.rack[1] == Tile(Color.BLACK, 7)
    assert player.rack[2] == Tile(Color.BLUE, 7)
    assert player.rack[3] == Tile(Color.RED, 10)
    assert player.rack[4] == Tile(Color.BLUE, 11)
    assert player.rack[5] == Tile.create_joker()

def test_sort_by_color(sample_tiles):
    player = Player(player_name, sample_tiles)
    player.sort_rack_by_color()

    assert player.rack[0] == Tile(Color.BLACK, 7)
    assert player.rack[1] == Tile(Color.BLUE, 7)
    assert player.rack[2] == Tile(Color.BLUE, 11)
    assert player.rack[3] == Tile(Color.RED, 10)
    assert player.rack[4] == Tile(Color.YELLOW, 2)
    assert player.rack[5] == Tile.create_joker()

def test_rack_points_calculation(sample_tiles):
    player = Player(player_name, sample_tiles)

    assert player.rack_points == 67
