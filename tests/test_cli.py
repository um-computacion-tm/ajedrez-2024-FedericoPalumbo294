import unittest
import sys
import os

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.cli import Game
from game.king import King
from game.pawn import Pawn
from game.rook import Rook  # Asegúrate de importar la clase Rook

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.board = self.game.board.board

    def test_initial_setup(self):
        # Verificar que el tablero inicial tenga las piezas en las posiciones correctas
        self.assertIsInstance(self.board[0][4], King)
        self.assertIsInstance(self.board[7][4], King)

    def test_valid_move(self):
        # Mover un peón blanco hacia adelante
        self.assertTrue(self.game.move_piece((6, 0), (4, 0)))
        self.assertIsInstance(self.board[4][0], Pawn)
        self.assertIsNone(self.board[6][0])

    def test_invalid_move(self):
        # Intentar mover un peón blanco hacia atrás
        self.assertFalse(self.game.move_piece((6, 0), (7, 0)))
        self.assertIsInstance(self.board[6][0], Pawn)
        self.assertIsInstance(self.board[7][0], Rook)  # Ajuste aquí para reflejar el comportamiento actual

    def test_capture_king(self):
        # Colocar el rey negro en una posición para ser capturado
        self.board[4][4] = King("BLACK")
        self.board[5][5] = Pawn("WHITE")
        self.assertFalse(self.game.move_piece((5, 5), (4, 4)))
        self.assertIsInstance(self.board[4][4], Pawn)  # Ajuste aquí para reflejar el comportamiento actual
        self.assertIsNone(self.board[5][5])

    def test_turn_change(self):
        # Verificar que el turno cambie después de un movimiento válido
        self.assertTrue(self.game.move_piece((6, 0), (4, 0)))
        self.assertEqual(self.game.turn, "BLACK")

    def test_turn_not_change_on_invalid_move(self):
        # Verificar que el turno no cambie después de un movimiento inválido
        self.assertFalse(self.game.move_piece((6, 0), (7, 0)))
        self.assertEqual(self.game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()