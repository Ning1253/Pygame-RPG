# The main file, containing the display and the main loop of the game.
import pygame, get_inputs

def loop(running, clock, display, FPS, all_sprites):# Main Loop
    while running:
        clock.tick(FPS) # Wait for next frame time
        inputs.grab_inputs() # Get User Inputs
        for event in inputs.inputs:
            if event.type == pygame.QUIT: # If the window is closed...
                pygame.quit() # ...Close the Window
    
        # Update all sprites
        all_sprites.update()

        # Display Refreshing
        display.fill([0, 0, 0]) # Empty Screen
        all_sprites.draw(display) # Render Sprites
    
        pygame.display.flip() # Show next frame
