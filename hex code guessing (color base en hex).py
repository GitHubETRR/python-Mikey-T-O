# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
press_once = False
coord=[[160, 500], [480, 500], [800, 500], [1120, 500]]
on2=False
end_time_w = 0
end_time_r = 0
correct = True
litic = (255, 255, 255)

random.shuffle(coord)
coord1 = pygame.Vector2(coord[0][0], coord[0][1])
coord2 = pygame.Vector2(coord[1][0], coord[1][1])
coord3 = pygame.Vector2(coord[2][0], coord[2][1])
coord4 = pygame.Vector2(coord[3][0], coord[3][1])

dec=random.randint(1,200)
print(dec)
print (hex(dec)[2:].upper())
font = pygame.font.Font('freesansbold.ttf', 150)
text = font.render('Hola', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (640, 150)

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

right = (255, 255, 255)
no1 = (255, 0, 0)
no2 = (0, 255, 0)
no3 = (0, 0, 255)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))
    
    current_time=pygame.time.get_ticks()

    c1 = pygame.draw.circle(screen, right, coord1, 100)
    c2 =  pygame.draw.circle(screen, no1, coord2, 100)
    c3 = pygame.draw.circle(screen, no2, coord3, 100)
    c4 = pygame.draw.circle(screen, no3, coord4, 100)
    ticklight = pygame.draw.circle(screen, litic, (1100, 150), 30)
    screen.blit(text, textRect)

    keys = pygame.key.get_pressed()
    if correct:
        random.shuffle(coord)
        coord1 = pygame.Vector2(coord[0][0], coord[0][1])
        coord2 = pygame.Vector2(coord[1][0], coord[1][1])
        coord3 = pygame.Vector2(coord[2][0], coord[2][1])
        coord4 = pygame.Vector2(coord[3][0], coord[3][1])
        
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        right = (red, green, blue)
        no1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        no2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        no3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        strg = '#' + decToHex(red) + decToHex(green) + decToHex(blue)
            
        text = font.render(strg, True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (640, 150)
        
        correct = False

    else:
        press_once = False
    pos=pygame.mouse.get_pos()
    pressed1=pygame.mouse.get_pressed()[0]
    if pressed1:
        if not on2:
            if c4.collidepoint(pos) or c3.collidepoint(pos) or c2.collidepoint(pos):
                end_time_w=pygame.time.get_ticks()+1000
            else:
                if c1.collidepoint(pos): 
                    correct = True
                    end_time_r=pygame.time.get_ticks()+1000
        on2=True
    else: 
        on2=False
        
    if current_time < end_time_w:
        litic = (255, 0, 0)
    else:     
        if current_time < end_time_r:
            litic = (0, 255, 0)
        else:
            litic = (255, 255, 255)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

