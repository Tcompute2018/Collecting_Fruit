import pygame
# import time
from pygame.locals import * # import KEYDOWN pygame.event

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500)) #window size  # initilize a window or screen for display

    surface.fill((92,25,84)) # add background to white color  
    pygame.display.flip() # this function is to update the function above

    # time.sleep(5) #window appear for 5 seconds
    # instead of time let stop the game when click on the escape.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif event.type == QUIT: # quit when click on X
                running = False
