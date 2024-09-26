import sys
import os

# Añadir el directorio raíz del proyecto al sys.path
current_file_path = os.path.abspath(__file__)  # Obtener la ruta absoluta del archivo actual
project_root = os.path.dirname(os.path.dirname(current_file_path))  # Obtener el directorio raíz del proyecto
sys.path.append(project_root)  # Agregar el directorio raíz al sys.path

from game.piece import Piece

class Rook(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♜' if self.color == "WHITE" else '♖'  # Símbolos para la torre

    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Verificar si el movimiento es horizontal o vertical
        if start_row != end_row and start_col != end_col:
            return False

        # Verificar que el camino esté despejado
        def calculate_step(start, end):
            return (end - start) // max(1, abs(end - start)) if start != end else 0

        step_row = calculate_step(start_row, end_row)
        step_col = calculate_step(start_col, end_col)


        current_row, current_col = start_row + step_row, start_col + step_col
        
        # Iterar a través de las casillas entre la posición de inicio y la de destino
        while (current_row, current_col) != (end_row, end_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += step_row
            current_col += step_col

        # Verificar si la casilla de destino está vacía o contiene una pieza del oponente
        destination_piece = board[end_row][end_col]
        return destination_piece is None or destination_piece.color != self.color
