import pygame
import sys
import os
import random
import importlib

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 100

# Color Palette
GOLDEN_YELLOW = (255, 223, 0)
ELVEN_GREEN = (0, 128, 0)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load assets
title_screen = pygame.image.load(r'D:\Prototype\Assets\titlescreen1.png')
title_screen = pygame.transform.scale(title_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
wooden_table = pygame.image.load(r'D:\Prototype\Assets\1.png')  
wooden_table = pygame.transform.scale(wooden_table, (BUTTON_WIDTH, BUTTON_HEIGHT))

# Fonts and text
title_font = pygame.font.Font(None, 115)
title_font.set_bold(True)
button_font = pygame.font.Font(None, 55)

# Text rendering with shadow
def render_text_with_shadow(surface, text, position, font, text_color, shadow_color):
    x, y = position
    shadow_surface = font.render(text, True, shadow_color)
    text_surface = font.render(text, True, text_color)

    surface.blit(shadow_surface, (x+5, y+5))
    surface.blit(text_surface, (x, y))

def update_ui(module, *args, **kwargs):



# Main loop
    running = True
while running:
    screen.blit(title_screen, (0, 0))

    # Title with shadow
    render_text_with_shadow(screen, 'Days of High Adventure', (700, 100), title_font, GOLDEN_YELLOW, (0, 0, 0))

    # Company placeholder
    render_text_with_shadow(screen, 'Company Logo Here', (700, 250), title_font, GOLDEN_YELLOW, (0, 0, 0))

    # New Game Button
    new_game_rect = pygame.Rect(810, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
    screen.blit(wooden_table, (new_game_rect.x, new_game_rect.y))
    render_text_with_shadow(screen, 'New Game', (new_game_rect.x + 50, new_game_rect.y + 25), button_font, ELVEN_GREEN, (0, 0, 0))

    # Load Game Button
    load_game_rect = pygame.Rect(810, 550, BUTTON_WIDTH, BUTTON_HEIGHT)
    screen.blit(wooden_table, (load_game_rect.x, load_game_rect.y))
    render_text_with_shadow(screen, 'Load Game', (load_game_rect.x + 50, load_game_rect.y + 25), button_font, ELVEN_GREEN, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if new_game_rect.collidepoint(x, y):
                print("New Game clicked")
            if load_game_rect.collidepoint(x, y):
                print("Load Game clicked")

    pygame.display.flip()

pygame.quit()
sys.exit()
