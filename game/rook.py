import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class Rook(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♜' if self.color == "WHITE" else '♖'  # Devuelve '♜' si el color de la torre es blanca, sino devuelve '♖'

    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Verificar si el movimiento es horizontal o vertical
        if start_row != end_row and start_col != end_col:
            return False

        # Verificar que el camino esté despejado
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        step_row = (end_row - start_row) // max(1, row_diff)  # 1, -1 o 0
        step_col = (end_col - start_col) // max(1, col_diff)  # 1, -1 o 0

        current_row, current_col = start_row + step_row, start_col + step_col
        while True:
            current_row += step_row
            current_col += step_col
            if (current_row, current_col) == (end_row, end_col):
                break
            if board[current_row][current_col] is not None:
                return False

        # Verificar si la casilla de destino está vacía o contiene una pieza del oponente
        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False