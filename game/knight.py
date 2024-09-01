import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class Knight(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♞' if self.color == "WHITE" else '♘'
