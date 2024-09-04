import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board

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
                self.board.board[end_row][end_col] = piece
                self.board.board[start_row][start_col] = None
                self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
                return True
        return False

    def play_turn(self):
        self.print_board()
        print(f"Turno de {self.turn}")
        start_pos = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
        end_pos = tuple(map(int, input("Ingrese la posición final (fila columna): ").split()))

        if not self.move_piece(start_pos, end_pos):
            print("Movimiento inválido, intente de nuevo.")

    def play(self):
        while True:
            self.play_turn()

if __name__ == "__main__":
    game = Game()
    game.play()