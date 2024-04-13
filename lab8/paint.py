import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(colorBLACK)
base_layer = pygame.Surface((WIDTH, HEIGHT))

done = False

LMBpressed = False
RMBpressed = False

prevX = 0
prevY = 0

currX = 0
currY = 0

shape = None
colors = (colorBLACK, colorBLUE, colorGREEN, colorRED, colorYELLOW)
color = colors[0]
color_number = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    radius = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return int(radius)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #ЛКМ
                LMBpressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
                if shape == 'rectangle':
                    pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), 2)
                elif shape == 'circle':
                    pygame.draw.circle(screen, color, (prevX, prevY), calculate_circle(prevX, prevY, currX, currY), 2)

            elif event.button == 3:  #ПКМ
                RMBpressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  #ЛКМ
                LMBpressed = False
                
                if shape in ['rectangle', 'circle', 'eraser']:
                    base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_SPACE:
                color_number += 1
                if color_number > 4:
                    color_number -= 4
                color = colors[color_number]

    if LMBpressed and shape == 'eraser':
        pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), 20)  
        
    if shape == 'eraser':
        prevX, prevY = currX, currY

    if LMBpressed and shape != 'eraser':
        screen.blit(base_layer, (0, 0))
        if shape == 'rectangle':
            pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), 2)
        elif shape == 'circle':
            pygame.draw.circle(screen, color, (prevX, prevY), calculate_circle(prevX, prevY, currX, currY), 2)
        elif shape == 'eraser':
            pygame.draw.circle(screen, colorWHITE, (prevX, prevY), 10)
    
    

    pygame.display.flip()
