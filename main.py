import pygame
# import time
from pygame.locals import * # import KEYDOWN pygame.event


def draw_block():
    surface.fill((92,25,84)) # add background to white color  // call this function, will update the screen to remove all blocks 
    surface.blit(block,(block_x,block_y)) # draw block
    pygame.display.flip() # this function is to update the function above otherwise it wont work can also use with .update



if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500)) #window size  # initilize a window or screen for display

    surface.fill((92,25,84)) # add background to white color  



    #  # load the image
    block = pygame.image.load("blueB.png").convert()
    block_x = 100 # give the block initial location in the screen
    block_y = 100
    surface.blit(block,(block_x,block_y)) # draw block



    pygame.display.flip() # this function is to update the function above

    

    # time.sleep(5) #window appear for 5 seconds
    # instead of time let stop the game when click on the escape.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # this is for when you press escape key, this will close the window
                    running = False 
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT: # quit when click on X
                running = False

    # draw blocks





