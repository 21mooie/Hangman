import unittest
from hangman import *


# noinspection SpellCheckingInspection
class HangmanTestCase(unittest.TestCase):
    """
    Unit test for all methods in hangman.py class except:
        print_word(word)
        end_game()
        play_game(word,board)
        game_result(status)
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
        self.assertEqual(find_dict(), 'wordlist.txt')
        self.assertNotEqual(find_dict(), 'notwordlist.txt')

    def test_get_word(self):
        #TEST NO ERROR ON CORRECT FILE OPEN
        #TEST word == '' IF NUM GEN EXCEEDS NUM WORDS IN DIC
        #TEST FileNotFoundError raises on dictionary not found

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
        for i in range(100):
            try:
                start_game()
            except Exception:
                self.fail('game not started')


    def test_set_board(self):
        self.assertEqual(len(set_board('')), 0)
        self.assertEqual(len(set_board('a')), 1)
        self.assertEqual(len(set_board('zzzzzzzzzzzzzz')), 14)
        self.assertEqual(len(set_board('zaz')), 3)

    #def test_play_game(self):
    #    word = 'a'
    #    play_game(word,set_board(word))

    #def test_take_turn(self):
        #design take turn test to test that board & times_wrong matches

    # def test_game_status(self):
    #
    # def test_set_hangman(self):
    #
    # def test_set_board(self):
    #
    # def test_show_board(self):
    #
    # def test_valid_guess(self):
    #
    # def test_update_board(self):
    #
    # def test_correct_guess(self):
    #
    # def test_win_or_loss(self):
    #
    # def test_decrease_times_wrong(self):


if __name__ == '__main__':
    unittest.main()
