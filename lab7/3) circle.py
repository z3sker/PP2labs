import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 960))
running = True
clock = pygame.time.Clock()
FPS = 120
x = 640
y = 480

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20 if y > 30 else 0
        if pressed[pygame.K_DOWN]: y += 20 if y < 930 else 0
        if pressed[pygame.K_LEFT]: x -= 20 if x > 30 else 0
        if pressed[pygame.K_RIGHT]: x += 20 if x < 1250 else 0
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
        clock.tick(FPS)
        pygame.display.flip()