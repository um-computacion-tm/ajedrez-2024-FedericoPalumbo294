import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, mock_open
from game.cli import Game
from game.board import Board
from game.king import King

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_print_board(self):
        with patch('builtins.print') as mocked_print:
            self.game.print_board()
            self.assertTrue(mocked_print.called)

    def test_move_piece_valid(self):
        self.game.board.board[0][0] = King("WHITE")
        self.game.turn = "WHITE"
        self.assertTrue(self.game.move_piece((0, 0), (1, 1)))

    def test_move_piece_invalid(self):
        self.game.board.board[0][0] = King("WHITE")
        self.game.turn = "BLACK"
        self.assertFalse(self.game.move_piece((0, 0), (1, 1)))

    def test_move_piece_no_piece(self):
        self.assertFalse(self.game.move_piece((0, 0), (1, 1)))  # Línea 40

    def test_save_game(self):
        with patch('builtins.open', mock_open()) as mocked_file:
            with patch('json.dump') as mocked_json_dump:
                self.game.save_game()
                mocked_file.assert_called_once_with('savegame.json', 'w')
                self.assertTrue(mocked_json_dump.called)

    def test_load_game(self):
        game_state = {
            "board": [[None for _ in range(8)] for _ in range(8)],
            "turn": "WHITE"
        }
        with patch('builtins.open', mock_open(read_data=json.dumps(game_state))) as mocked_file:
            self.game.load_game()
            mocked_file.assert_called_once_with('savegame.json', 'r')
            self.assertEqual(self.game.turn, "WHITE")

    def test_load_game_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch('builtins.print') as mocked_print:
                self.game.load_game()
                mocked_print.assert_called_with("No se encontró el archivo de partida guardada.")

    def test_load_game_exception(self):
        with patch('builtins.open', side_effect=Exception("Error")):
            with patch('builtins.print') as mocked_print:
                self.game.load_game()
                self.assertTrue(mocked_print.called)

    def test_play_turn_move(self):
        with patch('builtins.input', side_effect=['m', '0 0', '1 1']):
            with patch.object(self.game, 'move_piece', return_value=True):
                self.assertTrue(self.game.play_turn())

    def test_play_turn_save(self):
        with patch('builtins.input', side_effect=['s']):
            with patch.object(self.game, 'save_game'):
                self.assertTrue(self.game.play_turn())

    def test_play_turn_load(self):
        with patch('builtins.input', side_effect=['c']):
            with patch.object(self.game, 'load_game'):
                self.assertTrue(self.game.play_turn())

    def test_play_turn_restart(self):
        with patch('builtins.input', side_effect=['r']):
            self.assertTrue(self.game.play_turn())

    def test_play_turn_invalid(self):
        with patch('builtins.input', side_effect=['x']):
            with patch('builtins.print') as mocked_print:
                self.assertFalse(self.game.play_turn())  # Líneas 74-89
                mocked_print.assert_called_with("Acción inválida.")

    def test_play(self):
        with patch.object(self.game, 'play_turn', side_effect=[True, False]):
            self.game.play()

    def test_play_quit(self):
        with patch.object(self.game, 'play_turn', return_value=False):
            self.game.play()  # Línea 101

if __name__ == '__main__':
    unittest.main()