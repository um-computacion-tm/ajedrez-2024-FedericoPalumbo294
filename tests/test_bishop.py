import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.bishop import Bishop
from game.piece import Piece

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_bishop = Bishop("WHITE")
        self.black_bishop = Bishop("BLACK")
        self.board[4][4] = self.white_bishop  # Colocar el alfil blanco en el centro del tablero

    def test_valid_moves(self):
        # Movimientos válidos para el alfil blanco desde (4, 4)
        valid_moves = [
            (4, 4, 0, 0), (4, 4, 7, 7), (4, 4, 1, 7), (4, 4, 7, 1),
            (4, 4, 2, 2), (4, 4, 6, 6)
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.white_bishop.move((start_row, start_col), (end_row, end_col), self.board))

    def test_invalid_moves(self):
        # Movimientos inválidos para el alfil blanco desde (4, 4)
        invalid_moves = [
            (4, 4, 4, 5), (4, 4, 5, 4), (4, 4, 3, 4), (4, 4, 4, 3)
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_bishop.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición válida
        self.board[0][0] = Piece("BLACK", self.board)
        self.assertTrue(self.white_bishop.move((4, 4), (0, 0), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición válida
        self.board[0][0] = Piece("WHITE", self.board)
        self.assertFalse(self.white_bishop.move((4, 4), (0, 0), self.board))

    def test_path_blocked(self):
        # Colocar una pieza en el camino del alfil
        self.board[2][2] = Piece("WHITE", self.board)
        self.assertFalse(self.white_bishop.move((4, 4), (0, 0), self.board))

if __name__ == '__main__':
    unittest.main()