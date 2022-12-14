#import libraries and modules
import pygame, sys
from pygame import display, event, draw
from numpy import zeros

#initialize pygame modules, set screen and caption
pygame.init()
screen = display.set_mode((550,550))
display.set_caption("Tic Tac Toe")

#colors
red = (249, 66, 58)
line_color = (210, 55, 53)
white = (255,255,255)
grey = (50, 50, 50)
screen.fill(red)

#initialize relevant variables and matrices
board = zeros((3,3))
gap = 550 / 3
player = 1

#draw board lines
draw.line(screen, line_color, (0, gap), (550, gap), 15)
draw.line(screen, line_color, (0, gap*2), (550, gap*2), 15)
draw.line(screen, line_color, (gap, 0), (gap, 550), 15)
draw.line(screen, line_color, (gap*2, 0), (gap*2, 550), 15)

#draw circle or cross depending on player
def draw_figures():
  for row in range(0,3):
    for col in range(0,3):
      if board[row][col] == 1:
        x = int(col * gap + gap / 2)
        y = int(row * gap + gap / 2)
        draw.circle(screen, white, (x,y), 60, 15)
      if board[row][col] == 2:
        draw.line(screen, grey, (col*gap+50, row*gap+gap-50), (col*gap+gap-50, row*gap+50), 15)
        draw.line(screen, grey, (col*gap+50, row*gap+50), (col*gap+gap-50, row*gap+gap-50), 15)

#draw vertical winner line
def draw_vertical(col, player):
  posX = col*gap+gap/2
  if player == 1:
    color = white
  if player == 2:
    color = grey
  draw.line(screen, color, (posX, 15), (posX, 535), 15)

#draw horizontal winner line
def draw_horizontal(row, player):
  posY = row*gap+gap/2
  if player == 1:
    color = white
  if player == 2:
    color = grey
  draw.line(screen, color, (15, posY), (535, posY), 15)

#draw ascending diagonal winner line
def draw_asc_diagonal(player):
  if player == 1:
    color = white
  if player == 2:
    color = grey
  draw.line(screen, color, (15, 535), (535, 15), 15)

#check if a player has won
def check_win(player):
  for col in range(0,3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      draw_vertical(col, player)
      return True

  for row in range(0,3):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      draw_horizontal(row, player)
      return True 

  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    draw_asc_diagonal(player)
    return True
  return False

#game loop
while True:
  allevents = event.get()
  for myevent in allevents:
    if myevent.type == pygame.QUIT:
      sys.exit()
    if myevent.type == pygame.MOUSEBUTTONDOWN:
      mouseX = myevent.pos[0]
      mouseY = myevent.pos[1]
      clicked_row = int(mouseY / gap)
      clicked_col = int(mouseX / gap)
      if board[clicked_row][clicked_col] == 0:
        if player == 1:
          board[clicked_row][clicked_col] = 1
          print(board)
          check_win(player)
          player = 2
          draw_figures()
        elif player == 2:
          board[clicked_row][clicked_col] = 2
          print(board)
          check_win(player)
          player = 1
          draw_figures()

  display.flip()