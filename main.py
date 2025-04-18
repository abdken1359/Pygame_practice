import pygame
from sys import exit
pygame.init()
screen= pygame.display.set_mode((800,500))
pygame.display.set_caption("Maven")

clock = pygame.time.Clock()
test_font=pygame.font.Font("fonts/Chakra_Petch/ChakraPetch-Bold.ttf",40)
display_surface=pygame.Surface((100,50))
display_surface.fill("blue")
image_surface=pygame.image.load("graphics/ground.jpg")
image_height=image_surface.get_height()
text_surface= test_font.render('Hello Player!',False,"orange")
print("Hello World")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(image_surface,(0, 850 - image_height))
    screen.blit(text_surface,(300,50))
    #Draw all elements
    #Update  everything
    pygame.display.update()
    clock.tick(60)
