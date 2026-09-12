from rummikub.core.meld import Group
from rummikub.core.tile import Tile, Color

def test_valid_three_tile_group():
    tiles = [Tile(Color.RED, 7), Tile(Color.BLUE, 7), Tile(Color.BLACK, 7)]
    group = Group(tiles)

    assert group.is_valid()
    assert group.points == 21

def test_valid_four_tile_group():
    tiles = [Tile(Color.RED, 4), Tile(Color.BLUE, 4), Tile(Color.BLACK, 4), Tile(Color.YELLOW, 4)]
    group = Group(tiles)

    assert group.is_valid()
    assert group.points == 16

def test_valid_group_with_joker():
    tiles = [Tile(Color.RED, 8), Tile.create_joker(), Tile.create_joker()]
    group = Group(tiles)

    assert group.is_valid()
    assert group.points == 24

def test_invalid_group_too_few_or_many_tiles():
    tiles_few = [Tile(Color.RED, 8), Tile(Color.BLUE, 8)]
    tiles_many = [Tile(Color.RED, 8), Tile(Color.BLUE, 8), Tile(Color.BLACK, 8), Tile(Color.YELLOW, 8), Tile.create_joker()]

    group_few = Group(tiles_few)
    group_many = Group(tiles_many)

    assert not group_few.is_valid()
    assert not group_many.is_valid()

def test_invalid_group_duplicated_color():
    tiles = [Tile(Color.RED, 8), Tile(Color.BLUE, 8), Tile(Color.RED, 8)]
    group = Group(tiles)

    assert not group.is_valid()

def test_group_different_values():
    tiles = [Tile(Color.RED, 8), Tile(Color.BLUE, 8), Tile(Color.YELLOW, 3)]
    group = Group(tiles)

    assert not group.is_valid()

def test_invalid_group_only_jokers():
    tiles = [Tile.create_joker(), Tile.create_joker(), Tile.create_joker()]
    group = Group(tiles)

    assert not group.is_valid()