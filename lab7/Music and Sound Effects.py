import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
running = True
clock = pygame.time.Clock()

pygame.mixer.music.load('lookatmenow.mp3')
pygame.mixer.music.play(0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                 
    pygame.display.flip()
    clock.tick(60*5)
