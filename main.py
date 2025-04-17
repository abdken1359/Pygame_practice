import pygame
pygame.init()
screen= pygame.display.set_mode((800,500))
print("Hello World")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    #Draw all elements
    #Update  everything
    pygame.display.init()

