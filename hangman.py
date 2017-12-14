# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:39:10 2017

@author: Muata Nkosi
"""
import random


def print_word(word):
    """
    shows the word being guessed
    :param word: word being guessed
    :return: word
    """
    return word


def game_status(guess, times_wrong, board):
    """
    Returns true if game is over
    :param guess: checks if the player quit
    :param times_wrong: checks if player ran out of guesses
    :param board: checks board for done
    :return:
    """
    return True if (guess == 'quit' or times_wrong == 0 or win_or_loss(board)) else False


def end_game():
    """
    Shows end of game
    :return:
    """
    print('Thanks for playing!')


def choose_to_play(choice):
    """
    return True if choice == y
    """
    print("Would you like to play?")
    while choice != 'y' and choice != 'n':
        choice = input("Please enter y/n: ")
    if choice == 'n':
        print("ok :(")
        return False
    else:
        return True


def set_hangman(times_wrong):
    """
    sets hangman board
    :param times_wrong: represents how much of hangman should be drawn
    :return: a graphical representation of hangman
    """
    print('_____________')
    print('|            |')
    print('|            |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    return times_wrong


def set_board(word):
    """
    Is run at beginning of game to use board
    :param word: word being used for game
    :return: list to keep track of game
    """
    return ['_']*len(word)


def show_board(board):
    """
    Visual representation of board
    :param board: board being used for game
    :return: visual rep of board for player
    """
    boardstr = ''
    for i in board:
        boardstr += i
        boardstr += ' '
    return boardstr


def show_inc_guess_left(times_wrong):
    """
    Textual showing of how many guesses are left
    :param times_wrong: guesses left
    :return: text
    """
    return 'You can make ' + str(times_wrong) + ' incorrect guesses.'

# def check_win(board):
#     for i in board:
#         if i == '_':
#             return False
#     return True


def valid_guess(guess):
    """
    Checks if guess is valid
    :param guess: player's guess
    :return: a valid guess for game
    """
    while guess.lower() < 'a' or guess.lower() > 'z' and guess != 'quit':
        guess = input('Please guess a letter between a and z: ')
    return guess


def update_board(guess, word, board):
    """
    Updates status of board
    :param guess: player's guess
    :param word: word for game
    :param board: the player's current status at guessing the word
    :return: updated board with the new guess
    """
    for i in range(len(board)):
        if guess == word[i]:
            board[i] = guess
    return board


def correct_guess(guess, word):
    """
    Checks if guess has been correctly made
    :param guess: player's guess
    :param word: word being used in game
    :return: true if guess in word false if not
    """
    check = False
    for i in range(len(word)):
        if guess == word[i]:
            check = True
    return check


# def take_turn(word, times_wrong,board):
#     set_hangman(times_wrong)
#     print(show_board(board))
#     print('You can make ' + str(5 - times_wrong) + ' incorrect guesses.')
#     guess = valid_guess('')
#     if (guess == 'quit'):
#         choose_to_play('n')
#     else:
#         if (correct_guess(guess, word, board)):
#             print("Good job! This is correct!")
#         else:
#             times_wrong += 1
#             print("Incorrect guess. You have " + str(5 - times_wrong) + " guesses left.")
#         # print(board)
#         game_won = check_win(board)
#         print('game won', game_won)
#     return game_won

def win_or_loss(board):
    """
    Checks if player has won
    :param board: the current board
    :return: true if player won false if player loss
    """
    return '_' not in board and len(board) > 0


def play_game(word, board):
    """
    Entire logic of hangman
    :param word: word to be used for game
    :param board: keeps status of game's guesses
    :return: if player won or loss
    """
    game_done = False
    times_wrong = 5
    while not game_done:

        #  sets round up   ####
        set_hangman(times_wrong)
        print(show_board(board))
        print(show_inc_guess_left(times_wrong))

        guess = valid_guess('')
        if guess != 'quit':
            if correct_guess(guess, word):
                board = update_board(guess, word, board)
                print("Good job! This is correct!")
            else:
                times_wrong = decrease_times_wrong(times_wrong)
        print(show_board(board))
        game_done = game_status(guess, times_wrong, board)
    return win_or_loss(board)


def decrease_times_wrong(times_wrong):
    """
    after incorrect guess will update player's number of guesses left
    :param times_wrong: current number of guesses left
    :return: updated number of guesses left
    """
    return times_wrong-1


def ran_num_gen():
    """
    Generate a pseudo-random number
    :return: psuedo-random number
    """
    x = random.randint(0, 69902)
    return x


def find_dict():
    """
    returns a dictionary
    :return: dictionary
    """
    dictionary = 'wordlist.txt'
    return dictionary


def get_word(num, dictionary):
    """
    Picks word for game
    :param num: random number
    :param dictionary: dictionary
    :return: returns the num word in the dictionary for game
    """
    word = 'emptyword'
    try:
        with open(dictionary) as txtfile:
            for i in range(num+1):
                word = txtfile.readline()[0:-1]
    except FileNotFoundError:
        raise FileNotFoundError('cannot open dictionary/find word')

    if not word:
        word = 'emptyword'
    return word


def start_game():
    """
    Starts hangman
    :return: word to be used for game
    """
    print("Yay! Let's play!")
    # figure out which dictionary
    # grab number of lines in file
    # pick random number within file
    try:
        word = get_word(ran_num_gen(), find_dict())
        print(print_word(word))
    except Exception:
        raise Exception("Error Game Cannot Start")
    return word


def game_result(status):
    """
    Updates result of game
    :param status: true if game was won false if loss
    :return: null
    """
    if status:
        print("You won! Congrats!")
    else:
        print("Sorry, you lost. Try again next time.")
    end_game()