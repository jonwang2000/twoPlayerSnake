import pygame, random, sys
import Tkinter as tk
from Tkinter import *
from pygame.locals import *




# Defines the death function
def death(screen, score, loop):
    font = pygame.font.SysFont("Arial", 36) # Font for the message
    if score == 0:
        death_text = font.render("You didn't eat any food at all.",True,(255,255,255))
    elif score == range(1,15):
        death_text = font.render("You have died! Your score was: " + str(score) + ".", True, (255,255,255)) # String that appears
    else:
        death_text = font.render("Good job pal! Your score was: " + str(score) + ".", True, (255,255,255))
    screen.blit(death_text,(100,100))
    loop = False # Blits the message onto the screen
    pygame.display.update()

    highscore = open("Highscore.txt", "a")
    highscore.write(" "+str(score))
    highscore.close()

    pygame.time.wait(2000)
    pygame.quit()

# Defines the collision function
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2: # Logic that checks if the given coordinates are colliding
        return True
    else:
        return False

# Defines the original snake's position, where it spawns at first
snake_x = [350,350,350,350,350]
snake_y = [290,270,250,230,210]

# Defines the basic variables
direction = 0 # By default, down is 0
score = 0 # Score set to 0 at first

# Defines the basic size of each "square"
block_size = (20,20)


pygame.init()

# Window and images
window = pygame.display.set_mode((800, 600))
background = pygame.image.load("grass.jpg")
pygame.display.set_caption('Snake')

# Defines both snake segments and food segments
snake_segment = pygame.Surface(block_size)
snake_segment.fill((237,103,19)) # Snake is green
food = pygame.image.load("ant1.png")




# Defines font to be used in game (ie Score)
font = pygame.font.SysFont('Arial', 55)

# Sets clock
clock = pygame.time.Clock()

# Boolean to set game loop
game_loop = True

# Defines randomized position for food
food_position = (random.randint(0,603),random.randint(0,470))



while game_loop:
    clock.tick(17) # Sets basic frame rate

    for event in pygame.event.get():
        if event.type == QUIT: # If the program is told to quit
            sys.exit()
        elif event.type == KEYDOWN: # If the event is a keypress
            if event.key == K_UP and direction != 0: # If that keypress is up AND the snake is not currently going down
                direction = 1 # go UP
            elif event.key == K_DOWN and direction != 1: # Similar for everything else, cannot go opposite
                direction = 0
            elif event.key == K_LEFT and direction != 3:
                direction = 2
            elif event.key == K_RIGHT and direction != 2:
                direction = 3
    # defining a number for future use in ranges, as length of list - 1
    number = len(snake_x) - 1
    if collide(snake_x[0], food_position[0], snake_y[0], food_position[1], 20,20,20,20):
        score = score +1
        snake_x.append(20)
        snake_y.append(20)
        food_position = (random.randint(0, 790), random.randint(0, 590))
    if snake_x[0] < 0 or snake_x[0] > 780 or snake_y[0] < 0 or snake_y[0] > 580:
        death(window, score, game_loop)

    # Movement for snake
    number1 = len(snake_x) - 1
    while number1 >= 1:
        snake_x[number1] = snake_x[number1 - 1]
        snake_y[number1] = snake_y[number1 - 1]
        number1 -= 1
    if direction == 0:
        snake_y[0] += 20
    elif direction == 1:
        snake_y[0] -= 20
    elif direction == 2:
        snake_x[0] -= 20
    elif direction == 3:
        snake_x[0] += 20

    # Blitting all the resources
    window.blit(background, (0,0))
    for block in range(0, len(snake_x)):
        window.blit(snake_segment, (snake_x[block], snake_y[block]))
    window.blit(food, food_position)
    t = font.render(str(score), True, (255, 255, 255))
    window.blit(t, (10, 10))
    pygame.display.update()



pygame.quit()
