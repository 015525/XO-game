from typing import Union

import pygame
import time
from pygame import Surface
from pygame.surface import SurfaceType

print("welcome")
board_array = ['' * 3 for i in range(3)]
pygame.init()
screen = pygame.display.set_mode(size=(400, 500))
pygame.display.set_caption("XO game")
background = pygame.image.load('WoodTexture.png')
pygame.draw.line(background, (0, 0, 0), (0, 210), (350, 210))
pygame.draw.line(background, (0, 0, 0), (0, 105), (350, 105))
pygame.draw.line(background, (0, 0, 0), (105, 0), (105, 350))
pygame.draw.line(background, (0, 0, 0), (210, 0), (210, 350))
#pygame.draw.line(background , (0, 0, 0), (0, 0), (50, 50))
icon = pygame.image.load('71683e880808ae1cbbd3f8b84cb27cdd.jpg')
title = pygame.image.load('maxresdefault (1).jpg')
titlex = 40
titley = 5
backx = 40
backy = 150
pygame.display.set_icon(icon)
game_board = [['', '', ''], ['', '', ''], ['', '', '']]
first = pygame.draw.rect(background, (128, 128, 0), (10, 10, 85, 85))
second = pygame.draw.rect(background, (128, 128, 0), (115, 10, 85, 85))
third = pygame.draw.rect(background, (128, 128, 0), (220, 10, 85, 85))
forth = pygame.draw.rect(background, (128, 128, 0), (10, 115, 85, 85))
fifth = pygame.draw.rect(background, (128, 128, 0), (115, 115, 85, 85))
sixth = pygame.draw.rect(background, (128, 128, 0), (220, 115, 85, 85))
seventh = pygame.draw.rect(background, (128, 128, 0), (10, 220, 85, 85))
eighth = pygame.draw.rect(background, (128, 128, 0), (115, 220, 85, 85))
ninth = pygame.draw.rect(background, (128, 128, 0), (220, 220, 85, 85))


def Title():
    screen.blit(title, (titlex, titley))


def Print():
    screen.blit(background, (backx, backy))
    pygame.display.update()
    Title()
def isWinning (game_board) :
    if win == 'x' :
        print("x is the winner")
    if win == 'o' :
        print("o is the winner")

def insert(game_board,raw,col,tile):
    game_board[raw][col] = tile




running = True
#def isWinning():


n=0
player_switch =1
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eights_open = True
ninth_open = True

choice = print("welcome to tic tac toe game ")

