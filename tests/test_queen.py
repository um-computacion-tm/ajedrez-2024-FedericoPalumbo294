import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.queen import Queen
from game.piece import Piece

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_queen = Queen("WHITE")
        self.black_queen = Queen("BLACK")
        self.board[4][4] = self.white_queen  # Colocar la reina blanca en el centro del tablero

    def test_valid_moves(self):
        # Movimientos válidos para la reina blanca desde (4, 4)
        valid_moves = [
            (4, 4, 0, 0), (4, 4, 7, 7), (4, 4, 0, 4), (4, 4, 4, 0),
            (4, 4, 7, 4), (4, 4, 4, 7), (4, 4, 7, 1), (4, 4, 1, 7)
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.white_queen.move((start_row, start_col), (end_row, end_col), self.board))

    def test_invalid_moves(self):
        # Movimientos inválidos para la reina blanca desde (4, 4)
        invalid_moves = [
            (4, 4, 5, 2), (4, 4, 2, 5), (4, 4, 3, 6), (4, 4, 6, 3)
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_queen.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición válida
        self.board[0][0] = Piece("BLACK", self.board)
        self.assertTrue(self.white_queen.move((4, 4), (0, 0), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición válida
        self.board[0][0] = Piece("WHITE", self.board)
        self.assertFalse(self.white_queen.move((4, 4), (0, 0), self.board))

    def test_path_blocked(self):
        # Colocar una pieza en el camino de la reina
        self.board[2][2] = Piece("WHITE", self.board)
        self.assertFalse(self.white_queen.move((4, 4), (0, 0), self.board))

if __name__ == '__main__':
    unittest.main()