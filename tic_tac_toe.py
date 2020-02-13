
'''
This a Python implementation of the classic game 'Tic-Tac-Toe'
@author: aashish.mathersiii@gmail.com
'''
#***********************************************************************************************
# variables
#***********************************************************************************************
turn = 'X'
player1 = 'X'
position = 0
pos_array = ['', '', '', '', '', '', '', '', '']
user_response = 'Y'
win = 'NO'
valid_positions = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
valid_responses = ['Y', 'N']
valid_symbols = ['X', 'O']


#***********************************************************************************************
# functions
#***********************************************************************************************

# reset variables
#***********************************************************************************************
def reset_vars():
    global turn
    turn = 'X'
    global player1
    player1 = 'X'
    global position
    position = 0
    global pos_array
    pos_array = ['', '', '', '', '', '', '', '', '']
    global user_response
    user_response = 'Y'
    global win
    win = 'NO'

# player 1
#***********************************************************************************************
def select_player1():
    global turn
    turn = 'T'
    while turn != 'X':
        turn = input('Player 1 select "X" or "O": ')
        if turn == 'O':
            break
        elif turn != 'O':
            print('Enter a valid response!')
            continue

# alternates the turn
#***********************************************************************************************
def alternate_turns():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
# prompts user to input next position
#***********************************************************************************************
def user_position_input():
    global position
    user_input = input("Enter the next position (0-8): ")
    bool_check =  user_input in valid_positions
    while bool_check != True:
        user_input = input('Enter a valid position (0-8): ')
        bool_check =  user_input in valid_positions
    position = user_input

# drawing updated board
#***********************************************************************************************
def update_board():
    print('\t{}\t|\t{}\t|\t{}'.format(pos_array[6], pos_array[7], pos_array[8]))
    print('_________________________________________________')
    print('\t{}\t|\t{}\t|\t{}'.format(pos_array[3], pos_array[4], pos_array[5]))
    print('_________________________________________________')
    print('\t{}\t|\t{}\t|\t{}'.format(pos_array[0], pos_array[1], pos_array[2]))
    print(pos_array)

# updating the position in array
#***********************************************************************************************
def update_position():
    global position
    global pos_array
    pos_array[(int)(position)] = turn

# resetting the board to empty
#***********************************************************************************************
def reset_board():
    global pos_array
    pos_array = ['', '', '', '', '', '', '', '', '']

# checking if anyone has won yet
#***********************************************************************************************
def check_win():
    global win
    # row 1
    if pos_array[0] == turn and pos_array [1] == turn and pos_array[2] == turn:
        win = 'YES'
    # row 2
    elif pos_array[3] == turn and pos_array [4] == turn and pos_array[5] == turn:
        win = 'YES'
    # row 3
    elif pos_array[6] == turn and pos_array [7] == turn and pos_array[8] == turn:
        win = 'YES'
    # dia 1
    elif pos_array[0] == turn and pos_array [4] == turn and pos_array[8] == turn:
        win = 'YES'
    # dia 2
    elif pos_array[6] == turn and pos_array [4] == turn and pos_array[2] == turn:
        win = 'YES'
    # col 1
    elif pos_array[6] == turn and pos_array [3] == turn and pos_array[0] == turn:
        win = 'YES'
    # col 2
    elif pos_array[7] == turn and pos_array [4] == turn and pos_array[1] == turn:
        win = 'YES'
    # col 3
    elif pos_array[8] == turn and pos_array [5] == turn and pos_array[2] == turn:
        win = 'YES'
    else:
        win = 'NO'
    
    if win == 'YES':
        declare_winner()

# declaring a winner
#***********************************************************************************************

def declare_winner():
    if turn == player1:
        print('Player 1 won')
    else:
        print('Player 2 won')

#***********************************************************************************************
# driver program
#***********************************************************************************************
player1 = turn
while user_response == 'Y':
    select_player1()
    update_board()
    while win == 'NO':
        user_position_input()
        update_position()
        update_board()
        check_win()
        alternate_turns()
    reset_board()
    reset_vars()
    user_response = 'T'
    while user_response != 'Y':
        user_response = input('Do you want to play again? (Y/N): ')
        if user_response == 'N':
            break
        elif user_response != 'N':
            print('Enter a valid response!')
            continue

print('Hope you had fun! See ya!')

#***********************************************************************************************
# Pseudo
#***********************************************************************************************

'''
1. player chooses X or O
2. board prints
3. prompt to user for position
4. board prints
5. repeat 3 and 4 until winner
6. prompt to play again
'''


'''
1. ask user to input position
2. update the array
3. draw the board with the updated array
4. repeat until win
'''
#***********************************************************************************************
#***********************************************************************************************
#***********************************************************************************************