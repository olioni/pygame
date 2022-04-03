import pygame
import math

pygame.init()

screen = pygame.display.set_mode((900, 600))
w, h = pygame.display.get_surface().get_size()

pygame.display.set_caption("Olioni's Game")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, playerSize):
        super().__init__()
        self.surf = pygame.image.load('images/dwayne.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (playerSize, playerSize))
        self.rect = self.surf.get_rect(midbottom = (x, y))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.image.load('images/ground.png').convert_alpha()
        self.rect = self.surf.get_rect(midbottom = (x, y))

# random variables
ground_level = 300

# define background
sky_surf = pygame.image.load('images/sky.png')

# define ground
ground = Platform(250, ground_level)

# define player
player = Sprite(100, 300, 100)

# player variables
velocity = 1
player_velocityX = 0
player_velocityY = 0

player_x_pos = w / 2
player_y_pos = h / 2

# random variables
gravity = 1
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
            if event.key == pygame.K_UP:
                player_velocityY -= velocity
            if event.key == pygame.K_DOWN:
                player_velocityY += velocity
            if event.key == pygame.K_LEFT:
                player_velocityX -= velocity
            if event.key == pygame.K_RIGHT:
                player_velocityX += velocity
        else:
            player_velocityX = 0
            player_velocityY = 0

    

    # display sky
    screen.blit(sky_surf, (0, 0))

    # display ground
    screen.blit(ground.surf, (ground.rect.x, ground.rect.y))

    # move and display player
    player.rect.y += player_velocityY
    player.rect.x += player_velocityX
    screen.blit(player.surf, (player.rect.x, player.rect.y))

    # print(player_rect.bottom, ground_rect.top)

    collideTest = ground.rect.colliderect(player.rect)
    print(collideTest)

    pygame.display.update()