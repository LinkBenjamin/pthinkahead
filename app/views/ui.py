import pygame
import app.modules.gameboard

from config.constants import *

class UI:  # Controls the overall running of the game.
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def display(self):
        # The gameboard's components know how to draw themselves.
        # TODO: refactor those draw instructions out to here at some point in the future
        # so that concerns are properly separated
        self.gameboard.draw()

    def handle_events(self):
        pressed = pygame.mouse.get_pressed()
        button = ' '
        if pressed[0]:
            # Mouse was clicked
            location = pygame.mouse.get_pos()

            for i in range(GAME_ROWS):
                for j in range(GAME_COLS):
                    # if the mouse position is on a game tile
                    if self.gameboard.tiles[i][j].tile_rect.collidepoint(location):
                        # if that tile hasn't yet been played and is currently highlighted (valid move)
                        if self.gameboard.tiles[i][j].active and self.gameboard.tiles[i][j].is_highlighted:
                            self.gameboard.play(self.gameboard.tiles[i][j])

            # if it's player 1's turn and they click their "scramble" button, 
            # scramble the board (if allowed)
            if self.gameboard.player_turn and self.gameboard.player1.scramble_rect.collidepoint(location):
                self.gameboard.scramble()
            # if it's player 2's turn and they click their "scramble" button,
            # scramble the board (if allowed)
            if (not self.gameboard.player_turn) and self.gameboard.player2.scramble_rect.collidepoint(location):
                self.gameboard.scramble()