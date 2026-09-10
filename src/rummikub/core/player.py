from .tile import Tile

class Player:
    def __init__(self, name, rack: list[Tile] | None = None):
        self.name = name
        self.rack = rack if rack is not None else []
        self.has_initial_meld = False


    def add_tiles(self, tiles: list[Tile]):
        self.rack.extend(tiles)

    def remove_tile(self, tile: Tile):
        if tile not in self.rack:
            raise ValueError("Player doesn't have the TILE in RACK")

        self.rack.remove(tile)

    def sort_rack_by_value(self):
        self.rack.sort(key=lambda tile: (99, 'ZZZ') if tile.is_joker else (tile.value, tile.color.value))

    def sort_rack_by_color(self):
        self.rack.sort(key=lambda tile: ('ZZZ', 99) if tile.is_joker else (tile.color.value, tile.value))

    @property
    def rack_points(self):
        return sum(30 if tile.is_joker else tile.value for tile in self.rack)

    @property
    def is_winner(self):
        return len(self.rack) == 0

