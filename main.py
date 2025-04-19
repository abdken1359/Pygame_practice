import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
pygame.display.set_caption("Maven")
#Surface
while True:
    #Draw all your element
    #Update everything
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
    
