import unittest

from interview_sudoku_python import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    def test_empty_board_is_not_solved(self):
        self.assertFalse(SudokuBoard([[0 for _ in range(9)] for _ in range(9)]).is_solved(),
                         "An empty board should not be solved")

    def test_board_should_be_within_sudoku_range(self):
        board_with_empty_cells = [
            [5, 0, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 0, 0, 4, 999],
            [1, 9, 0, 0, 0, 0, 5, 6, 7],
            [0, 5, 9, 7, 0, 0, 4, 0, 3],
            [4, 2, 6, 8, 5, 3, 0, 0, 0],
            [7, 1, 0, 0, 0, 4, 0, 0, 0],
            [0, 6, 1, 0, -10, 7, 2, 8, 4],
            [2, 8, 7, 0, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 0, 6, 1, 7, 9],
        ]
        self.assertFalse(SudokuBoard(board_with_empty_cells).is_solved(),
                         "A board with wrong cells should not be solved")

    def test_invalid_board_with_incorrect_column_is_not_solved(self):
        invalid_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 9],  # wrong
            [3, 4, 5, 2, 8, 6, 1, 7, 5],  # wrong
        ]
        self.assertFalse(SudokuBoard(invalid_board).is_solved(),
                         "A board with an incorrect COLUMN should not be solved")

    def test_invalid_board_is_not_solved(self):
        invalid_board = [
            [8, 8, 8, 8, 8, 8, 8, 8, 8],
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [4, 4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [9, 9, 9, 9, 9, 9, 9, 9, 9],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
        self.assertFalse(SudokuBoard(invalid_board).is_solved(), "An incorrect board should not be solved")

    def test_invalid_board_with_incorrect_row_is_not_solved(self):
        invalid_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 9],  # wrong
            [3, 4, 5, 2, 8, 6, 1, 7, 5],  # wrong
        ]
        self.assertFalse(SudokuBoard(invalid_board).is_solved(), "A board with an incorrect ROW should not be solved")

    def test_invalid_board_with_incorrect_square_is_not_solved(self):
        invalid_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],  # wrong, should be last row
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
        ]
        self.assertFalse(SudokuBoard(invalid_board).is_solved(),
                         "A board with an incorrect SQUARE should not be solved")

    def test_full_board_is_solved(self):
        solved_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        self.assertTrue(SudokuBoard(solved_board).is_solved(), "A full correct board should be solved")
