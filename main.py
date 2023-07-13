import pygame

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

WINDOW_BACKGROUND = (0,0,0)
WINDOW_TEXT = (255,255,255)
PLAYER1 = (255,100,100)
PLAYER2 = (100,100,255)
TILE_BACKGROUND = (200,200,200)
TILE_TEXT = (0,0,0)
FPS = 60
CLOCK = pygame.time.Clock()

pygame.display.set_caption("Think Ahead")

def set_configuration():
    WINDOW.fill(WINDOW_BACKGROUND)

def handle_events():
    playGame = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
    return playGame

def update_screen():
    pygame.display.update()
        
def main():
    set_configuration()

    run = True
    while run:
        CLOCK.tick(FPS)
        run = handle_events()
        update_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
