import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import Board
from game.king import King  # Asegúrate de importar la clase King

class Game:

    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def print_board(self):# Método para mostrar el tablero
        for row in self.board.board:
            print(" ".join([str(piece) if piece else '.' for piece in row]))
        print()

    def move_piece(self, start_pos, end_pos): # Añadir parámetros de posición inicial
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board.board[start_row][start_col]

        if piece and piece.color == self.turn:# Añadir condición para verificar el color de la pieza
            if piece.move(start_pos, end_pos, self.board.board):
                captured_piece = self.board.board[end_row][end_col]
                self.board.board[end_row][end_col] = piece
                self.board.board[start_row][start_col] = None
                self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
                
                if isinstance(captured_piece, King):
                    print(f"El rey {captured_piece.color} ha sido capturado. ¡Juego terminado!")
                    return False  # Termina el juego
                
                return True
        return False

    def play_turn(self):# Método para jugar un turno
        self.print_board()
        print(f"Turno de {self.turn}")
        start_pos = tuple(map(int, input("Ingrese la posición inicial (fila columna): ").split()))
        end_pos = tuple(map(int, input("Ingrese la posición final (fila columna): ").split()))

        if not self.move_piece(start_pos, end_pos):

            print("Movimiento inválido, intente de nuevo.")
            return self.play_turn()  # Pedir entrada nuevamente si el movimiento es inválido
        
        self.print_board()  # Imprimir el tablero después de cada intento de movimiento
        return True  # Continuar el juego si el movimiento es válido

    def play(self):
        while True:
            if not self.play_turn():
                break  # Termina el bucle si el juego ha terminado

if __name__ == "__main__":
    game = Game()
    game.play()