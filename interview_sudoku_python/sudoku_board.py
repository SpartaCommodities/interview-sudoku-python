from typing import List

class SudokuBoard:
    board: List[List[int]]

    def __init__(self, board: List[List[int]]):
        self.board = board

    def is_solved(self) -> bool:
        return True
