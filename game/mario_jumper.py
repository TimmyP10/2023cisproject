import random
import pygame


pygame.init()

width = 1600
height = 1080
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mario Jumper")

clock = pygame.time.Clock()

coin_image = pygame.image.load('coin.png')
mario_image = pygame.image.load("mario.png")

mario_image = pygame.transform.scale(mario_image, (50, 50))
mario_rect = mario_image.get_rect()
mario_rect.center = (50, 890)

move_speed = 5
jump_speed = 20
gravity = 1
is_jumping = False
jump_count = 0


coins = []
for i in range(25):
    coin_rect = coin_image.get_rect()
    coin_rect.center = (random.randint(0, width), random.randint(0, height))
    coins.append(coin_rect)
coin_image = pygame.image.load('coin.png')
coin_image = pygame.transform.scale(coin_image, (50, 20))
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (width, height))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_rect.x -= move_speed
    elif keys[pygame.K_RIGHT]:
        mario_rect.x += move_speed
    
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            jump_count = jump_speed
    else:
        if jump_count >= -jump_speed:
            mario_rect.y -= jump_count
            jump_count -= gravity
        else:
            is_jumping = False

    if mario_rect.left < 0:
        mario_rect.left = 0
    elif mario_rect.right > width:
        mario_rect.right = width
    if mario_rect.top < 0:
        mario_rect.top = 0
    elif mario_rect.bottom >= height:
        mario_rect.bottom = height
        is_jumping = False
        jump_count = 0

    for coin in coins:
        if mario_rect.colliderect(coin):
            if mario_rect.bottom < coin.top + 10:
                mario_rect.bottom = coin.top
                is_jumping = False
                jump_count = 0

    if len(coins) < 5:
        coin_rect = coin_image.get_rect()
        coin_rect.center = (random.randint(0, width), 0)
        coins.append(coin_rect)

    for coin in coins:
        if coin.top > height:
            coins.remove(coin)

  
    screen.blit(background_image, (0, 0))
    for coin in coins:
        screen.blit(coin_image, coin)
    screen.blit(mario_image, mario_rect)
    pygame.display.flip()

    clock.tick(75)

pygame.quit()
