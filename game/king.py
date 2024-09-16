import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.piece import Piece

class King(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♚' if self.color == "WHITE" else '♔' # Devuelve '♔' si el color de la torre es white, sino devuelve '♚'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):

        start_row, start_col = start_pos # definimos la posición inicial con la fila y columna inicial
        end_row, end_col = end_pos # definimos la posición final con la fila y columna final

        row_diff = abs(end_row - start_row) # Calcula la diferencia entre la fila final y la fila inicial
        col_diff = abs(end_col - start_col) # Calcula la diferencia entre la columna final y la columna inicial

        # El rey puede moverse una casilla en cualquier dirección
        if max(row_diff, col_diff) == 1:  # Verifica si la diferencia máxima en fila o columna es 1
            destination_piece = board[end_row][end_col]
            if destination_piece is None or destination_piece.color != self.color:  # Verificar si la casilla de destino está vacía o contiene una pieza del oponente
                return True

        return False