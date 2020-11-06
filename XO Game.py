import pygame

pygame.init()
screen = pygame.display.set_mode(size=(500,500))
pygame.display.set_caption("XO game")
icon = pygame.image.load('71683e880808ae1cbbd3f8b84cb27cdd.jpg')
title = pygame.image.load('maxresdefault (1).jpg')
titlex= 250
titley= 250
pygame.display.set_icon(icon)
def Title():
    screen.blit(title,(titlex,titley))


running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128 ,0))
    Title()
    pygame.display.update()