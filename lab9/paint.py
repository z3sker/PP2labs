import pygame
import sys
import math

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

def draw_square(x1, y1, x2, y2):
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(min(x1, x2), min(y1, y2), side_length, side_length)
    pygame.draw.rect(screen, color, rect, 2)

def draw_right_triangle(x1, y1, x2, y2):
    pygame.draw.line(screen, color, (x1, y1), (x2, y1), 2)
    pygame.draw.line(screen, color, (x2, y1), (x2, y2), 2)
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

def draw_equilateral_triangle(x1, y1, x2, y2):
    side_length = abs(x2 - x1)
    height = side_length * math.sqrt(3) / 2
    top_x = (x1 + x2) // 2
    top_y = y1 - int(height)
    pygame.draw.line(screen, color, (x1, y1), (x2, y1), 2)
    pygame.draw.line(screen, color, (x1, y1), (top_x, top_y), 2)
    pygame.draw.line(screen, color, (x2, y1), (top_x, top_y), 2)

def draw_rhombus(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    half_width = abs(x2 - x1) // 2
    half_height = abs(y2 - y1) // 2
    pygame.draw.polygon(screen, color, [(center_x - half_width, center_y),
                                         (center_x, center_y - half_height),
                                         (center_x + half_width, center_y),
                                         (center_x, center_y + half_height)], 2)

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
                if shape in ['rectangle', 'circle', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_t:
                shape = 'right_triangle'
            elif event.key == pygame.K_e:
                shape = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                shape = 'rhombus'
            elif event.key == pygame.K_SPACE:
                color_number += 1
                if color_number > 4:
                    color_number -= 4
                color = colors[color_number]

    if LMBpressed: # and shape != 'eraser'
        screen.blit(base_layer, (0, 0))
        if shape == 'rectangle':
            draw_square(prevX, prevY, currX, currY)
        elif shape == 'circle':
            pygame.draw.circle(screen, color, (prevX, prevY), calculate_circle(prevX, prevY, currX, currY), 2)
        elif shape == 'right_triangle':
            draw_right_triangle(prevX, prevY, currX, currY)
        elif shape == 'equilateral_triangle':
            draw_equilateral_triangle(prevX, prevY, currX, currY)
        elif shape == 'rhombus':
            draw_rhombus(prevX, prevY, currX, currY)

    pygame.display.flip()
