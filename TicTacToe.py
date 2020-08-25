# Tic Tac Toe game
# Nhut Trinh
# 08/24/2020
import random

count = 1

theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def winRule():
    global winner
    if (theboard['top-L'] == theboard['top-M'] == theboard['top-R'] != ' '):
        winner = theboard['top-L']
        return True
    elif (theboard['mid-L'] == theboard['mid-M'] == theboard['mid-R'] != ' '):
        winner = theboard['mid-L']
        return True
    elif (theboard['low-L'] == theboard['low-M'] == theboard['low-R'] != ' '):
        winner = theboard['low-L']
        return True
    elif (theboard['top-L'] == theboard['mid-M'] == theboard['low-R'] != ' '):
        winner = theboard['top-L']
        return True
    elif (theboard['low-L'] == theboard['mid-M'] == theboard['top-R'] != ' '):
        winner = theboard['low-L']
        return True
    elif (theboard['top-L'] == theboard['mid-L'] == theboard['low-L'] != ' '):
        winner = theboard['top-L']
        return True
    elif (theboard['top-M'] == theboard['mid-M'] == theboard['low-M'] != ' '):
        winner = theboard['top-M']
        return True
    elif (theboard['top-R'] == theboard['mid-R'] == theboard['low-R'] != ' '):
        winner = theboard['top-R']
        return True
    else:
        return False


def computerChoice():
    key = random.choice(list(theboard.keys()))
    while theboard[key] != ' ':
        key = random.choice(list(theboard.keys()))
    theboard[key] = 'X'
    global count
    count += 1


def playerChoice():
    choice = input()
    if (choice in theboard) and (theboard[choice] == ' '):
        theboard[choice] = 'O'
        global count
        count += 1
    else:
        print('Please enter your choice again!')
        playerChoice()


print('Welcome to the Tic tac Toe game! The computer will go first')

while count < 10:

    computerChoice()
    printBoard(theboard)
    win = winRule()
    if win:
        break
    print('Your turn')
    playerChoice()
    print(count)
    win = winRule()
    if win:
        break

printBoard(theboard)

if winner == 'O':
    print("You are winner!!!")
else:
    print('You lose!')