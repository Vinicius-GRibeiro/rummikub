from rummikub.core.tile import Tile, Color
from rummikub.core.meld import Run

def test_invalid_min_size():
    tiles = [Tile(Color.RED, 2), Tile(Color.RED, 3)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_invalid_max_size():
    tiles = [Tile(Color.RED, n) for n in range(1, 14)]
    tiles.append(Tile.create_joker())
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_invalid_jokers_only_sequence():
    tiles = [Tile.create_joker(), Tile.create_joker(), Tile.create_joker()]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_invalid_different_colors_sequence():
    tiles = [Tile(Color.RED, 1), Tile(Color.BLUE, 2), Tile(Color.RED, 3)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_valid_ordered_sequence_3_tiles_no_joker():
    tiles = [Tile(Color.RED, 1), Tile(Color.RED, 2), Tile(Color.RED, 3)]
    run = Run(tiles)

    assert run.is_valid()
    assert run.points == 6

def test_invalid_unordered_sequence_3_tiles_no_joker():
    tiles = [Tile(Color.RED, 2), Tile(Color.RED, 3), Tile(Color.RED, 1)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_valid_ordered_sequence_2_tiles_1_joker():
    tiles = [Tile(Color.RED, 1), Tile.create_joker(), Tile(Color.RED, 3)]
    run = Run(tiles)

    assert run.is_valid()
    assert run.points == 6

def test_invalid_unordered_sequence_2_tiles_1_joker():
    tiles = [Tile.create_joker(), Tile(Color.RED, 3), Tile(Color.RED, 1)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_invalid_not_enough_jokers():
    tiles = [Tile.create_joker(), Tile(Color.YELLOW, 3), Tile(Color.YELLOW, 4), Tile(Color.YELLOW, 7)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_valid_multiple_jokers():
    tiles = [Tile.create_joker(), Tile(Color.YELLOW, 3), Tile(Color.YELLOW, 4), Tile.create_joker(), Tile.create_joker()]
    run = Run(tiles)

    assert run.is_valid()
    assert run.points == 20

def test_invalid_repeated_numbers():
    tiles = [Tile(Color.YELLOW, 2), Tile(Color.YELLOW, 2), Tile(Color.YELLOW, 3)]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0

def test_invalid_sequence_in_wrong_positions_with_joker():
    tiles = [Tile(Color.BLACK, 2), Tile(Color.BLACK, 4), Tile.create_joker()]
    run = Run(tiles)

    assert not run.is_valid()
    assert run.points == 0