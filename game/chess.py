from game.rook import Rook
from game.bishop import Bishop

class Chess:
    def __init__(self):
        # Creamos una matriz de 8x8 para simular el tablero de ajedrez
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Crear una torre blanca en la posición (0, 0)
        self.board[0][0] = Rook("WHITE")

        # Crear un obstáculo en la posición (0, 3)
        self.board[0][3] = Rook("WHITE")

        # Crear un alfil blanco en la posición (0, 2)
        self.board[0][2] = Bishop("WHITE")

    def display(self):
        # Mostrar el tablero
        for row in self.board:
            print(" ".join([str(piece) if piece else "." for piece in row]))

if __name__ == "__main__":
    chess_game = Chess()
    
    # Crear una instancia del alfil en la posición inicial
    bishop = chess_game.board[0][2]

    # Intentar mover el alfil a la posición (2, 4)
    start_pos = (0, 2)
    end_pos = (2, 4)

    if bishop.move(start_pos, end_pos, chess_game.board):
        chess_game.board[end_pos[0]][end_pos[1]] = bishop
        chess_game.board[start_pos[0]][start_pos[1]] = None
        chess_game.display()
    else:
        print("Movimiento inválido")