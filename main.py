import pygame, sys
from app.modules.gametile import Tile
from app.modules.player import Player
from app.views.ui import UI
from app.views import titlescreen
from app.modules.gameboard import Gameboard
from config.constants import *

class PThinkAhead():
    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.WINDOW.fill(COLORS_WINDOW_BACKGROUND)
        self.CLOCK = pygame.time.Clock()
        self.GAME_STATE = 'TITLE'
        pygame.display.set_caption(GAME_TITLE)
        self.titlescreen = titlescreen.TitleScreen(screen=self.WINDOW)
        self.ui = ' '
        self.gameboard=' '
    def run(self):
        while True:
            if 'TITLE' in self.GAME_STATE:
                self.GAME_STATE = self.titlescreen.handle_events()
                self.titlescreen.render()
            if 'SETUP' in self.GAME_STATE:
                names = self.titlescreen.get_player_info()
                self.gameboard = Gameboard(names['player1']['name'], names['player2']['name'])
                self.ui = UI(self.gameboard)
                self.GAME_STATE = 'RUN'
            if 'RUN' in self.GAME_STATE:
                self.ui.handle_events()
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
