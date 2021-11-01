import pygame
import time
from pygame.locals import * # import KEYDOWN pygame.event


SIZE = 29 # block size

class Snake:
    def __init__(self, parent_screen, length): # start will begin here 
        self.length = length
         #  # load the image
        self.parent_screen = parent_screen
        self.block = pygame.image.load("blueB.png").convert()
        self.x = [SIZE] * length # giving array of block with size
        self.y = [SIZE] * length
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((92,25,84)) # add background to white color  // call this function, will update the screen to remove all blocks 
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) # draw block

        pygame.display.flip() # this function is to update the function above otherwise it wont work can also use with .update

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self): # snake walk on it own
        for i in range (self.length - 1, 0,-1):
            self.x[i] = self.x [i-1]
            self.y[i] = self.y [i-1]
        
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800)) #window size  # initilize a window or screen for display
        self.surface.fill((92,25,84)) # add background to white color  
        self.snake = Snake(self.surface,6) # window
        self.snake.draw() # draw the snake

    def run(self):
            # time.sleep(5) #window appear for 5 seconds
              # instead of time let stop the game when click on the escape.
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # this is for when you press escape key, this will close the window
                        running = False 
                    if event.key == K_UP:
                        self.snake.move_up()
                  
                    if event.key == K_DOWN:
                        self.snake.move_down()
                       
                    if event.key == K_LEFT:
                        self.snake.move_left()
                     
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                      
                elif event.type == QUIT: # quit when click on X
                    running = False
            
            self.snake.walk() # snake walk on its own without using any key
            time.sleep(0.3)


    


if __name__ == "__main__":

    game = Game()
    game.run()








