import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board
from game.king import King
from game.queen import Queen
from game.rook import Rook
from game.bishop import Bishop
from game.knight import Knight
from game.pawn import Pawn

class Game:

    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def print_board(self):
        for row in self.board.board:
            print(" ".join([str(piece) if piece else '.' for piece in row]))
        print()

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board.board[start_row][start_col]

        if piece and piece.color == self.turn:
            if piece.move(start_pos, end_pos, self.board.board):
                captured_piece = self.board.board[end_row][end_col]
                # Solo mover si la pieza de destino es nula o es del color opuesto
                if captured_piece is None or captured_piece.color != piece.color:
                    self.board.board[end_row][end_col] = piece
                    self.board.board[start_row][start_col] = None
                    self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

                    if isinstance(captured_piece, King):
                        print(f"El rey {captured_piece.color} ha sido capturado. ¡Juego terminado!")
                        return False

                    return True
        return False

    def create_piece(self, piece_str):
        if piece_str is None:
            return None

        piece_color = "WHITE" if piece_str[0] == 'W' else "BLACK"  # Determinar el color basado en la primera letra
        piece_type = piece_str[1]  # Obtener el tipo de pieza

        piece_classes = {
            'K': King,
            'Q': Queen,
            'R': Rook,
            'B': Bishop,
            'N': Knight,
            'P': Pawn
        }

        # Crear la pieza sin duplicados
        piece_class = piece_classes.get(piece_type)
        if piece_class:
            return piece_class(piece_color)  # Crear la pieza
        else:
            print(f"Error: Tipo de pieza desconocido '{piece_type}'")
            return None

    def play_turn(self):
        self.print_board()
        print(f"Turno de {self.turn}")
        action = input("Ingrese 'm' para mover, o 'r' para reiniciar: ")

        if action == 'm':
            start_pos = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
            end_pos = tuple(map(int, input("Ingrese la posición final (fila columna): ").split()))
            if not self.move_piece(start_pos, end_pos):
                print("Movimiento inválido, intente de nuevo.")
                return self.play_turn()

        elif action == 'r':
            self.__init__()

        else:
            print("Acción inválida.")
            return False

        return True

    def play(self):
        while True:
            if not self.play_turn():
                break

if __name__ == "__main__":
    game = Game()
    game.play()
