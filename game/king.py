import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class King(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'K' if self.color == "WHITE" else 'k'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos):
        raise NotImplementedError("This method should be overridden by subclasses")