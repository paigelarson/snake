import pygame
from pygame import *
import random
pygame.init()

#colors 
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

#game window creation
window_width = 800
window_height = 600
size = 10
game_over = False

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

#snake variables
x1 = window_width / 2
y1 = window_height / 2
x1_change = 0
y1_change = 0

snake_List = []
Length_of_snake = 1

#food variables
foodx = round(random.randrange(0, window_width - size) /10 )*10
foody = round(random.randrange(0, window_height - size) /10)*10

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #snake movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = size
                x1_change = 0
                
    x1 += x1_change
    y1 += y1_change

    #background
    window.fill(blue)

    #snake creation/length change
    pygame.draw.rect(window, green, [foodx, foody, size, size])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True
            
    for x in snake_List:
        pygame.draw.rect(window, black, [x[0], x[1], size, size])

    #display score
    score_font = pygame.font.SysFont("calibri", 35)
    value = score_font.render("Your Score: " + str(Length_of_snake - 1),True, yellow)
    window.blit(value, [0, 0])

    #collision detection
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width - size) / 10.0) * 10.0
        foody = round(random.randrange(0, window_height - size) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(15)
    pygame.display.update()
    
pygame.quit()
quit()
 
