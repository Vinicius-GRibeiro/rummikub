from enum import Enum
from dataclasses import dataclass

class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    YELLOW = "Yellow"
    BLACK = "Black"

@dataclass(frozen=True)
class Tile:
    color: Color | None
    value: int | None
    is_joker: bool = False

    @classmethod
    def create_joker(cls):
        return cls(None, None, True)

    def __repr__(self):
        return f"[{self.color.value}]({self.value})" if not self.is_joker else "[JOKER]"

    def __str__(self):
        return f"[{self.color.value}]({self.value})" if not self.is_joker else "[JOKER]"

    def __post_init__(self):
        if self.is_joker:
            if self.value is not None or self.color is not None:
                raise ValueError("A JOKER tile should not have VALUE nor COLOR")

        else:
            if self.value is None or not (1 <= self.value <= 13):
                raise ValueError("A common tile should have a VALUE between 1 and 13")

            if self.color is None:
                raise ValueError("A common tile should have a COLOR")

