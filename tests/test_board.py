import pytest
from rummikub.core.tile import Tile, Color
from rummikub.core.meld import Group, Run
from rummikub.core.board import Board

def test_board_initial_state():
    board = Board()

    assert len(board) == 0
    assert board.is_valid()

def test_add_and_get_meld():
    board = Board()
    group = Group([Tile(Color.YELLOW, 2), Tile(Color.BLACK, 2), Tile(Color.RED, 2)])
    run = Run([Tile(Color.YELLOW, 1), Tile(Color.YELLOW, 2), Tile(Color.YELLOW, 3)])

    board.add_meld(group)
    board.add_meld(run)

    assert len(board) == 2
    assert board.get_meld(0) == group
    assert board.get_meld(1) == run

def test_remove_meld():
    board = Board()
    group = Group([Tile(Color.YELLOW, 2), Tile(Color.BLACK, 2), Tile(Color.RED, 2)])
    run = Run([Tile(Color.YELLOW, 1), Tile(Color.YELLOW, 2), Tile(Color.YELLOW, 3)])
    board.add_meld(group)
    board.add_meld(run)

    board.remove_meld(0)

    assert len(board) == 1
    assert board.melds[0] == run

def test_board_validity_with_mixed_melds():
    board = Board()
    group = Group([Tile(Color.YELLOW, 2), Tile(Color.BLACK, 2), Tile(Color.RED, 2)])
    run = Run([Tile(Color.YELLOW, 1), Tile(Color.YELLOW, 2), Tile(Color.BLUE, 3)])

    board.add_meld(group)
    assert board.is_valid()

    board.add_meld(run)
    assert not board.is_valid()

def test_snapshot_and_rollback():
    board = Board()
    group = Group([Tile(Color.YELLOW, 2), Tile(Color.BLACK, 2), Tile(Color.RED, 2)])
    board.add_meld(group)

    board.take_snapshot()

    run = Run([Tile(Color.YELLOW, 1), Tile(Color.YELLOW, 2), Tile(Color.BLUE, 3)])
    board.add_meld(run)

    assert not board.is_valid()

    board.rollback()

    assert board.is_valid()

def test_commit_valid_state():
    board = Board()
    group = Group([Tile(Color.YELLOW, 2), Tile(Color.BLACK, 2), Tile(Color.RED, 2)])
    board.add_meld(group)

    board.take_snapshot()
    run = Run([Tile(Color.YELLOW, 1), Tile(Color.YELLOW, 2), Tile(Color.YELLOW, 3)])
    board.add_meld(run)

    board.commit()

    assert board._snapshot is None

def test_commit_invalid_board_raises_error():
    board = Board()
    board.add_meld(Group([Tile(Color.RED, 1)]))
    with pytest.raises(ValueError, match="invalid"):
        board.commit()