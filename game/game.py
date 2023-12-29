import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
GRAVITY = 0.5
JUMP_FORCE = 12

# Create the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

# Load images
player_img = pygame.image.load('player.png').convert_alpha()
background_img = pygame.image.load('background.jpg').convert()
ground_img = pygame.image.load('floor.png').convert()

# Resize images to match the window size if needed
player_img = pygame.transform.scale(player_img, (30, 30))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ground_img = pygame.transform.scale(ground_img, (WIDTH, 20))

# Player properties
player_rect = player_img.get_rect()
player_rect.x = 50
player_rect.y = HEIGHT - 80  # Adjust starting position
player_vel = pygame.Vector2(0, 0)
player_acc = pygame.Vector2(0, GRAVITY)
on_ground = False

# Ground properties
ground_rect = ground_img.get_rect()
ground_rect.x = 0
ground_rect.y = HEIGHT - 50  # Adjust ground height

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Move left and right
    if keys[pygame.K_LEFT]:
        player_vel.x = -5
    elif keys[pygame.K_RIGHT]:
        player_vel.x = 5
    else:
        player_vel.x = 0
    
    # Jumping
    if keys[pygame.K_SPACE] and on_ground:
        player_vel.y = -JUMP_FORCE
        on_ground = False
    
    # Apply gravity
    player_vel += player_acc
    player_rect.y += player_vel.y
    player_rect.x += player_vel.x  # Move the player horizontally
    
    # Check collision with ground
    if player_rect.colliderect(ground_rect):
        if player_vel.y > 0:
            player_rect.bottom = ground_rect.top
            player_vel.y = 0
            on_ground = True

    # Update screen
    win.blit(background_img, (0, 0))  # Draw the background first
    win.blit(ground_img, ground_rect)  # Draw the ground
    win.blit(player_img, player_rect)  # Draw the player
    pygame.display.flip()

pygame.quit()
sys.exit()
