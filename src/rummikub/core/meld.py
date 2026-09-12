from .tile import Tile, Color
from abc import ABC, abstractmethod

class Meld(ABC):
    def __init__(self, tiles: list[Tile] | None = None):
        self.tiles: list[Tile] = tiles if tiles is not None else []

    def __len__(self):
        return len(self.tiles)

    @property
    @abstractmethod
    def points(self):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

class Group(Meld):
    def __init__(self, tiles: list[Tile] | None = None):
        super().__init__(tiles)

    @property
    def points(self):
        if not self.is_valid():
            return 0

        regular_tiles = [t for t in self.tiles if not t.is_joker]
        target_value = regular_tiles[0].value
        return target_value * len(self.tiles)

    def is_valid(self) -> bool:
        if not (3 <= len(self.tiles) <= 4):
            return False

        regular_tiles = [t for t in self.tiles if not t.is_joker]

        if len(regular_tiles) == 0:
            return False

        first_value = regular_tiles[0].value
        if not all(t.value == first_value for t in regular_tiles):
            return False

        colors = [t.color for t in regular_tiles]
        if len(colors) != len(set(colors)):
            return False

        return True

class Run(Meld):
    def __init__(self, tiles: list[Tile] | None = None):
        super().__init__(tiles)

    def is_valid(self) -> bool:
        if not(3 <= len(self.tiles) <= 13): # Tamanho
            return False

        regular_tiles = [t for t in self.tiles if not t.is_joker]
        if len(regular_tiles) == 0: # Somente coringas
            return False
        
        if len(set([t.color for t in regular_tiles])) > 1: # Cor única
            return False

        if len(set(regular_tiles)) != len(regular_tiles): # Números repetidos
            return False

        anchor_tile = regular_tiles[0]
        anchor_index = self.tiles.index(anchor_tile)

        expected_sequence_first_value = anchor_tile.value - anchor_index
        expected_sequence_last_value = expected_sequence_first_value + (len(self.tiles) - 1)

        if expected_sequence_first_value < 1 or expected_sequence_last_value > 13:
            return False

        for index, tile in enumerate(self.tiles):
            expected_value = expected_sequence_first_value + index

            if tile.is_joker:
                continue

            if tile.value != expected_value:
                return False

        return True

        # joker_tiles = [j for j in self.tiles if j.is_joker]

        # regular_tiles.sort(key=lambda tile: (tile.value, tile.color.value))
        # missing_values = 0
        #
        # for index, tile in enumerate(regular_tiles):
        #     if index == len(regular_tiles) - 1: break
        #     missing_values += (regular_tiles[index+1].value - tile.value - 1)
        #
        # if missing_values > len(joker_tiles):
        #     return False

        # return True


    @property
    def points(self):
        pass
