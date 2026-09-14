import copy
from .meld import Meld

class Board:
    def __init__(self):
        self.melds: list[Meld] = []
        self._snapshot: list[Meld] | None = None

    def add_meld(self, meld: Meld):
        self.melds.append(meld)

    def remove_meld(self, index: int):
        return self.melds.pop(index)

    def get_meld(self, index):
        return self.melds[index]

    def is_valid(self):
        return all(meld.is_valid() for meld in self.melds)

    def take_snapshot(self):
        self._snapshot = copy.deepcopy(self.melds)

    def rollback(self):
        if self._snapshot is not None:
            self.melds = copy.deepcopy(self._snapshot)
            self._snapshot = None

    def commit(self):
        if not self.is_valid():
            raise ValueError("Can not commit a invalid board")

        self._snapshot = None

    def __len__(self):
        return len(self.melds)
