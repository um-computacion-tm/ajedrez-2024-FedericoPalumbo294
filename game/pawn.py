import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game.piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♟' if self.color == "WHITE" else '♙'  # Símbolos para el peón

    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        direction = -1 if self.color == "WHITE" else 1

        if self.is_move_forward(start_pos, end_pos, board, direction):
            return True
        if self.is_initial_double_move(start_pos, end_pos, board, direction):
            return True
        if self.is_capture(start_pos, end_pos, board, direction):
            return True

        return False

    def is_move_forward(self, start_pos, end_pos, board, direction):
        """Verificar si el peón se mueve hacia adelante una casilla."""
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        return start_col == end_col and end_row == start_row + direction and board[end_row][end_col] is None

    def is_initial_double_move(self, start_pos, end_pos, board, direction):
        """Verificar si el peón realiza el movimiento inicial de dos casillas."""
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        is_initial_row = (self.color == "WHITE" and start_row == 6) or (self.color == "BLACK" and start_row == 1)
        return is_initial_row and start_col == end_col and end_row == start_row + 2 * direction and \
               board[start_row + direction][start_col] is None and board[end_row][end_col] is None

    def is_capture(self, start_pos, end_pos, board, direction):
        """Verificar si el peón captura una pieza enemiga."""
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        return abs(start_col - end_col) == 1 and end_row == start_row + direction and \
               board[end_row][end_col] is not None and board[end_row][end_col].color != self.color
