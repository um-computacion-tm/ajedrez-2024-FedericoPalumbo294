import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game.piece import Piece

class Pawn(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♟' if self.color == "WHITE" else '♙' # Devuelve '♟' si el color del peón es blanco, sino devuelve '♙'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):
        # Descomponer las posiciones inicial y final en filas y columnas
        start_row = start_pos[0]
        start_col = start_pos[1]
        end_row = end_pos[0]
        end_col = end_pos[1]

        # Determinar la dirección del movimiento basado en el color del peón
        if self.color == "WHITE":
            direction = -1
        else:
            direction = 1

        # Movimiento de una casilla hacia adelante
        if start_col == end_col and board[end_row][end_col] is None:
            if end_row == start_row + direction:
                return True
            # Movimiento de dos casillas desde la posición inicial
            if (self.color == "WHITE" and start_row == 6) or (self.color == "BLACK" and start_row == 1):
                if end_row == start_row + 2 * direction and board[start_row + direction][start_col] is None:
                    return True

        # Captura de una pieza del oponente
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True

        return False