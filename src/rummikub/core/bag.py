from .tile import Tile, Color
from random import shuffle


class TileBag:
    def __init__(self, autoshuffle = True):
        self.tiles: list[Tile] = []
        self._create_tiles()

        if autoshuffle:
            self.shuffle()

    def _create_tiles(self):
        for color in Color:
            for i in range(1, 14):
                self.tiles.append(Tile(color, i))
                self.tiles.append(Tile(color, i))

        self._create_jokers()

    def _create_jokers(self):
        self.tiles.append(Tile.create_joker())
        self.tiles.append(Tile.create_joker())

    def shuffle(self):
        shuffle(self.tiles)

    def draw(self) -> Tile:
        if not self.tiles:
            raise IndexError("Tile Bag is empty")

        return self.tiles.pop()

    def draw_many(self, count) -> list[Tile]:
        if not self.tiles:
            raise IndexError("Tile Bag is empty")

        return [self.draw() for _ in range(min(count, len(self.tiles)))]

    def __len__(self):
        return len(self.tiles)

# tb = TileBag()
# print(tb.tiles)
