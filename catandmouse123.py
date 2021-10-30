import pygame
pygame.display.init()
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
bridge=pygame.image.load("greenbridge.jpg")
mouse=pygame.image.load("mouse502.png")
cat=pygame.image.load("redcat.jpg")
def player (mousex,mousey,cover_m_x,cover_m_y):
    mousex=125
    mousey=125
    cover_m_x=110
    cover_m_y=110
    pygame.draw.rect(screen,gray,(cover_m_x+60,cover_m_y,60,60))
    screen.blit(mouse,(mousex+60,mousey))
def enemy (catx,caty,cover_c_x,cover_c_y):
    pygame.draw.rect(screen,red,(cover_c_x,cover_c_y,60,60))
    screen.blit(cat,(catx,caty))
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


def screen_color():
    screen.fill(black)

running=True

while running:
    screen_color()
    draw_board()
    player(mousex,mousey,cover_m_x,cover_m_y)
    enemy(catx,caty,cover_c_x,cover_c_y)
    bridgewin()
     #left,top,width,height
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()           