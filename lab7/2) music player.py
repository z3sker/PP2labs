import pygame

pygame.init()
running = True

screen = pygame.display.set_mode((1200, 630))
img = pygame.image.load('bg.jpeg')
screen.blit(img, (0, 0))

clock = pygame.time.Clock()
FPS = 120

songs = ['lookatmenow.mp3', 'sweaterweather.mp3', 'million.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
playing = True
cur = 0

def next_song():
    global songs
    global cur
    cur += 1
    if cur == 3:
        cur = 0
    pygame.mixer.music.load(songs[cur])
    pygame.mixer.music.play()
    
def prev_song():
    global songs
    global cur
    cur -= 1
    if cur == -1:
        cur = 2
    pygame.mixer.music.load(songs[cur])
    pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    playing = False
                    pygame.mixer.music.pause()
                else:
                    playing = True
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
    
    pygame.display.flip()
    clock.tick(FPS)
                 
