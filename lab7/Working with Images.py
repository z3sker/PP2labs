import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
running = True
clock = pygame.time.Clock()
img = pygame.image.load('bg.jpeg')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    screen.blit(img, (1, 1))
    
    pygame.display.flip()
    clock.tick(60*5)
