import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.piece import Piece

class Rook(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♜' if self.color == "WHITE" else '♖' # Devuelve '♜' si el color de la torre es white, sino devuelve '♖'

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):

        start_row, start_col = start_pos # definimos la posición inicial con la fila y columna inicial
        end_row, end_col = end_pos # definimos la posición final con la fila y columna final

        # Movimiento horizontal o vertical
        if start_row == end_row or start_col == end_col: # Verifica si la torre se mueve en forma horizontal o vertical
            
            if start_row == end_row:  # Movimiento horizontal
                step = 1 if start_col < end_col else -1 # Define step = 1 (para la derecha) si la columna inicial < columna final o -1 para la izquierda
                # Verificar si hay obstáculos en el camino
                for col in range(start_col + step, end_col, step): # Recorre entre las columnas start_col y end_col en pasos de 'step'
                    if board[start_row][col] is not None: # Verifica si hay una pieza en la posición donde esta del tablero
                        return False

            else:  # Movimiento vertical
                step = 1 if start_row < end_row else -1 # Define step = 1 (para abajo) si la fila inicial < fila final o -1 para arriba
                for row in range(start_row + step, end_row, step): # Recorre entre las filas start_row y end_row en pasos de 'step'
                    if board[row][start_col] is not None: # Verifica si hay una pieza en la posición donde esta del tablero
                        return False
            return True  # Movimiento válido
        return False  # Movimiento inválido