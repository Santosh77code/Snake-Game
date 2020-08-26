# THIS IS SNAKE GAME IN PYTHON BY SANTOSH KHATRI. Here I have coded simple snake game with pygame. 
#In this code ,There is code for custom background image & music That i have commented.  
#to use this code uncomment LINES 9 ,11,12,32,33,95,96,106,107,144 & comment line 143.
#***************************ENJOY***********************************
import pygame
import random
import os
#for playing background music plus background image
#pygame.mixer.init()
#background music
#pygame.mixer.music.load('background.mp3')
#pygame.mixer.music.play()
#for initializing pygame function
pygame.init()


#defining_color
white = (255,255,255)
black =(0,0,0)
red = (255,0,0)
green = (0,255,0)
#screen resolution(UI)
screen_width = 800
screen_height = 400


clock = pygame.time.Clock()

#Creating _Game_Window
game_window = pygame.display.set_mode((screen_width,screen_height))
#choosing background image
#background = pygame.image.load("bgimage1.jpg")
#background = pygame.transform.scale(background,(screen_width,screen_height)).convert_alpha()
#game title
pygame.display.set_caption("SNAKEGAMEWITHSANTOSH")
pygame.display.update()


#importing font from os to display text on UI
font = pygame.font.SysFont(None,40)
#function for printing texts on game window
def score_screen(text , color , x ,y):
    text_screen = font.render(text, True , color)
    game_window.blit(text_screen,[x,y])
#making snake
def plot_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:

     pygame.draw.rect(game_window,color,[x ,y, snake_size , snake_size])
#for displaying welcome window
def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((150,150,150))
        score_screen("Welcome To Snakes",red,220,150)
        score_screen("Press Enter to Play",black,220,200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop() 

        pygame.display.update()
        clock.tick(40)

#GAME_LOOP
def game_loop():
    #GAME_SPECIFIC_VARIABLE
    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 45
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    food_x =random.randint(30,screen_width/2)
    food_y =random.randint(30,screen_height/2)
    score = 0
    init_velocity = 5
    fps = 40
    #checking whether high score file exist or not
    if(not os.path.exists("High_Score.txt")):
        with open("High_Score.txt","w") as f:
            f.write("0")
#reading High_Score.txt for getting highscore
    with open("High_Score.txt","r") as f:
        HighScore = f.read()

    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            #pygame.mixer.music.load('gameover.mp3')
            #pygame.mixer.music.play()
            with open("High_Score.txt","w") as f:
                f.write(str(HighScore))
            game_window.fill(white)
            score_screen("Game Over ! Press enter to continue",red , 100 , 150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #pygame.mixer.music.load('background.mp3')
                        #pygame.mixer.music.play()
                        game_loop()

                
        else:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y =  -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0
                    
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) <10:
                score = score + 10
            
            #food positioning
                food_x =random.randint(30,screen_width/2)
                food_y =random.randint(30,screen_height/2)
            #increasing length of snake after eating food
                snake_length = snake_length + 5
            #Updating High score if secured
                if score > int(HighScore):
                    HighScore = score

            game_window.fill(red) 
            #game_window.blit(background,(0,0))
        #printing score & high score in game window
            score_screen("Score :" + str(score) + "    HighScore: "+ str(HighScore),black,5,5)
        #creating food 
            pygame.draw.rect(game_window,green,[food_x ,food_y, snake_size , snake_size])

        #deleting head  of snake after snake become long(as in condition)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
        #printing game over if head of snake and body collaps 
            if head in snake_list[:-1]:
                game_over = True
        #printing game over if snake touches game window
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height :
                game_over = True
            
        #creating snake    
            plot_snake(game_window,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()