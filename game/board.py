from .rook import Rook
from .pawn import Pawn
from .queen import Queen
from .king import King
from .bishop import Bishop
from .knight import Knight

class Board:

    def __init__(self):
    # Creamos una matriz de 8x8 para simular el tablero de ajedrez:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        ################################################################
        ################# Posicionamiento de piezas Negras ##############
        #################################################################

        # Posicionamos Torres Negras:
        self.board[0][0] = Rook("BLACK")
        self.board[0][7] = Rook("BLACK")

        # Posicionamos Caballos Negros:
        self.board[0][1] = Knight("BLACK") 
        self.board[0][6] = Knight("BLACK") 

        # Posicionamos Alfiles Negros:
        self.board[0][2] = Bishop("BLACK")
        self.board[0][5] = Bishop("BLACK")

        # Posicionamos Reyes Negros:
        self.board[0][3] = Queen("BLACK")
        self.board[0][4] = King("BLACK")   

        # Posicionamos Peones Negros:         
        for i in range(8):                 
            self.board[1][i] = Pawn("BLACK")

        ################################################################
        ############### Posicionamiento de piezas Blancas ##############
        ################################################################ 
        
        # Posicionamos Torres Blancas:
        self.board[7][0] = Rook("WHITE")
        self.board[7][7] = Rook("WHITE")
        
        # Posicionamos Caballos Blanca:
        self.board[7][1] =Knight("WHITE")
        self.board[7][6] = Knight("WHITE")

        # Posicionamos Alfiles Blanca:
        self.board[7][2] = Bishop("WHITE")
        self.board[7][5] = Bishop("WHITE")

        # Posicionamos Reyes Blanca:
        self.board[7][3] = Queen("WHITE")
        self.board[7][4] = King("WHITE")

        # Posicionamos Peones Blanca:        
        for i in range(8):                 
            self.board[6][i] = Pawn("WHITE")

            
    def get_piece(self, row, col):         
        # Devolver la pieza en la posición dada         
        return self.board[row][col] 
     
chess_board = Board()