while running:


    screen.fill((128, 128, 0))
    Title()
    Print()
    time.sleep(0.25)

    pos = input("Enter a position from 1 to 9 : ")
    if pos == '1' and first_open:
        n += 1
        if player_switch == 1:
            raw = 0
            col = 0
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (20, 20), (90, 90))
            pygame.draw.line(background, (0, 0, 0), (90, 20), (20, 90))
            pygame.display.update()
            player_switch = 2

        else:
            raw = 0
            col = 0
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (50, 50), 30)
            pygame.display.update()
            player_switch = 1
        first_open = False
    elif pos == '2' and second_open:
        n += 1
        if player_switch == 1:
            raw = 0
            col = 1
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (125, 20), (195, 90))
            pygame.draw.line(background, (0, 0, 0), (195, 20), (125, 90))
            player_switch = 2
        else:
            raw = 0
            col = 1
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (155, 50), 30)
            player_switch = 1
        second_open = False
    elif pos == '3' and third_open:
        n += 1
        if player_switch == 1:
            raw = 0
            col = 2
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (230, 20), (300, 90))
            pygame.draw.line(background, (0, 0, 0), (300, 20), (230, 90))
            player_switch = 2
        else:
            raw = 0
            col = 2
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (260, 50), 30)
            player_switch = 1
        third_open = False
    elif pos == '4' and fourth_open:
        n += 1
        if player_switch == 1:
            raw = 1
            col = 0
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (20, 125), (90, 195))
            pygame.draw.line(background, (0, 0, 0), (90, 125), (20, 195))
            player_switch = 2
        else:
            raw = 1
            col = 0
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (50, 155), 30)
            player_switch = 1
        fourth_open = False

    elif pos == '5' and fifth_open:
        n += 1
        if player_switch == 1:
            raw = 1
            col = 1
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (125, 125), (195, 195))
            pygame.draw.line(background, (0, 0, 0), (195, 125), (125, 195))
            player_switch = 2
        else:
            raw = 1
            col = 1
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (155, 155), 30)
            player_switch = 1
        fifth_open = False
    elif pos == '6' and sixth_open:
        n += 1
        if player_switch == 1:
            raw = 1
            col = 2
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (230, 125), (300, 195))
            pygame.draw.line(background, (0, 0, 0), (300, 125), (230, 195))
            player_switch = 2
        else:
            raw = 1
            col = 2
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (260, 155), 30)
            player_switch = 1
        sixth_open = False
    elif pos == '7' and seventh_open:
        n += 1
        if player_switch == 1:
            raw = 2
            col = 0
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (20, 230), (90, 300))
            pygame.draw.line(background, (0, 0, 0), (90, 230), (20, 300))
            player_switch = 2
        else:
            raw = 2
            col = 0
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (50, 260), 30)
            player_switch = 1
        seventh_open = False
    elif pos == '8' and eights_open:
        n += 1
        if player_switch == 1:
            raw = 2
            col = 1
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (125, 230), (195, 300))
            pygame.draw.line(background, (0, 0, 0), (195, 230), (125, 300))
            player_switch = 2
        else:
            raw = 1
            col = 1
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (155, 260), 30)
            player_switch = 1
        eights_open = False
    elif pos == '9' and ninth_open:
        n += 1
        if player_switch == 1:
            raw = 2
            col = 2
            tile = 'x'
            insert(game_board, raw, col, tile)
            pygame.draw.line(background, (0, 0, 0), (230, 230), (300, 300))
            pygame.draw.line(background, (0, 0, 0), (300, 230), (230, 300))
            player_switch = 2
        else:
            raw = 2
            col = 2
            tile = 'o'
            insert(game_board, raw, col, tile)
            pygame.draw.circle(background, (0, 0, 0), (260, 260), 30)
            player_switch = 1
        ninth_open = False
    else:
        print("not avalaible")

    if game_board[1] == ['x', 'x', 'x']:
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0] == ['x', 'x', 'x']:
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[2] == ['x', 'x', 'x']:
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0][0] == 'x' and game_board[1][0] == 'x' and game_board[2][0] == 'x':
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0][1] == 'x' and game_board[1][1] == 'x' and game_board[2][1] == 'x':
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0][2] == 'x' and game_board[1][2] == 'x' and game_board[2][2] == 'x':
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0][0] == 'x' and game_board[1][1] == 'x' and game_board[2][2] == 'x':
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[0][2] == 'x' and game_board[1][1] == 'x' and game_board[2][0] == 'x':
        win = 'x'
        isWinning(game_board)
        running = False
    elif game_board[1] == ['o', 'o', 'o']:
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0] == ['o', 'o', 'o']:
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[2] == ['o', 'o', 'o']:
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0][0] == 'o' and  game_board[1][0] == 'o' and game_board[2][0] == 'o':
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0][1] == 'o' and game_board[1][1] == 'o' and  game_board[2][1] == 'o':
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0][2] == 'o' and  game_board[1][2] == 'o' and  game_board[2][2] == 'o':
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0][0] == 'o' and  game_board[1][1] == 'o' and  game_board[2][2] == 'o':
        win = 'o'
        isWinning(game_board)
        running = False
    elif game_board[0][2] == 'o' and  game_board[1][1] == 'o' and  game_board[2][0] == 'o':
        win = 'o'
        isWinning(game_board)
        running = False
    elif n == 9 :
        print("Tie")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if running == False:
            break







    Title()
    Print()
  #  insert(player_switch=int(input("please enter the player no. : ")))
    pygame.display.update()