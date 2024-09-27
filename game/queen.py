import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.piece import Piece

class Queen(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♛' if self.color == "WHITE" else '♕'  # Símbolos para la reina

    def is_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        step_row = (end_row - start_row) // max(1, abs(end_row - start_row))  # 1, -1 o 0
        step_col = (end_col - start_col) // max(1, abs(end_col - start_col))  # 1, -1 o 0

        current_row, current_col = start_row + step_row, start_col + step_col

        # Verificar el camino hasta la posición final
        for _ in range(max(abs(end_row - current_row), abs(end_col - current_col))):
            if board[current_row][current_col] is not None:
                return False
            current_row = current_row + step_row
            current_col = current_col + step_col


        return True

    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Verificar si el movimiento es horizontal, vertical o diagonal
        if not (row_diff == 0 or col_diff == 0 or row_diff == col_diff):
            return False

        # Verificar que el camino esté despejado
        if not self.is_path_clear(start_pos, end_pos, board):
            return False

        # Verificar si la casilla de destino está vacía o contiene una pieza del oponente
        destination_piece = board[end_row][end_col]
        if destination_piece is None or destination_piece.color != self.color:
            return True

        return False
