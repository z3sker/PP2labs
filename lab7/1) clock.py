import pygame
import datetime

pygame.init()

FPS = 60
WIDTH, HEIGHT = 1400, 950
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Mouse Chasy")

mickey_img = pygame.image.load("clear.png")
r_ruka = pygame.image.load("right.png")
l_ruka = pygame.image.load("left.png")

def mickey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #display.fill((255, 255, 255))
        mickey_rect = mickey_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        display.blit(mickey_img, mickey_rect)
        
        cur_time = datetime.datetime.now()
        mins = cur_time.minute
        secs = cur_time.second
        
        #levaya ruka
        r_angle = -6 * secs + 60
        rotated_right_hand = pygame.transform.rotate(r_ruka, r_angle)
        right_hand_rect = r_ruka.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        display.blit(rotated_right_hand, rotated_right_hand.get_rect(center=right_hand_rect.center))
        
        #pravaya ruka
        l_angle = -6 * (mins + secs/60) - 54
        rotated_left_hand = pygame.transform.rotate(l_ruka, l_angle)
        left_hand_rect = l_ruka.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        display.blit(rotated_left_hand, rotated_left_hand.get_rect(center=left_hand_rect.center))
        
        pygame.display.update()
        clock.tick(FPS)
        
mickey()