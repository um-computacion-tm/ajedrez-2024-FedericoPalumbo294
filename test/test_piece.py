import unittest
from game.piece import Piece

class TestPiece(unittest.TestCase):
    def test_SetUp(self):
        piece = Piece("WHITE")
        self.assertEqual(piece.__color__,"WHITE")

if __name__ == '__main__':
    unittest.main()