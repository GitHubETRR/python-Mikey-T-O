# Example file showing a circle moving on screen
import pygame
import random

###
###

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
strg=''
strg2=''
hexrite=''
ye=False
colr = (255, 255, 255)
clrite = (255, 255, 255)
correct=True
listy = ['#', 'X', 'X', 'X', 'X', 'X', 'X']
dig1 = '0'
dig2 = '0'
dig3 = '0'
dig4 = '0'
dig5 = '0'
dig6 = '0'
cpdig1 = 16
cpdig2 = 16
cpdig3 = 16
cpdig4 = 16
cpdig5 = 16
cpdig6 = 16

font = pygame.font.Font('freesansbold.ttf', 150)

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
					5: '5', 6: '6', 7: '7', 
					8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
					13: 'D', 14: 'E', 15: 'F'} 

def decToHex(dec):
    hexa = ''
    while(dec>0):
        reminder = dec%16
        hexa = conversion_table[reminder] + hexa
        dec = dec // 16
    rmlen = 2 - len(hexa)
    for i in range(rmlen):
        hexa = '0' + hexa
    return hexa


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))
    if correct:
        rdred = random.randint(0, 255)
        rdgreen = random.randint(0, 255)
        rdblue = random.randint(0, 255)
        clrite = (rdred, rdgreen, rdblue)
        tester = decToHex(rdred) + decToHex(rdgreen) + decToHex(rdblue)
        tsdig1=int(tester[:1], 16)
        tsdig2=int(tester[1:2], 16)
        tsdig3=int(tester[2:3], 16)
        tsdig4=tester[3:]
        tsdig4=int(tsdig4[:1], 16)
        tsdig5=tester[4:]
        tsdig5=int(tsdig5[:1], 16)
        tsdig6=int(tester[5:], 16)
        hexrite = '#' + tester
        correct = False
    
    strg3=''.join(listy)
    strg2='#' + strg
    
    text2 = font.render(strg3, True, (255, 255, 255), (0, 0, 0))
    text = font.render(strg2, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (640, 360)
    textRect2 = text2.get_rect()
    textRect2.center = (640, 530)
    
    c1 = pygame.draw.circle(screen, (colr), (355, 150), 100)
    c2 = pygame.draw.circle(screen, (clrite), (925, 150), 100)
    
    current_time=pygame.time.get_ticks()

    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    keys = pygame.key.get_pressed()
    
    a = len(strg)
    
    if keys[pygame.K_a]:
        if not ye and a<6:
            strg=strg+'A'
            ye = True
    elif keys[pygame.K_b]:
        if not ye and a<6:
            strg=strg+'B'
            ye = True
    elif keys[pygame.K_c]:
        if not ye and a<6:
            strg=strg+'C'
            ye = True
    elif keys[pygame.K_d]:
        if not ye and a<6:
            strg=strg+'D'
            ye = True
    elif keys[pygame.K_e]:
        if not ye and a<6:
            strg=strg+'E'
            ye = True
    elif keys[pygame.K_f]:
        if not ye and a<6:
            strg=strg+'F'
            ye = True
    elif keys[pygame.K_0] or keys[pygame.K_KP0]:
        if not ye and a<6:
            strg=strg + '0'
            ye = True
    elif keys[pygame.K_1] or keys[pygame.K_KP1]:
        if not ye and a<6:
            strg=strg + '1'
            ye = True
    elif keys[pygame.K_2] or keys[pygame.K_KP2]:
        if not ye and a<6:
            strg=strg + '2'
            ye = True
    elif keys[pygame.K_3] or keys[pygame.K_KP3]:
        if not ye and a<6:
            strg=strg + '3' 
            ye = True
    elif keys[pygame.K_4] or keys[pygame.K_KP4]:
        if not ye and a<6:
            strg=strg + '4'
            ye = True
    elif keys[pygame.K_5] or keys[pygame.K_KP5]:
        if not ye and a<6:
            strg=strg + '5'
            ye = True
    elif keys[pygame.K_6] or keys[pygame.K_KP6]:
        if not ye and a<6:
            strg=strg + '6'
            ye = True
    elif keys[pygame.K_7] or keys[pygame.K_KP7]:
        if not ye and a<6:
            strg=strg + '7'
            ye = True
    elif keys[pygame.K_8] or keys[pygame.K_KP8]:
        if not ye and a<6:
            strg=strg + '8'
            ye = True
    elif keys[pygame.K_9] or keys[pygame.K_KP9]:
        if not ye and a<6:
            strg=strg + '9'
            ye = True
    elif keys[pygame.K_BACKSPACE]:
        if not ye:
            b=a-1
            strg=strg[:b]
            ye = True
    else:
        ye = False
    
    a = len(strg)
        
    if a==6:
        dig1=strg[:1]
        dig2=strg[1:2]
        dig3=strg[2:3]
        dig4=strg[3:]
        dig4=dig4[:1]
        dig5=strg[4:]
        dig5=dig5[:1]
        dig6=strg[5:]
        red = dig1 + dig2
        red = int(red,16)
        green = dig3 + dig4
        green = int(green,16)
        blue = dig5 + dig6
        blue = int(blue,16)
        colr=(red, green, blue)
        cpdig1 = int(dig1, 16)
        cpdig2 = int(dig2, 16)
        cpdig3 = int(dig3, 16)
        cpdig4 = int(dig4, 16)
        cpdig5 = int(dig5, 16)
        cpdig6 = int(dig6, 16)
        
    if a==6:
        if cpdig1 == tsdig1:
            listy[1]= dig1
        elif cpdig1 < tsdig1:
            listy[1]='+'
        elif cpdig1 > tsdig1:
            listy[1]='-'
        if cpdig2 == tsdig2:
            listy[2]= dig2
        elif cpdig2 < tsdig2:
            listy[2]=' +'
        elif cpdig2 > tsdig2:
            listy[2]=' -'
        if cpdig3 == tsdig3:
            listy[3]= dig3
        elif cpdig3 < tsdig3:
            listy[3]=' +'
        elif cpdig3 > tsdig3:
            listy[3]=' -'
        if cpdig4 == tsdig4:
            listy[4]= dig4
        elif cpdig4 < tsdig4:
            listy[4]=' +'
        elif cpdig4 > tsdig4:
            listy[4]=' -'
        if cpdig5 == tsdig5:
            listy[5]= dig5
        elif cpdig5 < tsdig5:
            listy[5]=' +'
        elif cpdig5 > tsdig5:
            listy[5]=' -'
        if cpdig6 == tsdig6:
            listy[6]= dig6
        elif cpdig6 < tsdig6:
            listy[6]=' +'
        elif cpdig6 > tsdig6:
            listy[6]=' -'
        
    if strg2 == hexrite:
        correct=True
        strg = ''
        listy = ['#', 'X', 'X', 'X', 'X', 'X', 'X']

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

