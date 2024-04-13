import pygame
import sys
from pygame.locals import * #для кнопок налево и направо
import random
import time

pygame.init()

FPS = 60
clock = pygame.time.Clock()

#палитра цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#перменные для счетчика, скорости и разрешение экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_COUNT = 0

#шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#экран
SCREEN = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")


#для встречных машиин и их передвижения
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


#гг машина и его передвижение
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


#рандом монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((30, 30))  # размер монеты
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)  #рандом позиция для икса
        self.rect.y = random.randint(-500, -30)  # рандом позиция для игрика


    def update(self):
        self.rect.y += SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 20)
            self.rect.y = random.randint(-500, -20)


#спрайты
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
enemies.add(E1)
all_sprites.add(E1)
 
#ускорение движения
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#монета промежуток
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 3000)  # каждые три секунды новая монета

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    SCREEN.blit(background, (0, 0))
    coin_count = font_small.render("Coins: " + str(COIN_COUNT), True, BLACK)  # кол-во собранных монет на экран
    SCREEN.blit(coin_count, (300, 10))

    for entity in all_sprites:
        if isinstance(entity, Player) or isinstance(entity, Enemy):
            entity.move()
        SCREEN.blit(entity.image, entity.rect)

    coins.update()

    # проверка получения монеты и звук
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_collisions:
        pygame.mixer.Sound('coin.wav').play()
        COIN_COUNT += 1
        coin.kill()
        all_sprites.remove(coin)

    # если столкнулся с другой машиной
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        SCREEN.fill(RED)
        SCREEN.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    clock.tick(FPS)
