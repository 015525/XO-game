import pygame

pygame.init()
screen = pygame.display.set_mode(size=(400,500))
pygame.display.set_caption("XO game")
icon = pygame.image.load('71683e880808ae1cbbd3f8b84cb27cdd.jpg')
title = pygame.image.load('maxresdefault (1).jpg')
background = pygame.image.load('WoodTexture.png')
titlex= 40
titley= 5
backx=40
backy=150
pygame.display.set_icon(icon)
def Title():
    screen.blit(title,(titlex,titley))

def Background():
    screen.blit(background,(backx,backy))


running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128 ,0))
    Title()
    Background()
    pygame.display.update()