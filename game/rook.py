import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class Rook(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'R' if self.color == "WHITE" else 'r'

    def move(self, start_pos, end_pos, board):

        """Verifica si el movimiento de la torre es válido."""
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento horizontal o vertical
        if start_row == end_row or start_col == end_col:
            # Verificar si hay obstáculos en el camino
            if start_row == end_row:  # Movimiento horizontal
                step = 1 if start_col < end_col else -1
                for col in range(start_col + step, end_col, step):
                    if board[start_row][col] is not None:
                        return False
            else:  # Movimiento vertical
                step = 1 if start_row < end_row else -1
                for row in range(start_row + step, end_row, step):
                    if board[row][start_col] is not None:
                        return False
            return True
        return False