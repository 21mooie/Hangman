# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:39:10 2017

@author: Muata Nkosi
"""
import random
import tkinter 

def game_status(game_won,times_wrong,guess):
    if (guess!='quit' and not game_won and times_wrong<5):
        return False
    else:
        if (guess == 'quit'):
            print('stupid quitter :p')
        elif (game_won and times_wrong>5):
            print("Congrats You won!")
        elif (game_won == False and times_wrong==5):
            print("Too bad you lose!")
        end_game()
        return True

def end_game():
    print('Thanks for playing!')

def choose_to_play(choice):
    while (choice != 'y' and choice != 'n'):
        choice = input("Please enter y/n: ")
    if (choice=='n'):
        print("ok :(")
    else:
        run_game()

def set_hangman(times_wrong):
    print('_____________')
    print('|            |')
    print('|            |')


    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')


def set_board(board):
    boardstr = ''
    for i in board:
        boardstr+=i
        boardstr+=' '

    print(boardstr)

def check_win(board):
    for i in board:
        if i == '_':
            return False
    return True

def valid_guess(guess):
    while (guess.lower() < 'a' or guess.lower() > 'z' and guess!='quit'):
        guess = input('Please guess a letter between a and z: ')
    return guess


def correct_guess(guess,word,board):
    check = False
    for i in range(len(word)):
        if guess == word[i]:
            check = True
            board[i] = guess
    return check


def play_game(word):
    game_done = False
    game_won = False
    times_wrong = 0
    board = ['_']*len(word)
    while not (game_done):
        set_hangman(times_wrong)
        set_board(board)
        print('You can make ' + str(5-times_wrong) + ' incorrect guesses.')
        guess = valid_guess('')
        if (guess=='quit'):
            choose_to_play('n')
            game_done = True
        else:
            if (correct_guess(guess,word,board)):
                print("Good job! This is correct!")
            else:
                times_wrong+=1
                print("Incorrect guess. You have " + str(5-times_wrong) + " guesses left.")
            #print(board)
            game_won = check_win(board)
            print('game won',game_won)
        game_done = game_status(game_won,times_wrong,guess)
        print('game done',game_done)
    if (guess!='quit'):
        print("Do you want to play again?")
        choose_to_play('')


def run_game():
    print("Yay! Let's play!")
    x = random.randint(0,69902)
    with open ('wordlist.txt') as txtfile:
        for i in range(x+1):
            word = txtfile.readline()[0:-1]
    print(word)
    play_game(word)


def main():
    print("Welcome to hangman! Would you like to play?")
    choose_to_play('')
main()
