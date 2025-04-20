import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Load assets
sky_surface = pygame.image.load("UltimatePygameIntro/graphics/Sky.png").convert()
ground_surface = pygame.image.load("UltimatePygameIntro/graphics/ground.png").convert()
test_font = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 20)
score_surface = test_font.render(f"My game", True, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))

# Snail
snail_surface = pygame.image.load("UltimatePygameIntro/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

# Player
player_surf = pygame.image.load("UltimatePygameIntro/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

#game active state
game_active=True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #Jump on user click on player
        if event.type==pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity=-20
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN and game_active==False:
                game_active=True
                player_rect.bottom=300
                snail_rect.right=0
    if game_active:
        
        # Background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, "#c0e8ec", score_rect, 20)
        screen.blit(score_surface, score_rect)

        # Snail movement
        snail_rect.right -= 10
        if snail_rect.right < -100:
            snail_rect.right = 800
        screen.blit(snail_surface, snail_rect)

        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom >= 300:
            player_gravity = -20  # Jump force
        
        
        # Gravity
        player_gravity += 1  # Gravity acceleration
        player_rect.y += player_gravity

        # Stop at ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        # Collision
        if player_rect.colliderect(snail_rect):
           game_active=False
           
        screen.blit(player_surf, player_rect)
    else:
        screen.fill("yellow")
   
    pygame.display.update()
    clock.tick(60)
