import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)))

from game.piece import Piece

class Knight(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♞' if self.color == "WHITE" else '♘' # Devuelve '♞' si el color del caballo es blanco, sino devuelve '♘'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):

        start_row, start_col = start_pos # Definimos la posición inicial con la fila y columna inicial
        end_row, end_col = end_pos # Definimos la posición final con la fila y columna final

        row_diff = abs(end_row - start_row) # Calcula la diferencia entre la fila final y la fila inicial
        col_diff = abs(end_col - start_col) # Calcula la diferencia entre la columna final y la columna inicial

        # El caballo se mueve en forma de "L": dos casillas en una dirección y una en la otra
        is_knight_move = (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

        if is_knight_move:
            destination_piece = board[end_row][end_col]
            is_empty_or_enemy = destination_piece is None or destination_piece.color != self.color
            if is_empty_or_enemy:
                return True
        return False