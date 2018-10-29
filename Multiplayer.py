import pygame, random, sys

from pygame.locals import *

# Defines the death function
def mul_death(screen, player,color, loop):
    font = pygame.font.SysFont("Arial", 24) # Font for the message
    death_text = font.render(str(player)+" died!", True, color) # String that appears
    screen.blit(death_text,(100,100)) # Blits the message onto the screen
    pygame.display.update()
    loop = False # this is meant to stop the game loop
    pygame.time.wait(2000) # Wait 2 seconds
    pygame.display.quit()
    pygame.quit()

# The Victory Page, which blits the victory message then closes the window
def mul_win(screen, player,color):
    font = pygame.font.SysFont("Arial", 24) # Font for the message
    death_text = font.render(str(player)+" won!", True, color) # String that appears
    screen.blit(death_text,(100,100)) # Blits the message onto the screen
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.display.quit()
    pygame.quit()

# Defines the collision function
def collide(x1, x2, y1, y2, w1, w2, h1, h2): # Asks for 2 xy coordinate pairs, than the distance that needs to be checked
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2: # Logic that checks if the given coordinates are colliding
        return True
    else:
        return False

# Defines the first snake's position, where it spawns at first
snake_x = [350,350,350,350,350]
snake_y = [290,270,250,230,210]

# Defines the basic variables
direction = 0 # By default, down is 0
score = 0 # Score set to 0 at first


# Second snake and variables
snake_x2 = [210,210,210,210,210]
snake_y2 = [350,330,310,290,270]
direction_2 = 0
score_2 = 0

# Defines the basic size of each "square"
block_size = (20,20)

pygame.init()

# Lists out the few sounds that are in the game
pygame.mixer.init()
eat = pygame.mixer.Sound('eat.wav')
pop = pygame.mixer.Sound('pop.wav')

# Sets window size, background image, and caption
window = pygame.display.set_mode((800, 600))
background = pygame.image.load("grass.jpg")
pygame.display.set_caption('Snake')



# Defines both snake segments and food segments
snake_segment = pygame.Surface(block_size)
snake_segment.fill((255, 51, 0))
snake_segment2 = pygame.Surface(block_size)
snake_segment2.fill((66, 59, 217))

food = pygame.image.load("ant1.png")


# Defines font to be used in game (ie Score)
font = pygame.font.SysFont('Arial', 48)
font2 = pygame.font.SysFont('Arial', 24)

# Sets clock
clock = pygame.time.Clock()

# Boolean to set game loop
game_loop = False

# Defines randomized position for food
food_position = (random.randint(0,760),random.randint(0,570))

# The how to intro screen
howto_1 = "How to Play:"
howto_2 = "Arrow keys control the first snake."
howto_3 = "WASD controls the second snake."
howto_4 = "Collect 10 food to win!"
howto_5 = "Going through the other snake will result in shrinkage of your snake, as well as -1 score."
howto_6 = "press space to continue"
howtoloop = True

# Quick loop that stops when space bar is hit
while howtoloop:
    window.fill((255,255,255))
    h1 = font2.render(howto_1, True, (0, 0, 0))
    h2 = font2.render(howto_2, True, (0, 0, 0))
    h3 = font2.render(howto_3, True, (0, 0, 0))
    h4 = font2.render(howto_4, True, (0, 0, 0))
    h5 = font2.render(howto_5, True, (0, 0, 0))
    h6 = font2.render(howto_6, True, (0, 0, 0))
    window.blit(h1, (30, 20))
    window.blit(h2, (30, 50))
    window.blit(h3, (30, 80))
    window.blit(h4, (30, 110))
    window.blit(h5, (30, 140))
    window.blit(h6, (30,300))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                howtoloop = False
                game_loop = True

