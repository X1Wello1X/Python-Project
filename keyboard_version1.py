import pygame
import time
import keyboard
import random
import keyboard as k
import pyautogui
       
pygame.display.init()
pygame.init()
weidth,height=800,600
screen=pygame.display.set_mode((weidth,height))
steps=60
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
gray=(211,211,211)
mousex=125
mousey=125
cover_m_x=110
cover_m_y=110
catx=365
caty=125
cover_c_x=350
cover_c_y=110
range_of_line_on_board=469
end_of_movement=20
bridge=pygame.image.load("greenbridge.jpg")
mouse=pygame.image.load("mouse502.png")
cat=pygame.image.load("redcat.jpg")
#MOVES
font=pygame.font.Font("freesansbold.ttf",32)
moves_scorex=500
moves_scorey=20
#gameover
font=pygame.font.Font("freesansbold.ttf",32)
gameover_scorex=500
gameover_scorey=70
#yowin
youwinx=500
youwiny=80

def moves_on_screen (x,y):
    smoves=font.render("Moves: " + str(end_of_movement),True,(122,0,0))
    screen.blit(smoves,(x,y))
def game_over(x,y):
    game_over123=font.render(  "gameover",True,(122,0,0))
    screen.blit(game_over123,(x,y))
    pygame.display.update()
    time.sleep(2)
def youwin (x,y):
    you_win123=font.render("YOU WIN!!",True,(green))  
    screen.blit(you_win123,(x,y))
    pygame.display.update()
    time.sleep(2)
   
        
def player ():
    pygame.draw.rect(screen,gray,(cover_m_x+60,cover_m_y,60,60))
    screen.blit(mouse,(mousex+60,mousey))
def enemy (catx,caty,cover_c_x,cover_c_y):
    pygame.draw.rect(screen,red,(cover_c_x,cover_c_y+60,60,60))
    screen.blit(cat,(catx,caty+60))
def bridgewin ():
    pygame.draw.rect(screen,green,(410,230,60,60))
    screen.blit(bridge,(410,230))

    #screen.blit(gameover_image,(0,0))     
def draw_board ():
    size=0
    #410
    pygame.draw.rect(screen,blue,(410,410,60,60))    
    #Blue
    for i in range(6):
        pygame.draw.rect(screen,blue,(50+size,50 ,100,100)) #upward row
        pygame.draw.rect(screen,blue,(50+size,410 ,60,60))#downward row
        pygame.draw.rect(screen,blue,(50,50+size,60,60))#column right
        pygame.draw.rect(screen,blue,(410,50+size,60,60)) #column left
        size+=60
    size=0
    downstairs=0
    #white
    for i in range (5):
        for i in range(5):

            pygame.draw.rect(screen,white,(110+size,110+downstairs ,60,60))
            size+=60
        downstairs+=60 
        size=0  
    size=0    
    #lines
    for i in range(7):
        pygame.draw.line(screen,black,(50,50+size),(range_of_line_on_board,50+size)) #row lines
        pygame.draw.line(screen,black,(50+size,50),(50+size,range_of_line_on_board))
        size+=60
#def check ():
    #if movement == end_of_movement:
        #print("GAME OVER")
        #pygame.quit()
        #exit()


def movementx12 (mousex,mousey): 
    global movingx
    movingx=60 
    global dice
    dice=random.randint(0,1)
    global random_mouse
    random_mouse=[movingx,-movingx]

def movementy12 (mousex,mousey): 
    global movingx
    movingx=60 
    global dice
    dice=random.randint(0,1)
    global random_mouse
    random_mouse=[movingx,-movingx]
def step_counter (end):
    print(end_of_movement)
    if end_of_movement==0:
        global outofmovement
        outofmovement=True


           
out=True    

def screen_color():
    screen.fill(black)
running=True
def touching_bridge():
    if (mousex==365) and mousey==245:
        global touching_bridge123
        touching_bridge123=True
losing=0
while running:
    
    outofmovement=False
    step_counter(end_of_movement)
    print(outofmovement)
    if outofmovement:
        print(outofmovement)
        game_over(gameover_scorex,gameover_scorey)
        pygame.quit()
        exit()

    touching_bridge123=False
    touching_bridge()
    if touching_bridge123:
        youwin(youwinx,youwiny)
        soundObj=pygame.mixer.Sound("crd.mp3")
        soundObj.play()
        time.sleep(9.5)
        soundObj.stop()
        pygame.quit()
        exit()
    if out==False:
        game_over(gameover_scorex,gameover_scorey)
        pygame.quit()
        exit()
    screen_color()
    draw_board()
    
    

    if  (mousex>=125+(60*3)) and 125+(60*2) >mousey>125  :
        time.sleep(1)
        game_over(gameover_scorex,gameover_scorey)
        pygame.quit()
        exit()
         #left,top,width,height
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if mousex==65:
                    mousex-=60
                    cover_m_x-=60
                    out=False
                elif mousex>=65: 
                    mousex-=60   
                    cover_m_x-=60
                    end_of_movement-=1

            if event.key==pygame.K_RIGHT:
                if mousex==305:
                    mousex+=60
                    cover_m_x+=60
                    out=False
                elif mousex<=305: 
                    mousex+=60   
                    cover_m_x+=60  
                    end_of_movement-=1 
            if event.key==pygame.K_UP:
                if mousey==125:
                    mousey-=60
                    cover_m_y-=60
                    out=False
                elif mousey>=125: 
                    mousey-=60   
                    cover_m_y-=60
                    end_of_movement-=1
            if event.key==pygame.K_DOWN:
                if mousey==365:
                    mousey+=60
                    cover_m_y+=60
                    out=False
                elif mousey<365: 
                    mousey+=60   
                    cover_m_y+=60    
                    end_of_movement-=1        
                    
                #if golden_dice==2:
                    #movementy12(mousex,mousey)
                    #mousey+=random_mouse[dice] 
        if event.type==pygame.KEYUP:
            mousex+=0
            mousey+=0            
        

                  
    moves_on_screen(moves_scorex,moves_scorey)     
    player()
    enemy(catx,caty,cover_c_x,cover_c_y)
    bridgewin() 
    pygame.display.update()    





