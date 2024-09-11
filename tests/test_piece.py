import sys
import os
import unittest
from unittest.mock import patch

# Agrega el directorio raíz del proyecto a la ruta de búsqueda de módulos de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class MockBoard:
    pass

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.board = MockBoard()

    def test_initialization(self):
        piece_white = Piece("WHITE", self.board)
        piece_black = Piece("BLACK", self.board)
        
        self.assertEqual(piece_white.color, "WHITE")
        self.assertEqual(piece_white.board, self.board)
        self.assertEqual(piece_black.color, "BLACK")
        self.assertEqual(piece_black.board, self.board)

    def test_str_representation(self):
        piece_white = Piece("WHITE", self.board)
        piece_white.white_str = "W"
        piece_white.black_str = "B"
        
        piece_black = Piece("BLACK", self.board)
        piece_black.white_str = "W"
        piece_black.black_str = "B"
        
        self.assertEqual(str(piece_white), "W")
        self.assertEqual(str(piece_black), "B")

if __name__ == '__main__':
    unittest.main()