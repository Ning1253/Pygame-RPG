# The main file, containing the display and the main loop of the game.
import pygame, get_inputs, current_rendered

def loop(running, clock, display, FPS):# Main Loop
    while running:
        clock.tick(FPS) # Wait for next frame time
        get_inputs.grab_inputs() # Get User Inputs
        for event in get_inputs.inputs:
            if event.type == pygame.QUIT: # If the window is closed...
                pygame.quit() # ...Close the Window
    
        # Update all sprites
        current_rendered.all_sprites.update()
        #try:
        current_rendered.current_room.update() # Update Room if has function
        #except:
        #    pass # If not, do nothing


        # Display Refreshing
        display.fill([0, 0, 0]) # Empty Screen
        current_rendered.all_sprites.draw(display) # Render Sprites
    
        pygame.display.flip() # Show next frame
