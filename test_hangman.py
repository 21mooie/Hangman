import unittest
# import mock
from hangman import *


# noinspection SpellCheckingInspection
class HangmanTestCase(unittest.TestCase):
    """
    Unit test for all methods in hangman.py class except:
        end_game()
        play_game(word,board)
        game_result(status)
        find_num_lines_in_dic(dictionary)
    """

    def test_choose_to_play(self):
        """
        Test option to play with all possible parameter for entrance
        :return:
        """
        self.assertFalse(choose_to_play('n'))
        self.assertTrue(choose_to_play('y'))

    def test_ran_num_gen(self):
        for i in range(69903):
            self.assertLessEqual(ran_num_gen(), 69902)

    def test_find_dict(self):
        # self.assertEqual(find_dict(), 'wordlist.txt')
        # self.assertNotEqual(find_dict(), 'notwordlist.txt')
        find_dict()

    def test_get_word(self):
        # TEST NO ERROR ON CORRECT FILE OPEN
        # TEST word == '' IF NUM GEN EXCEEDS NUM WORDS IN DIC
        # TEST FileNotFoundError raises on dictionary not found

        try:
            print(get_word(0, 'wordlist.txt'))
        except FileNotFoundError:
            self.fail('get_word() could not open wordlist.txt')

        try:
            print(get_word(69905, 'wordlist.txt'))
        except FileNotFoundError:
            self.fail('get_word() could not open wordlist.txt')
        # self.assertEqual(get_word(69903, 'wordlist.txt'), '')
        # with self.assertRaises(FileNotFoundError):
        #     get_word(50, 'notwordlist.txt')

    def test_start_game(self):
        for i in range(10):
            try:
                start_game()
            except Exception:
                self.fail('game not started')


    def test_set_board(self):
        self.assertEqual(len(set_board('')), 0)
        self.assertEqual(len(set_board('a')), 1)
        self.assertEqual(len(set_board('zzzzzzzzzzzzzz')), 14)
        self.assertEqual(len(set_board('zaz')), 3)

    #def test_take_turn(self):
    #design take turn test to test that board & times_wrong matches

    def test_game_status(self):
        # singly true
        self.assertTrue(game_status('quit',1,set_board('word')))
        self.assertTrue(game_status('a', 0, set_board('word')))
        self.assertTrue(game_status('a', 1, ['a']))

        #doubly true
        self.assertTrue(game_status('quit', 0,set_board('word')))
        self.assertTrue(game_status('quit', 1, ['a']))
        self.assertTrue(game_status('a', 0, ['a']))

        #all true
        self.assertTrue(game_status('quit', 0, ['a']))

        #false
        self.assertFalse(game_status('a', 1, set_board('word')))
        self.assertFalse(game_status('a', 1, set_board('')))
        self.assertFalse(game_status('a', -4, set_board('word')))

    def test_set_hangman(self):
        self.assertEqual(set_hangman('word'),'word')
        self.assertEqual(set_hangman(''), '')

    def test_set_board(self):
        self.assertEqual(len([]),len(set_board('')))
        self.assertEqual(['_'],set_board('a'))

    def test_show_board(self):
        self.assertEqual('a _ ',show_board(['a','_']))
        self.assertEqual('_ ', show_board(['_']))

    def test_valid_guess(self):
        #with mock.patch('__builtin__.input', return_value='a'):
        self.assertEqual('a',valid_guess('a'))
    def test_update_board(self):
        self.assertEqual(['a','_'],update_board('a','at',set_board('at')))
        self.assertEqual(['a', 'a'], update_board('a', 'aa', set_board('aa')))
    def test_correct_guess(self):
        self.assertTrue(correct_guess('a','apple'))
        self.assertFalse(correct_guess('z', 'apple'))
        self.assertFalse(correct_guess('', 'apple'))
    def test_win_or_loss(self):
        self.assertTrue(win_or_loss(['a']))
        self.assertTrue(win_or_loss(['']))
        self.assertFalse(win_or_loss(['_']))
        self.assertFalse(win_or_loss([]))
    def test_decrease_times_wrong(self):
        self.assertEqual(4,decrease_times_wrong(5))


if __name__ == '__main__':
    unittest.main()
