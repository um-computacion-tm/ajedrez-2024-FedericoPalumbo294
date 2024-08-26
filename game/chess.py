from rook import Rook

# Crear un tablero vacío (8x8)
board = [[None for _ in range(8)] for _ in range(8)]

# Crear una torre blanca en la posición (0, 0)
rook = Rook("WHITE")
board[0][0] = rook

#creo un obstaculo en la posicion (0, 3)
board[0][3] = Rook("WHITE")

# Intentar mover la torre a la posición (0, 5)
start_pos = (0, 0)
end_pos = (0, 5)

if rook.move(start_pos, end_pos, board):
    print("Movimiento válido")
else:
    print("Movimiento inválido")