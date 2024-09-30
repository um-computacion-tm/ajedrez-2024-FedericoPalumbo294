import sys
import os
import unittest
from unittest.mock import patch

# Agrega el directorio raíz del proyecto a la ruta de búsqueda de módulos de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.chess import Chess
from game.board import Board
from game.piece import Piece

class TestChess(unittest.TestCase):

    # Test agregado para cubrir la línea 25 (validar turno incorrecto)
    @patch('game.board.Board.get_piece')
    @patch('builtins.print')
    def test_not_your_turn(self, mock_print, mock_get_piece):
        juego = Chess()
        board = Board()
        
        # Simulamos que es el turno de las blancas
        juego.turn = "WHITE"
        
        # Creamos una pieza negra
        piece_black = Piece("BLACK", board)
        mock_get_piece.return_value = piece_black
        
        # Intentamos mover la pieza negra cuando es el turno de las blancas
        result = juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("No es tu turno.")
    
    @patch('game.board.Board.get_piece', return_value=None)
    @patch('builtins.print')
    def test_no_piece_in_origin(self, mock_print, mock_get_piece):
        juego = Chess()
        result = juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("No hay pieza en la posición de origen.")
    
    @patch('game.board.Board.get_piece')
    @patch('builtins.print')
    def test_move_out_of_range(self, mock_print, mock_get_piece):
        juego = Chess()
        result = juego.move_piece((-1, 0), (1, 1))
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("Coordenadas fuera de rango.")    
    
    @patch('game.board.Board.get_piece')
    @patch('builtins.print')
    def test_invalid_move(self, mock_print, mock_get_piece):
        juego = Chess()
        board = Board()
        piece = Piece("WHITE", board)
        piece.move = lambda from_pos, to_pos: False
        mock_get_piece.return_value = piece
        result = juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("Movimiento inválido para la pieza.")
    
    @patch('game.board.Board.get_piece')
    @patch('builtins.print')
    def test_capture_own_piece(self, mock_print, mock_get_piece):
        juego = Chess()
        board = Board()
        piece = Piece("WHITE", board)
        piece.move = lambda from_pos, to_pos: True
        # Hace que exista una pieza blanca en el destino y en el origen
        mock_get_piece.side_effect = [piece, piece]
        result = juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el método retorna False
        self.assertFalse(result)
        
        # Verificar que se imprimió el mensaje correcto
        mock_print.assert_called_with("No puedes capturar tu propia pieza.")
    
    @patch('game.board.Board.get_piece')
    @patch('game.board.Board.move_piece')
    def test_valid_move(self, mock_move_piece, mock_get_piece):
        juego = Chess()
        board = Board()
        piece = Piece("WHITE", board)
        piece.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece, None]
        result = juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el método retorna True
        self.assertTrue(result)
        
        # Verificar que se llamó a move_piece
        mock_move_piece.assert_called_with(0, 0, 1, 1)
    
    @patch('game.board.Board.get_piece')
    @patch('game.board.Board.move_piece')
    def test_turn_change(self, mock_move_piece, mock_get_piece):
        juego = Chess()
        board = Board()
        piece = Piece("WHITE", board)
        piece.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece, None]
        juego.move_piece((0, 0), (1, 1))
        
        # Verificar que el turno cambió a BLACK
        self.assertEqual(juego.turn, "BLACK")
        
        # Realizar otro movimiento para cambiar el turno de nuevo
        piece_black = Piece("BLACK", board)
        piece_black.move = lambda from_pos, to_pos: True
        mock_get_piece.side_effect = [piece_black, None]
        juego.move_piece((1, 1), (2, 2))
        
        # Verificar que el turno cambió a WHITE
        self.assertEqual(juego.turn, "WHITE")

    def test_is_within_bounds(self):
        juego = Chess()
        self.assertTrue(juego.is_within_bounds((0, 0)))
        self.assertFalse(juego.is_within_bounds((8, 0)))  # Coordenadas fuera de rango
        self.assertFalse(juego.is_within_bounds((0, 8)))  # Coordenadas fuera de rango

if __name__ == '__main__':
    unittest.main()
