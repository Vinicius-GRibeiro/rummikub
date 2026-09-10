import pytest
from dataclasses import FrozenInstanceError
from rummikub.core.tile import Color, Tile


def test_create_valid_standard_tile():
    tile = Tile(Color.RED, 7)
    assert tile.color == Color.RED
    assert tile.value == 7
    assert tile.is_joker is False


def test_create_valid_joker():
    joker = Tile.create_joker()
    assert joker.is_joker is True
    assert joker.color is None
    assert joker.value is None


def test_tile_immutability():
    tile = Tile(Color.BLUE, 10)
    with pytest.raises(FrozenInstanceError):
        tile.value = 5


def test_tile_equality_and_hash():
    tile1 = Tile(Color.YELLOW, 8)
    tile2 = Tile(Color.YELLOW, 8)
    tile3 = Tile(Color.BLACK, 8)

    assert tile1 == tile2
    assert tile1 != tile3
    assert hash(tile1) == hash(tile2)
    assert len({tile1, tile2, tile3}) == 2


def test_string_representation():
    tile = Tile(Color.RED, 7)
    joker = Tile.create_joker()

    assert str(tile) == "[Red](7)"
    assert str(joker) == "[JOKER]"
    assert repr(tile) == "[Red](7)"
    assert repr(joker) == "[JOKER]"


def test_invalid_tile_missing_color():
    with pytest.raises(ValueError, match="COLOR"):
        Tile(None, 5)


def test_invalid_tile_missing_value():
    with pytest.raises(ValueError, match="VALUE"):
        Tile(Color.RED, None)


def test_invalid_joker_with_color_or_value():
    with pytest.raises(ValueError, match="JOKER"):
        Tile(Color.RED, 5, is_joker=True)

    with pytest.raises(ValueError, match="JOKER"):
        Tile(Color.RED, None, is_joker=True)

    with pytest.raises(ValueError, match="JOKER"):
        Tile(None, 5, is_joker=True)


@pytest.mark.parametrize("invalid_value", [0, -1, 14, 99])
def test_invalid_tile_value_out_of_bounds(invalid_value):
    with pytest.raises(ValueError):
        Tile(Color.RED, invalid_value)
