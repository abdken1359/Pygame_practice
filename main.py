import pygame
from sys import exit
pygame.init()
screen= pygame.display.set_mode((800,500))
pygame.display.set_caption("Maven")

clock = pygame.time.Clock()
test_font=pygame.font.Font("fonts/Chakra_Petch/ChakraPetch-Bold.ttf",40)
display_surface=pygame.Surface((100,50))
display_surface.fill("blue")
image_surface=pygame.image.load("graphics/ground.jpg").convert()
snail_image=pygame.image.load("graphics/snail.svg").convert_alpha()
snail_x_pos=1
player_x_pos=80
player_surface=pygame.image.load("UltimatePygameIntro/graphics/Player/player_walk_1.png")
player_rect=player_surface.get_rect(topleft=(player_x_pos,400))
image_height=image_surface.get_height()
text_surface= test_font.render('Hello Player!',True,"orange")
print(player_rect.left)
print("Hello World")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(image_surface,(0, 850 - image_height))
    screen.blit(snail_image,(snail_x_pos,150))
    screen.blit(player_surface,player_rect)
    snail_x_pos+=1
    if snail_x_pos==700:
        snail_x_pos=+10
    player_x_pos+=1
    player_rect.left+=1
    if player_x_pos==400:
        player_x_pos=80
        player_rect.left=80
    screen.blit(text_surface,(300,50))
    
        
    #Draw all elements
    #Update  everything
    pygame.display.update()
    clock.tick(60)
    
