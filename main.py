# The main file, containing the display and the main loop of the game.
import pygame

# Initialise
pygame.init()
running = True

# Main Settings
FPS = 60
screen_size = (480, 480)
clock = pygame.time.Clock()

# Display Setup
display = pygame.display.set_mode(screen_size)

# Main Groups Setup
all_sprites = pygame.sprite.Group()

# Main Loop
while running:
    clock.tick(FPS) # Wait for next frame time
    for event in pygame.event.get(): # Get User Inputs
        if event.type == pygame.QUIT: # If the window is closed...
            pygame.quit() # ...Close the Window
    
    # Display Refreshing
    display.fill([0, 0, 0]) # Empty Screen
    all_sprites.draw(display) # Render Sprites
    
    pygame.display.flip() # Show next frame