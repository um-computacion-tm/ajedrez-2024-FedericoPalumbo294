import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.knight import Knight
from game.piece import Piece

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_knight = Knight("WHITE")
        self.black_knight = Knight("BLACK")
        self.board[4][4] = self.white_knight  # Colocar el caballo blanco en el centro del tablero

    def test_valid_moves(self):
        # Movimientos válidos para el caballo blanco desde (4, 4)
        valid_moves = [
            (4, 4, 6, 5), (4, 4, 6, 3), (4, 4, 2, 5), (4, 4, 2, 3),
            (4, 4, 5, 6), (4, 4, 5, 2), (4, 4, 3, 6), (4, 4, 3, 2)
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.white_knight.move((start_row, start_col), (end_row, end_col), self.board))

    def test_invalid_moves(self):
        # Movimientos inválidos para el caballo blanco desde (4, 4)
        invalid_moves = [
            (4, 4, 4, 5), (4, 4, 5, 4), (4, 4, 3, 4), (4, 4, 4, 3),
            (4, 4, 6, 6), (4, 4, 2, 2)
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_knight.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición válida
        self.board[6][5] = Piece("BLACK", self.board)
        self.assertTrue(self.white_knight.move((4, 4), (6, 5), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición válida
        self.board[6][5] = Piece("WHITE", self.board)
        self.assertFalse(self.white_knight.move((4, 4), (6, 5), self.board))

if __name__ == '__main__':
    unittest.main()