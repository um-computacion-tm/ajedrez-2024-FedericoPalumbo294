import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.pawn import Pawn
from game.piece import Piece

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_pawn = Pawn("WHITE")
        self.black_pawn = Pawn("BLACK")
        self.board[6][4] = self.white_pawn  # Colocar el peón blanco en su posición inicial
        self.board[1][4] = self.black_pawn  # Colocar el peón negro en su posición inicial

    def test_valid_moves(self):
        # Movimientos válidos para el peón blanco desde (6, 4)
        valid_moves = [
            (6, 4, 5, 4),  # Movimiento de una casilla hacia adelante
            (6, 4, 4, 4)   # Movimiento de dos casillas desde la posición inicial
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.white_pawn.move((start_row, start_col), (end_row, end_col), self.board))

        # Movimientos válidos para el peón negro desde (1, 4)
        valid_moves = [
            (1, 4, 2, 4),  # Movimiento de una casilla hacia adelante
            (1, 4, 3, 4)   # Movimiento de dos casillas desde la posición inicial
        ]
        for start_row, start_col, end_row, end_col in valid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertTrue(self.black_pawn.move((start_row, start_col), (end_row, end_col), self.board))

    def test_invalid_moves(self):
        # Movimientos inválidos para el peón blanco desde (6, 4)
        invalid_moves = [
            (6, 4, 5, 5),  # Movimiento diagonal sin captura
            (6, 4, 4, 5),  # Movimiento de dos casillas diagonal
            (6, 4, 6, 5),  # Movimiento horizontal
            (6, 4, 7, 4)   # Movimiento hacia atrás
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.white_pawn.move((start_row, start_col), (end_row, end_col), self.board))

        # Movimientos inválidos para el peón negro desde (1, 4)
        invalid_moves = [
            (1, 4, 2, 5),  # Movimiento diagonal sin captura
            (1, 4, 3, 5),  # Movimiento de dos casillas diagonal
            (1, 4, 1, 5),  # Movimiento horizontal
            (1, 4, 0, 4)   # Movimiento hacia atrás
        ]
        for start_row, start_col, end_row, end_col in invalid_moves:
            with self.subTest(start=(start_row, start_col), end=(end_row, end_col)):
                self.assertFalse(self.black_pawn.move((start_row, start_col), (end_row, end_col), self.board))

    def test_capture_opponent_piece(self):
        # Colocar una pieza del oponente en una posición válida para captura
        self.board[5][5] = Piece("BLACK", self.board)
        self.assertTrue(self.white_pawn.move((6, 4), (5, 5), self.board))

        self.board[2][3] = Piece("WHITE", self.board)
        self.assertTrue(self.black_pawn.move((1, 4), (2, 3), self.board))

    def test_blocked_by_own_piece(self):
        # Colocar una pieza propia en una posición válida para captura
        self.board[5][5] = Piece("WHITE", self.board)
        self.assertFalse(self.white_pawn.move((6, 4), (5, 5), self.board))

        self.board[2][3] = Piece("BLACK", self.board)
        self.assertFalse(self.black_pawn.move((1, 4), (2, 3), self.board))

    def test_path_blocked(self):
        # Colocar una pieza en el camino del peón blanco
        self.board[5][4] = Piece("WHITE", self.board)
        self.assertFalse(self.white_pawn.move((6, 4), (4, 4), self.board))

        # Colocar una pieza en el camino del peón negro
        self.board[2][4] = Piece("BLACK", self.board)
        self.assertFalse(self.black_pawn.move((1, 4), (3, 4), self.board))

    def test_invalid_double_move_not_initial_position(self):
        # Probar el caso donde no se permite un movimiento de dos casillas (peón no en posición inicial)
        self.board[4][4] = self.white_pawn  # Mover el peón blanco fuera de su posición inicial
        self.assertFalse(self.white_pawn.move((4, 4), (2, 4), self.board))  # Movimiento de dos casillas no permitido

if __name__ == '__main__':
    unittest.main()
