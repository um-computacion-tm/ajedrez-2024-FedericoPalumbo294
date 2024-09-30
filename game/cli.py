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
                self.board.board[end_row][end_col] = piece
                self.board.board[start_row][start_col] = None
                self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

                if isinstance(captured_piece, King):
                    print(f"El rey {captured_piece.color} ha sido capturado. ¡Juego terminado!")
                    return False

                return True
        return False

    def save_game(self, filename="savegame.json"):
        game_state = {
            "board": [[self.serialize_piece(piece) for piece in row] for row in self.board.board],
            "turn": self.turn
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f)
        print("Partida guardada exitosamente.")

    def serialize_piece(self, piece):
        if piece is None:
            return None
        return f"{piece.color[0]}{piece.__class__.__name__[0]}"  # Guardar como "WK", "BQ", etc.

    def load_game(self, filename="savegame.json"):
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                self.board.board = [[self.create_piece(piece) for piece in row] for row in game_state['board']]
                self.turn = game_state['turn']
            print("Partida cargada exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de partida guardada.")
        except Exception as e:
            print(f"Ocurrió un error al cargar la partida: {e}")

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

        return piece_classes.get(piece_type, lambda color: None)(piece_color)

    def play_turn(self):
        self.print_board()
        print(f"Turno de {self.turn}")
        action = input("Ingrese 'm' para mover, 's' para guardar, 'c' para cargar, o 'r' para reiniciar: ")

        if action == 'm':
            start_pos = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
            end_pos = tuple(map(int, input("Ingrese la posición final (fila columna): ").split()))
            if not self.move_piece(start_pos, end_pos):
                print("Movimiento inválido, intente de nuevo.")
                return self.play_turn()

        elif action == 's':
            self.save_game()

        elif action == 'c':
            self.load_game()

        elif action == 'r':
            self.__init__()

        else:
            print("Acción inválida.")
            return False

        self.print_board()
        return True

    def play(self):
        while True:
            if not self.play_turn():
                break

if __name__ == "__main__":
    game = Game()
    game.play()
