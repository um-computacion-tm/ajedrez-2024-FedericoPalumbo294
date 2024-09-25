import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from game.piece import Piece

class Bishop(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return '♝' if self.color == "WHITE" else '♗'  # Símbolos para el alfil

    # Implementar la lógica de movimiento
    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Movimiento diagonal
        if abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1

            # Recorre la ruta diagonal
            for current_row, current_col in zip(range(start_row + row_step, end_row, row_step),
                                                range(start_col + col_step, end_col, col_step)):
                if board[current_row][current_col] is not None:
                    return False  # Camino no despejado

            # Verificar si la casilla de destino está vacía o contiene una pieza del oponente
            destination_piece = board[end_row][end_col]
            return destination_piece is None or destination_piece.color != self.color

        return False  # Movimiento no válido
