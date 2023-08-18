import pygame

from config.constants import *

class UI:  # Controls the overall running of the game.
    def __init__(self, player1, player2, gameboard):
        self.player1 = player1
        self.player2 = player2
        self.gameboard = gameboard
        self.p1turn = True # This is how we'll control whose turn it is.  Every move will cause this to flip.

    def display(self):
        self.player1.display(1,self.p1turn,COLORS_PLAYER_1)
        self.player2.display(2,not self.p1turn, COLORS_PLAYER_2)
        # TODO: self.gameboard.display()

# When a player clicks a valid tile:
# - The move is written to the game log.
# - Score is updated.
# - The Current Tile cursor is deactivated.
# - The Selected Tile becomes the cursor.
# - We check the win condition - will the next player have any valid moves (tile or scramble)
# - Toggle p1turn
# - Highlight the row/column of valid moves (draw a box around them, half-transparent, overlaid on top)