import pygame
import time
import keyboard
import random
import keyboard as k
        
pygame.display.init()
weidth,height=800,600
screen=pygame.display.set_mode((weidth,height))
steps=60
move=[[weidth,0],[height*-1,0],[0,weidth*-1],[0,height]]
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
joe=None
cover_c_x=350
cover_c_y=110
range_of_line_on_board=469
movement=0
end_of_movement=20
bridge=pygame.image.load("greenbridge.jpg")
mouse=pygame.image.load("mouse502.png")
cat=pygame.image.load("redcat.jpg")
fbs=60
def player ():
    pygame.draw.rect(screen,gray,(cover_m_x+60,cover_m_y,60,60))
    screen.blit(mouse,(mousex+60,mousey))
def enemy (catx,caty,cover_c_x,cover_c_y):
    pygame.draw.rect(screen,red,(cover_c_x,cover_c_y+60,60,60))
    screen.blit(cat,(catx,caty+60))
def bridgewin ():
    pygame.draw.rect(screen,green,(410,230,60,60))
    screen.blit(bridge,(410,230)) 
def draw_board ():
    size=0
    #410
    pygame.draw.rect(screen,blue,(410,410,60,60))
    result=0
    #Blue
    for i in range(6):
        result=50+size
        pygame.draw.rect(screen,blue,(50+size,50 ,60,60)) #upward row
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
        

    
out=True    

def screen_color():
    screen.fill(black)
running=True

while running:
    #clock.tick(fbs)
    if out==False:
        print("GAME OVER")
        pygame.quit()
        exit()
    screen_color()
    draw_board()

    
         #left,top,width,height
    for event in pygame.event.get():
        print(event)
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

            if event.key==pygame.K_RIGHT:
                if mousex==305:
                    mousex+=60
                    cover_m_x+=60
                    out=False
                elif mousex<=305: 
                    mousex+=60   
                    cover_m_x+=60   
            if event.key==pygame.K_UP:
                if mousey==125:
                    mousey-=60
                    cover_m_y-=60
                    out=False
                elif mousey>=125: 
                    mousey-=60   
                    cover_m_y-=60
            if event.key==pygame.K_DOWN:
                if mousey==365:
                    mousey+=60
                    cover_m_y+=60
                    out=False
                elif mousey<365: 
                    mousey+=60   
                    cover_m_y+=60            
                    
                #if golden_dice==2:
                    #movementy12(mousex,mousey)
                    #mousey+=random_mouse[dice] 
        if event.type==pygame.KEYUP:
            mousex+=0
            mousey+=0            
        


                 
                
    player()
    enemy(catx,caty,cover_c_x,cover_c_y)
    bridgewin()    
    pygame.display.update()    





