class Piece:
    # Constructor de la clase Piece
    def __init__(self, color, board):
        self.color = color  # Color de la pieza (por ejemplo, "WHITE" o "BLACK")
        self.board = board  # Referencia al tablero de ajedrez

    # Método para representar la pieza como una cadena
    def __str__(self):
        if self.color == "WHITE":
            return self.white_str  # Devuelve la representación de la pieza blanca
        else:
            return self.black_str  # Devuelve la representación de la pieza negra