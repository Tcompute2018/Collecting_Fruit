import pygame
# import time
from pygame.locals import * # import KEYDOWN pygame.event

class Snake:
    def __init__(self, parent_screen):
         #  # load the image
        self.parent_screen = parent_screen
        self.block = pygame.image.load("blueB.png").convert()
        self.x = 100 # give the block initial location in the screen
        self.y = 100

    def draw(self):
        self.parent_screen.blit(self.block,(self.x,self.y)) # draw block



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500)) #window size  # initilize a window or screen for display
        self.surface.fill((92,25,84)) # add background to white color  
        self.snake = Snake(self.surface) # window
        self.snake.draw() # draw the snake
    def run(self):
        pass

def draw_block():
    surface.fill((92,25,84)) # add background to white color  // call this function, will update the screen to remove all blocks 
    surface.blit(block,(block_x,block_y)) # draw block
    pygame.display.flip() # this function is to update the function above otherwise it wont work can also use with .update



if __name__ == "__main__":

    game = Game()
    game.run()



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





