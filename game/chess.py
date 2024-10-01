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
        # Verificar si las posiciones están dentro del tablero
        is_valid = True
        if not self.is_within_bounds(start_pos) or not self.is_within_bounds(end_pos):
            print("Coordenadas fuera de rango.")
            is_valid = False

        piece = self.board.get_piece(start_pos[0], start_pos[1])
        if is_valid and piece is None:
            print("No hay pieza en la posición de origen.")
            is_valid = False

        if is_valid and piece.color != self.turn:
            print("No es tu turno.")
            is_valid = False

        if is_valid and not piece.move(start_pos, end_pos):
            print("Movimiento inválido para la pieza.")
            is_valid = False

        target_piece = self.board.get_piece(end_pos[0], end_pos[1])
        if is_valid and target_piece is not None and target_piece.color == piece.color:
            print("No puedes capturar tu propia pieza.")
            is_valid = False

        if is_valid:
            self.board.move_piece(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
            self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
        
        return is_valid

    def is_within_bounds(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8
