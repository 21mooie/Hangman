from hangman import *


def main():
    print("Welcome to hangman!")
    while choose_to_play(''):
        word = start_game()
        if word:
            board = set_board(word)
            ### game_won status is returned which can be used to save player's score and increase over time
            game_result(play_game(word, board))
        else:
            print("Num gen > num words in dictionary")


main()
