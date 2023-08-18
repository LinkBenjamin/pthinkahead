import pygame, sys
from app.modules.gametile import Tile
from app.modules.player import Player
from app.views.ui import UI
from app.modules.gameboard import Gameboard
from config.constants import *

class PThinkAhead():
    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.WINDOW.fill(COLORS_WINDOW_BACKGROUND)
        self.CLOCK = pygame.time.Clock()
        self.GAME_STATE = 'RUN'
        pygame.display.set_caption(GAME_TITLE)
    
        #self.new_game_screen = NewGameScreen()
        self.gameboard = Gameboard()
        self.player1 = Player("Ben")
        self.player2 = Player("Josh")
        self.ui = UI(self.player1, self.player2, self.gameboard)
    
    def run(self):
        while True:
            if 'RUN' in self.GAME_STATE:
                self.handle_events()
                self.update_screen()
                self.CLOCK.tick(FPS)
            elif 'QUIT' in self.GAME_STATE:
                pygame.quit()
                sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GAME_STATE = 'QUIT'

    def update_screen(self):
        self.ui.display()
        pygame.display.update()

if __name__ == "__main__":
    game = PThinkAhead()
    game.run()
