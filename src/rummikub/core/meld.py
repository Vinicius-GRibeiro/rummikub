from .tile import Tile
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