# Game loop itself
while game_loop:
    clock.tick(12) # Sets basic frame rate

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
            elif event.key == K_w and direction_2 != 0:
                direction_2 = 1
            elif event.key == K_s and direction_2 != 1:
                direction_2 = 0
            elif event.key == K_a and direction_2 != 3:
                direction_2 = 2
            elif event.key == K_d and direction_2 != 2:
                direction_2 = 3


    numbera = len(snake_x)
    numberb = len(snake_x2)

    # If the snake collides with another part of the snake, then subtract one from score and make it one block shorter
    for x in range(0, numberb-1):
        if collide(snake_x[0], snake_x2[x], snake_y[0], snake_y2[x], 20,20,20,20) and len(snake_x) >1:
            del snake_x[-1]
            score -= 1
            pop.play()
    # Same code, but for other snake
    for y in range(0, numbera-1):
        if collide(snake_x2[0], snake_x[y], snake_y2[0], snake_y[y], 20,20,20,20) and len(snake_x2) >1:
            del snake_x2[-1]
            score_2 -=1
            pop.play()
    numbera -= 1
    numberb -= 1

    # Defining a number for future use in ranges, as length of list - 1
    number = len(snake_x) - 1

    # Eating/Growing if statement, using collide again
    # Also randomly respawn after being eaten
    if collide(snake_x[0], food_position[0], snake_y[0], food_position[1], 20,20,20,20):
        score = score +1
        snake_x.append(20) # The actual number doesn't matter that much since its changed later on before the screen blits
        snake_y.append(20)
        eat.play() # Play the sound eat
        food_position = (random.randint(0, 790), random.randint(0, 590))
    if collide(snake_x2[0], food_position[0], snake_y2[0], food_position[1], 20,20,20,20):
        score_2 = score_2 +1
        snake_x2.append(20)
        snake_y2.append(20)
        eat.play()
        food_position = (random.randint(0, 790), random.randint(0, 590))

    # If the snake collides with the borders (-20 because of the block spawns), kill the snake
    if snake_x[0] < 0 or snake_x[0] > 780 or snake_y[0] < 0 or snake_y[0] > 580:
        mul_death(window, "Red Snake" ,(255,51,0), game_loop)

    if snake_x2[0] < 0 or snake_x2[0] > 780 or snake_y2[0] < 0 or snake_y2[0] > 580:
        mul_death(window,"Blue Snake",(66, 59, 217), game_loop)


    # Movement loop
    number1 = len(snake_x) - 1
    while number1 >= 1:
        snake_x[number1] = snake_x[number1 - 1]
        snake_y[number1] = snake_y[number1 - 1]
        number1 -= 1
    # Maintaining movement
    if direction == 0:
        snake_y[0] += 20
    elif direction == 1:
        snake_y[0] -= 20
    elif direction == 2:
        snake_x[0] -= 20
    elif direction == 3:
        snake_x[0] += 20

    #####################################################################################
    # This entire loop was made because of an error we kept running into, see reflection#
    #####################################################################################

    number1 = len(snake_x) - 1
    while number1 > 2:
        if collide(snake_x[0], snake_x[2], snake_y[0],snake_y[2], 20,20,20,20):
            if direction == 0:
                direction = 1
                snake_y[0] += 20
            elif direction == 1:
                direction = 0
                snake_y[0] -= 20
            elif direction == 3:
                direction = 2
                snake_x[0] -=20
            elif direction == 2:
                direction = 3
                snake_x[0] +=20

        elif collide(snake_x[0], snake_x[number1], snake_y[0], snake_y[number1], 20, 20, 20, 20):
            mul_death(window, "Red Snake (Suicide) ", (255, 51, 0), game_loop)

        number1 -= 1 # WAVE DASHING

    number2 = len(snake_x2) - 1
    while number2 > 2:
        if collide(snake_x2[0], snake_x2[1], snake_y2[0],snake_y2[1], 20,20,20,20):
            if direction_2 == 0:
                direction_2 = 1
                snake_y2[0] += 20
            elif direction_2 == 1:
                direction_2 = 0
                snake_y2[0] -= 20
            elif direction_2 == 3:
                direction_2 = 2
                snake_x2[0] -=20
            elif direction_2 == 2:
                direction_2 = 3
                snake_x2[0] +=20
        elif collide(snake_x2[0], snake_x2[number2], snake_y2[0], snake_y2[number2], 20, 20, 20, 20):
            mul_death(window, "Blue Snake (Suicide) ", (66, 59, 217),game_loop)

        number2 -= 1 # WAVE DASHING

    ##################
    # End error loop #
    ##################

    # movement loop for second snake
    number2 = len(snake_x2) - 1
    while number2 >= 1:
        snake_x2[number2] = snake_x2[number2 - 1]
        snake_y2[number2] = snake_y2[number2 - 1]
        number2 -= 1
    if direction_2 == 0:
        snake_y2[0] += 20
    elif direction_2 == 1:
        snake_y2[0] -= 20
    elif direction_2 == 2:
        snake_x2[0] -= 20
    elif direction_2 == 3:
        snake_x2[0] += 20

    # Declaring victory for either snake if they hit 10
    if score == 10:
        mul_win(window, "Red", (255, 51, 0))
    if score_2 == 10:
        mul_win(window, "Blue", (66, 59, 217))

    # Make background image the background
    window.blit(background, (0,0))

    # For each entry in the snake list, draw a block at those coordinates
    for block in range(0, len(snake_x)):
        window.blit(snake_segment, (snake_x[block], snake_y[block]))
    for block in range(0, len(snake_x2)):
        window.blit(snake_segment2, (snake_x2[block], snake_y2[block]))
    window.blit(food, food_position)

    # Blit the scores
    t = font.render(str(score), True, (255, 51, 0))
    t2 = font.render(str(score_2), True, (66, 59, 217))
    window.blit(t, (10, 10))
    window.blit(t2, (780,10))

    # Update the display
    pygame.display.update()
pygame.quit()
