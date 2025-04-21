import pygame
from sys import exit
from random import randint
import types
def display_time():
    current_time=pygame.time.get_ticks() - start_time
    #start_time+=current_time
    score_surface = test_font.render(f"{current_time}", True, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(
        score_surface,score_rect)
    return current_time
def obstacle_mouvement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5
            if obstacle_rect.bottom==300:
                
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surface,obstacle_rect)
        obstacle_list=[obstacle_rect for obstacle_rect in obstacle_list if obstacle_rect.x>-100]
        return obstacle_list
    else:
        return []
def collisions(player, obstacles):
    for obstacle_rect in obstacles:
        if player.colliderect(obstacle_rect):
            return False
    return True
def player_animation():
    global player_real_surf,player_index
    if player_rect.bottom<300:
        player_real_surf=player_jump
    else:
        player_index+=0.1
        if player_index>len(player_walk): player_index=0
        player_real_surf=player_walk[int(player_index)]
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Load assets
sky_surface = pygame.image.load("UltimatePygameIntro/graphics/Sky.png").convert()
ground_surface = pygame.image.load("UltimatePygameIntro/graphics/ground.png").convert()
test_font = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 20)


# Snail
snail_surface = pygame.image.load("UltimatePygameIntro/graphics/snail/snail1.png").convert_alpha()
snail_surface_2 = pygame.image.load("UltimatePygameIntro/graphics/snail/snail2.png").convert_alpha()
snail_frame=[snail_surface,snail_surface_2]
snail_rect = snail_surface.get_rect(midbottom=(600, 300))
#Fly 
fly_surface=pygame.image.load("UltimatePygameIntro/graphics/Fly/Fly1.png")
fly_surface_2=pygame.image.load("UltimatePygameIntro/graphics/Fly/Fly2.png")
fly_frame=[fly_surface,fly_surface_2]
obstacle_list=[]

# Player
player_surf = pygame.image.load("UltimatePygameIntro/graphics/Player/player_walk_1.png").convert_alpha()
player_surf_2=pygame.image.load("UltimatePygameIntro/graphics/Player/player_walk_2.png").convert_alpha()
player_walk=[player_surf,player_surf_2]
player_index=0
player_jump=pygame.image.load("UltimatePygameIntro/graphics/Player/jump.png").convert_alpha()
player_real_surf=player_walk[player_index]
player_rect = player_real_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
#Player display when lost game
player_stand=pygame.image.load("UltimatePygameIntro/graphics/Player/player_stand.png").convert_alpha()
player_stand_scale=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand_scale.get_rect(center=(400,200))


# Game texts
welcome_text_surface=test_font.render("Runner",True,(111,196,169))
welcome_text_rect=welcome_text_surface.get_rect(center=(400,50))
press_enter_text=test_font.render("Press ENTER to Start",True,(111,196,169))
press_enter_rect=press_enter_text.get_rect(center=(400,350))
#game active state
game_active=False
start_time=0
score=0

#Obstacle
obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1500)
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
                
                start_time=pygame.time.get_ticks()
        if event.type==obstacle_timer and game_active:
            if randint(0,2):
                    obstacle_list.append(snail_surface.get_rect(midbottom=(randint(900,1100), 300)))
            else:
                obstacle_list.append(fly_surface.get_rect(midbottom=(randint(900,1100), 210)))
    if game_active:
        score = display_time()
        
        # Background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        #pygame.draw.rect(screen, "#c0e8ec", score_rect, 20)
       # screen.blit(score_surface, score_rect)

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
        player_animation()

        # Stop at ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        #Obstacle mpuvement
       # obstacle_rect_list = obstacle_mouvement(obstacle_list)
        #game_active=collisions(player_rect,obstacle_rect_list)
        # Collision
        if player_rect.colliderect(snail_rect):
           game_active=False
           
        screen.blit(player_real_surf, player_rect)
        display_time()
    else:
        score_message=test_font.render(f"Your score is : {score}",True,(111,196,169))
        score_rect=score_message.get_rect(center=(400,350))
        snail_rect.right=0
        obstacle_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0
        screen.fill((94,129,162))
        if score==0:
            screen.blit(press_enter_text,press_enter_rect)
        else:
            screen.blit(score_message,score_rect)
        screen.blit(welcome_text_surface,welcome_text_rect)
        screen.blit(player_stand_scale,player_stand_rect)
        
        
   
    pygame.display.update()
    clock.tick(60)
