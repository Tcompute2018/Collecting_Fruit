import pygame
import time
from pygame.locals import * # import KEYDOWN pygame.event
import random





SIZE = 29 # block size

Screen_Color = (92,25,84)
class food:
    def __init__(self, parent_screen):
        self.ranImage = random.randint(0,3)       
        self.image = pygame.image.load("food.jpg").convert()
      
        self.parent_screen = parent_screen
        self.x = SIZE * 5
        self.y = SIZE * 5

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y)) # window
        pygame.display.flip()

    def location(self):

        self.x = random.randint(0,26) * SIZE
        self.y = random.randint(0,13) * SIZE # get random location for food 800 / 40 for x and 400 / 40 for y

class Snake:
    def __init__(self, parent_screen, length): # start will begin here 
        self.length = length
         #  # load the image
        self.parent_screen = parent_screen
        self.block = pygame.image.load("blueB.png").convert()
        self.x = [SIZE] * length # giving array of block with size
        self.y = [SIZE] * length
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        
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
        pygame.display.set_caption("Eating Food Game")

        pygame.mixer.init()
        self.backGroundMusic()
        self.surface = pygame.display.set_mode((800,600)) #window size  # initilize a window or screen for display
        self.surface.fill((92,25,84)) # add background to white color  
        self.snake = Snake(self.surface,2) # snake size will equal to one
        self.snake.draw() # draw the snake
        self.food = food(self.surface)
        self.food.draw()
    
    def colision(self, x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False    

    def wallCollision(self, x1,y1,x2,y2):
        if x1 < 0 or x1 > 800 or y1 > 600 or y1 < 0:
            return True

    
    def mySound(self, sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3") # import sound when eat a fruit
        pygame.mixer.Sound.play(sound)

    def backGroundMusic(self):
        pygame.mixer.music.load("MusicBackGround.mp3")
        pygame.mixer.music.play()

    def backGround(self):
        myBackGound = pygame.image.load("backGround.jpg")
        self.surface.blit(myBackGound,(0,0))
        

    def play(self):
        self.backGround()
        self.snake.walk() # snake walk on its own without using any key
        self.food.draw()
        self.score()
        pygame.display.flip()

        # when snake hit the food
        if self.colision(self.snake.x[0],self.snake.y[0], self.food.x, self.food.y): # there is a collision based on the initial contact

            self.mySound("eatSound") # name of the mp3 file
            self.snake.increase_length()
            self.food.location()

        # when snake hit itself
        for i in range(1, self.snake.length): # start with 1 because the head will never hit the 1 point
            if self.colision(self.snake.x[0],self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.mySound("GameOverSound") # name of the mp3 file
                self.snake.increase_length()
                raise "Game over"
                exit(0)
            if self.wallCollision(self.snake.x[0],self.snake.y[0], self.snake.x[i], self.snake.y[i]): 
                self.mySound("GameOverSound") # name of the mp3 file
                self.snake.increase_length()
                raise "Game over"
                exit(0)

    def score(self):
        myText = pygame.font.SysFont('arial',25)
        
        myScore = myText.render(f"Point: {self.snake.length - 2}", True, (37, 36, 35))
        self.surface.blit(myScore,(700,10))

    def gameOver(self):
        self.backGround()
        myText = pygame.font.SysFont('arial',25)
        GameScore = myText.render(f"Game Over! Your final Score: {self.snake.length - 3}", True, (37, 36, 35) )
        self.surface.blit(GameScore, (300,200))
        ConMessage = myText.render(f"Press Enter if want to play again", True, (37, 36, 35) )
        self.surface.blit(ConMessage, (300,250))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface,2) # snake size will have two blocks
        self.food = food(self.surface)

    def run(self):
            # time.sleep(5) #window appear for 5 seconds
            # instead of time let stop the game when click on the escape.
        running = True
        stop = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # this is for when you press escape key, this will close the window
                        running = False 

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        stop = False   

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
                    
            try:
                if not stop:
                    self.play() # play the game
            except Exception as e: # call exception if the collision happen or return false
                self.gameOver()
                stop = True
                self.reset()

            time.sleep(0.2)


if __name__ == "__main__":

    game = Game()
    game.run()








