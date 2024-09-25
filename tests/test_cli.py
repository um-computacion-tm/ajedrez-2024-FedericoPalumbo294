import sys
import os
import unittest
import json

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.cli import Game  # Asegúrate de importar la clase Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_load_game(self):
        # Estado de juego de ejemplo
        game_state = {
            "board": [[None] * 8 for _ in range(8)],
            "turn": "WHITE"
        }
        
        # Simula guardar el estado en un archivo JSON
        with open('test_game_state.json', 'w') as f:
            json.dump(game_state, f)

        # Cargar el juego desde el archivo
        self.game.load_game('test_game_state.json')

        self.assertEqual(self.game.turn, "WHITE")

        loaded_board = self.game.board.board
        expected_board = [[None] * 8 for _ in range(8)]
        
        for row in range(8):
            for col in range(8):
                loaded_piece = loaded_board[row][col]
                expected_piece = expected_board[row][col]
                self.assertEqual(
                    str(loaded_piece) if loaded_piece else None,
                    str(expected_piece) if expected_piece else None
                )

        # Limpia el archivo después de la prueba
        os.remove('test_game_state.json')

if __name__ == "__main__":
    unittest.main()
