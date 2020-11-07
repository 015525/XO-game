from typing import Union

import pygame
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


def isWinning(game_board, ):
    if game_board[1] == ['x', 'x', 'x']:
        print("x")
    if game_board[0] == ['x', 'x', 'x']:
        print("x")
    if game_board[2] == ['x', 'x', 'x']:
        print("x")
    if game_board[0][0] == game_board[1][0] == game_board[2][0] == 'x':
        print("x")
    if game_board[0][1] == game_board[1][1] == game_board[2][1] == 'x':
        print("x")
    if game_board[0][2] == game_board[1][2] == game_board[2][2] == 'x':
        print("x")
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == 'x':
        print("x")
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == 'x':
        print("x")
    if game_board[1] == ['o', 'o', 'o']:
        print("o")
    if game_board[0] == ['o', 'o', 'o']:
        print("o")
    if game_board[2] == ['o', 'o', 'o']:
        print("o")
    if game_board[0][0] == game_board[1][0] == game_board[2][0] == 'o':
        print("o")
    if game_board[0][1] == game_board[1][1] == game_board[2][1] == 'o':
        print("o")
    if game_board[0][2] == game_board[1][2] == game_board[2][2] == 'o':
        print("o")
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == 'o':
        print("o")
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == 'o':
        print("o")


run = True
running = True


def insert():
    player_switch = 0
    pos = input("Enter a position from 1 to 9 : ")
    if pos == '1':

        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (20, 20), (90, 90))
            pygame.draw.line(background, (0, 0, 0), (90, 20), (20, 90))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(50,50),30)
            player_switch = 1
    if pos == '2':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (125, 20), (195, 90))
            pygame.draw.line(background, (0, 0, 0), (195, 20), (125, 90))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(155,50),30)
            player_switch = 1
    if pos == '3':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (230, 20), (300, 90))
            pygame.draw.line(background, (0, 0, 0), (300, 20), (230, 90))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(260,50),30)
            player_switch = 1
    if pos == '4':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (20, 125), (90, 195))
            pygame.draw.line(background, (0, 0, 0), (90, 125), (20, 195))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(50,155),30)
            player_switch = 1
    if pos == '5':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (125, 125), (195, 195))
            pygame.draw.line(background, (0, 0, 0), (195, 125), (125, 195))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(155,155),30)
            player_switch = 1
    if pos == '6':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (230, 125), (300, 195))
            pygame.draw.line(background, (0, 0, 0), (300, 125), (230, 195))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(260,155),30)
            player_switch = 1
    if pos == '7':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (20, 230), (90, 300))
            pygame.draw.line(background, (0, 0, 0), (90, 230), (20, 300))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(50,260),30)
            player_switch = 1
    if pos == '8':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (125, 230), (195, 300))
            pygame.draw.line(background, (0, 0, 0), (195, 230), (125, 300))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(155,260),30)
            player_switch = 1
    if pos == '9':
        if player_switch == 1:
            pygame.draw.line(background, (0, 0, 0), (230, 230), (300, 300))
            pygame.draw.line(background, (0, 0, 0), (300, 230), (230, 300))
            player_switch = 0
        else :
            pygame.draw.circle(background,(0,0,0),(260,260),30)
            player_switch = 1






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos) :
                print("clicked in first")
                pygame.draw.line(background, (0, 0, 0), (10, 10), (50, 50))

    screen.fill((128, 128, 0))
    Title()
    Print()
    insert()
    pygame.display.update()