import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import Board
from game.piece import Piece

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move_piece(self, start_pos, end_pos):
        if not self.is_within_bounds(start_pos) or not self.is_within_bounds(end_pos):
            print("Coordenadas fuera de rango.")
            return False

        piece = self.board.get_piece(start_pos[0], start_pos[1])
        if piece is None:
            print("No hay pieza en la posición de origen.")
            return False

        if piece.color != self.turn:
            print("No es tu turno.")
            return False

        if not piece.move(start_pos, end_pos):
            print("Movimiento inválido para la pieza.")
            return False

        target_piece = self.board.get_piece(end_pos[0], end_pos[1])
        if target_piece is not None and target_piece.color == piece.color:
            print("No puedes capturar tu propia pieza.")
            return False

        self.board.move_piece(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
        
        # Retornar True al final, ya que todas las verificaciones se pasaron
        return True

    def is_within_bounds(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8
