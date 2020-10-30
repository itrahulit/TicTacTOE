from IPython.display import clear_output

def display_board(board):
  clear_output()
  print('   |   | ')
  print(' '+board[7]+' | ' +board[8]+' | ' +board[9])
  print('   |   | ')
  print('-------------')
  print('   |   | ')
  print(' '+board[4]+' | ' +board[5]+' | ' +board[6])
  print('   |   | ')
  print('-------------')
  print('   |   | ')
  print(' '+board[1]+' | ' +board[2]+' | ' +board[3])
  print('   |   | ')


test_board = ['#','X','O','x','O','X','O','X','O','X']
display_board(test_board)


def player_input():

  '''
  OUTPUT = (player 1 marker, player 2 marker)
  '''
  marker = ''

  while not (marker == 'X' or marker == 'O'):
    marker = input('Player1: choose X or O: ').upper()
  
  if marker == 'X':
    return ('X','O')
  else:
    return ('X','O')

def place_marker(board, marker, position):
  board[position] = marker

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, marker):



  #win tic tak toe?

  #all rows and check to see if they all share the same marker?
  return((board[1] == marker and board[2] == marker and board[3] == marker) or 
  (board[4] == marker and board[5] == marker and board[6] == marker) or 
  (board[7] == marker and board[8] == marker and board[9] == marker) or 
  (board[1] == marker and board[4] == marker and board[7] == marker) or
  (board[2] == marker and board[5] == marker and board[8] == marker) or
  (board[3] == marker and board[6] == marker and board[9] == marker) or
  (board[1] == marker and board[5] == marker and board[9] == marker) or 
  (board[3] == marker and board[5] == marker and board[7] == marker))
  #all columns, check if all marker matches ?

  #2 diagonals, check to see matching?

import random

def choose_first():
  
  flip = random.randint(0,1)

  if flip == 0:
    return 'player 1'
  else:
    return 'player 2'
    
def space_check(board, position):

  return board[position] == ' '

def full_board_check(board):

  for i in range(1,10):
    if space_check(board,i):
      return False
  return True

def player_choice(board):

  position = 0

  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input('choose a position: (0-9) '))
  return position

def replay():
  choice = input('play again? enter Yes or No')
  return choice == 'Yes'

#while loop to keep running the game
print('Welcome to Tic Tac TOE')

while True:
  #play the game here

  ##Set everything up (board, whos first, choose marker X, O)

  the_board = [' ']*10
  player1_marker,player2_marker = player_input()

  turn = choose_first()
  print(turn + ' will go first')

  play_game = input('ready to play? y or n? ')

  if play_game == 'y':

    game_on = True 
  else:
    game_on = False

  ##Game play
  while game_on:

    if turn == 'player 1':
      #show the board
      display_board(the_board)
      #choose the position 
      position = player_choice(the_board)

      #place the marker on the position 
      place_marker(the_board,player1_marker,position) 
      #check if they won
      if win_check(the_board,player1_marker):
        display_board(the_board)
        print('Player 1 has won!!')
        game_on = False 
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('Tie Game!!')
          break 
        else: 
          turn = 'player 2'
      #check if the tie 

      #no tie and no win? then next player turn 


    ### Player 1 turn
    else:
      #show the board
      display_board(the_board)
      #choose the position 
      position = player_choice(the_board)

      #place the marker on the position 
      place_marker(the_board,player2_marker,position) 
      #check if they won
      if win_check(the_board,player2_marker):
        display_board(the_board)
        print('Player 2 has won!!')
        game_on = False 
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('Tie Game!!')
          break 
        else: 
          turn = 'player 1'

  ### player 2 turn  

  if not replay():
    break 
#break out of the while loop on replay()
print(game_on)
