import pygame
import math

pygame.init()

screen = pygame.display.set_mode((900, 600))
w, h = pygame.display.get_surface().get_size()

pygame.display.set_caption("Olioni's Game")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.surf = pygame.image.load('images/dwayne.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (size, size))
        self.rect = self.surf.get_rect(midbottom = (x, y))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.surf = pygame.image.load('images/ground 2.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (size, 140))
        self.rect = self.surf.get_rect(midbottom = (x, y))

# random variables
ground_level = 650

# define background
sky_surf = pygame.image.load('images/sky.png')

# define ground
ground = Platform((w / 2), ground_level, w)

# define player
player = Sprite(100, 300, 100)

# player variables
velocity = 1

player_velocityX = 0
player_velocityY = 0

player_x_pos = w / 2
player_y_pos = h / 2

# random variables
gravity = 0.5
touchingGround = False

# -- GAME LOOP --
running = True
while running:
    # screen.fill((255, 0, 45))

    # eventt loop to detect game eventts
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # detect user pressing keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocityX -= velocity
            if event.key == pygame.K_RIGHT:
                player_velocityX += velocity
        else:
            player_velocityX = 0
            player_velocityY = 0

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                if touchingGround == True:
                    player_velocityY = -200

    # display sky
    screen.blit(sky_surf, (0, 0))

    # display ground
    screen.blit(ground.surf, (ground.rect.x, ground.rect.y))

    # check if player is touching the ground
    collideTest = ground.rect.colliderect(player.rect)
    if collideTest == False:
        touchingGround = False
        player_velocityY += gravity
    elif collideTest:
        touchingGround = True
        player_velocityY = 0

    # move and display player
    player.rect.y += player_velocityY
    player.rect.x += player_velocityX
    screen.blit(player.surf, (player.rect.x, player.rect.y))

    pygame.display.update()