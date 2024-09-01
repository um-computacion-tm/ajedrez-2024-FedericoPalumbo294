import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class Pawn(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♟' if self.color == "WHITE" else '♙'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        direction = 1 if self.color == "WHITE" else -1

        # Movimiento hacia adelante
        if start_col == end_col:
            # Movimiento de una casilla
            if end_row == start_row + direction and board[end_row][end_col] is None:
                return True
            # Movimiento de dos casillas desde la posición inicial
            if (self.color == "WHITE" and start_row == 6 or self.color == "BLACK" and start_row == 1) and end_row == start_row + 2 * direction and board[end_row][end_col] is None and board[start_row + direction][start_col] is None:
                return True

        # Captura de piezas
        if abs(start_col - end_col) == 1 and end_row == start_row + direction and board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            return True

        return False