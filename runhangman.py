from hangman import *


def main():
    print("Welcome to hangman!")
    while choose_to_play(''):
        # word = start_game()
        gamelist = start_game()
        # if word:
        if gamelist:
            board = set_board(gamelist[0])
            # game_won status is returned which can be used to save player's score and increase over time
            game_result(play_game(gamelist, board),gamelist[0])
        else:
            print("There seems to have been an error")
            print("Num gen > num words in dictionary")
            # break and record this to be figured for why this num was generated.



main()
