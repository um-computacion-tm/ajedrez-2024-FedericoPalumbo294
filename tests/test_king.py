import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.king import King
from game.piece import Piece

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_king = King("WHITE")
        self.black_king = King("BLACK")
        self.board[4][4] = self.white_king  # Colocar el rey blanco en el centro del tablero

    def test_valid_moves(self):
        # Movimientos válidos para el rey blanco desde (4, 4)
        valid_moves = [
            (4, 4, 3, 3), (4, 4, 3, 4), (4, 4, 3, 5),
            (4, 4, 4, 3),               (4, 4, 4, 5),
            (4, 4, 5, 3), (4, 4, 5, 4), (4, 4, 5, 5)
        ]
        for start_row, start_col, end_row, end_col in valid_moves: # Recorre los movimientos válidos
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)): # Subtest para cada movimiento
                self.assertTrue(self.white_king.move((start_row, start_col), (end_row, end_col), self.board)) # Verifica si el movimiento es válido

    def test_invalid_moves(self):
        # Movimientos inválidos para el rey blanco desde (4, 4)
        invalid_moves = [
            (4, 4, 2, 2), (4, 4, 2, 4), (4, 4, 2, 6),
            (4, 4, 4, 2),               (4, 4, 4, 6),
            (4, 4, 6, 2), (4, 4, 6, 4), (4, 4, 6, 6)
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_king.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición adyacente
        self.board[3][3] = Piece("BLACK", self.board)
        self.assertTrue(self.white_king.move((4, 4), (3, 3), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición adyacente
        self.board[3][3] = Piece("WHITE", self.board)
        self.assertFalse(self.white_king.move((4, 4), (3, 3), self.board))

if __name__ == '__main__':
    unittest.main()