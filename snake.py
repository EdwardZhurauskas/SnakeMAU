import pygame
import time
import random as r
from functools import lru_cache
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 136, 4)
purple = (119, 15, 121)
 
colors=[white, yellow, black, red, green, blue] 

level_number = 0

snake_block = 10
snake_speed = 1
base_speed = 1
 
dis_width = 800
dis_height = 800
dsw = 800
dsh = 800
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()

 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

walls=[[], [], [], []]

for x_walls in range(10): pass
 
 
def message(msg, color,pos_x, pos_y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [pos_x, pos_y])

 
def Your_score(score):
    value1 = score_font.render("Score: ", True, white)
    value2 = score_font.render("Score: " + str(score), True, green)
    dis.blit(value2, [0, 0])
    dis.blit(value1, [0, 0])
    
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        if snake_list.index(x)%2==0:
            pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])
 
 
@lru_cache() 
def main(level_number):
    global snake_speed
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    walls = [] 
    foodx = 200
    foody = 400
 
    while not game_over:
        '''Logic chapter of the game stage'''
        while game_close == True:
            if level_number == 3:
                dis.fill(blue)
                message("Victory!", white, dsw/3, dsh/3)
                message("R - play now", black, dsw/3, dsh/3 + 50)
                message("Q - quit", black, dsw/3, dsh/3 + 100)
                pygame.display.update()
            if level_number != 3:
                dis.fill(red)
                message("Game over!", black, dsw/6, dsh/3)
                message("R - restart", black, dsw/6, dsh/3 + 50)
                message("Q - quit", black, dsw/6, dsh/3 + 100)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        main(level_number)
        
        
        '''Chapter of keyboard events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: 
                if x1_change != snake_block and event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif x1_change != -snake_block and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif y1_change != snake_block and event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif y1_change != -snake_block and event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                if snake_speed == base_speed: snake_speed += 1
        
                                         
        
        '''This is 'Kiss the Wall' chapter of game logic'''
        if x1 >= dis_width:
            x1_change -= dis_width
            
        if x1 < 0:
            x1_change += dis_width
            
        if y1 >= dis_height:
            y1_change -= dis_height        
            
        if y1 < 0:
            y1_change += dis_height           
            
        x1 += x1_change
        y1 += y1_change
        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    our_snake(snake_block, snake_List)
        
        '''Render chapter'''
        
        dis.fill(black)
        if snake_speed ==base_speed  and len(snake_List) == 1:
            message("Press any button to start!", white, dsw/6 + 75, dsh/10)
            message("Collect 5 apples", red, dsw/6 + 75, dsh/10 + 50)
            message("Collect 5 ", green, dsw/6 + 75, dsh/10 + 50)
            message("Collect ", white, dsw/6 + 75, dsh/10 + 50)
        else: message("", white, dsw/6, dsh/3 + 100)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
    
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        '''Snake throwing with she's tale'''
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
        '''Drawing the level's walls'''
        if level_number == 1:
            pygame.draw.aalines(dis, green, False, [[175, 375], [375, 375], [375, 175]])
            pygame.draw.aalines(dis, green, False, [[425, 175], [425, 375], [650, 375]])
            pygame.draw.aalines(dis, green, False, [[175, 425], [375, 425], [375, 650]])
            pygame.draw.aalines(dis, green, False, [[425, 650], [425, 425], [650, 425]])
        if level_number == 2:
            pygame.draw.aalines(dis, orange, False, [[275, 375] ,[175, 375], [175, 175], [375, 175],[375, 275]])
            pygame.draw.aalines(dis, orange, False, [[425, 275], [425, 175], [625, 175], [625, 375], [525, 375]])
            pygame.draw.aalines(dis, orange, False, [[275, 425], [175, 425], [175, 625], [375, 625], [375, 525]])
            pygame.draw.aalines(dis, orange, False, [[425, 525], [425, 625], [625, 625], [625, 425], [525, 425]])
            
        if level_number == 3:
            pygame.draw.aalines(dis, yellow, False, [[325, 375], [375, 375], [375, 325]])
            pygame.draw.aalines(dis, yellow, False, [[425, 325], [425, 375], [475, 375]])
            pygame.draw.aalines(dis, yellow, False, [[325, 425], [375, 425], [375, 475]])
            pygame.draw.aalines(dis, yellow, False, [[425, 475], [425, 425], [475, 425]])
            pygame.draw.aalines(dis, purple, False, [[275, 375] ,[175, 375], [175, 175], [375, 175],[375, 275]])
            pygame.draw.aalines(dis, purple, False, [[425, 275], [425, 175], [625, 175], [625, 375], [525, 375]])
            pygame.draw.aalines(dis, purple, False, [[275, 425], [175, 425], [175, 625], [375, 625], [375, 525]])
            pygame.draw.aalines(dis, purple, False, [[425, 525], [425, 625], [625, 625], [625, 425], [525, 425]])
            
            
        
        pygame.display.update()
 
        '''Apple on a snake way'''
        if x1 == foodx and y1 == foody:
            if Length_of_snake == 5 and level_number != 3: main(level_number + 1)
            if Length_of_snake == 5 and level_number == 3:
                game_close = True
            foodx = round(r.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(r.randrange(50, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1            
            if snake_speed<=10:
                snake_speed += 1
            if snake_speed >10 and snake_speed<=15:
                snake_speed += 0.5
            if snake_speed >15:
                snake_speed += 0.25
 
        clock.tick(15)
 
    pygame.quit()
    quit()
 
 
main(1)