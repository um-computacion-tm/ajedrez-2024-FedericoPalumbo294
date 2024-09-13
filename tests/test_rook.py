import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.rook import Rook
from game.piece import Piece

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")
        self.board[0][0] = self.white_rook  # Colocar la torre blanca en su posición inicial
        self.board[7][7] = self.black_rook  # Colocar la torre negra en su posición inicial

    def test_valid_moves(self):
        # Movimientos válidos para la torre blanca desde (0, 0)
        valid_moves = [
            (0, 0, 0, 5),  # Movimiento horizontal hacia la derecha
            (0, 0, 5, 0)   # Movimiento vertical hacia abajo
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.white_rook.move((start_row, start_col), (end_row, end_col), self.board))

        # Movimientos válidos para la torre negra desde (7, 7)
        valid_moves = [
            (7, 7, 7, 2),  # Movimiento horizontal hacia la izquierda
            (7, 7, 2, 7)   # Movimiento vertical hacia arriba
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.black_rook.move((start_row, start_col), (end_row, end_col), self.board))

    def test_invalid_moves(self):
        # Movimientos inválidos para la torre blanca desde (0, 0)
        invalid_moves = [
            (0, 0, 1, 1),  # Movimiento diagonal
            (0, 0, 2, 2),  # Movimiento diagonal
            (0, 0, 1, 2),  # Movimiento en L
            (0, 0, 2, 1)   # Movimiento en L
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_rook.move((start_row, start_col), (end_row, end_col), self.board))

        # Movimientos inválidos para la torre negra desde (7, 7)
        invalid_moves = [
            (7, 7, 6, 6),  # Movimiento diagonal
            (7, 7, 5, 5),  # Movimiento diagonal
            (7, 7, 6, 5),  # Movimiento en L
            (7, 7, 5, 6)   # Movimiento en L
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.black_rook.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición válida para captura
        self.board[0][5] = Piece("BLACK", self.board)
        self.assertTrue(self.white_rook.move((0, 0), (0, 5), self.board))

        self.board[2][7] = Piece("WHITE", self.board)
        self.assertTrue(self.black_rook.move((7, 7), (2, 7), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición válida para captura
        self.board[0][5] = Piece("WHITE", self.board)
        self.assertFalse(self.white_rook.move((0, 0), (0, 5), self.board))

        self.board[2][7] = Piece("BLACK", self.board)
        self.assertFalse(self.black_rook.move((7, 7), (2, 7), self.board))

    def test_path_blocked(self):
        # Colocar una pieza en el camino de la torre blanca
        self.board[0][3] = Piece("WHITE", self.board)
        self.assertFalse(self.white_rook.move((0, 0), (0, 5), self.board))

        # Colocar una pieza en el camino de la torre negra
        self.board[5][7] = Piece("BLACK", self.board)
        self.assertFalse(self.black_rook.move((7, 7), (2, 7), self.board))

if __name__ == '__main__':
    unittest.main()