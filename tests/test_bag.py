import pytest
from rummikub.core.tile import Tile, Color
from rummikub.core.bag import TileBag

def test_bag_initial_size():
    bag = TileBag()
    assert len(bag) == 106

def test_bag_composition(): # Saco com 2 peças de cada tipo (cor, valor e coringas)
    bag = TileBag(autoshuffle=False)

    jokers = [tile for tile in bag.tiles if tile.is_joker]
    assert len(jokers) == 2

    for color in Color:
        for value in range(1, 14):
            assert bag.tiles.count(Tile(color, value)) == 2

def test_bag_draw_one():
    bag = TileBag()
    initial_size = len(bag)
    drawed = bag.draw()

    assert len(bag) == initial_size - 1 # Tamanho decrementado em 1
    assert isinstance(drawed, Tile) # Peça comprada é do tipo Tile

def test_draw_from_empty_bag_error(): # Erro ao comprar peça com saco vazio
    bag = TileBag()

    for _ in range(106):
        bag.draw()

    assert len(bag) == 0 # Após esvaziar, saco tem tamanho 0

    with pytest.raises(IndexError, match="empty"):
        bag.draw() # Tentando comprar após saco vazio

def test_draw_many_tiles():
    bag = TileBag()
    drawed = bag.draw_many(14)

    assert len(drawed) == 14
    assert len(bag.tiles) == 92 # Sobraram a quantiddade correta

def test_draw_many_tiles_less_then_requested():
    bag = TileBag()
    bag.draw_many(100)

    drawed = bag.draw_many(10)

    assert len(drawed) == 6
    assert len(bag.tiles) == 0