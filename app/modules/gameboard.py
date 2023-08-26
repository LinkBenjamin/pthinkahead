import pygame 

from app.modules.gametile import Tile
from config.constants import *
from random import randint
from random import shuffle

class Gameboard:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.tiles = [[Tile((i*TILE_SIZE, j*TILE_SIZE),randint(-20, 20)) for j in range(GAME_COLS)] for i in range(GAME_ROWS)]

        self.tiles[0][0].set_cursor()
        self.cursor = (0,0)
        self.tiles[0][1] = Tile((0,TILE_SIZE),MYSTERY_BOX_CHARACTER)
        self.tiles[0][2] = Tile((0,2 * TILE_SIZE),MYSTERY_BOX_CHARACTER)
        self.tiles[0][3] = Tile((0,3 * TILE_SIZE),MYSTERY_BOX_CHARACTER)

        self.randomize()
        self.player_turn = True #Player 1's turn is True, Player 2's turn is False

    def set_turn(self, p1turn):
        self.player_turn = p1turn
        
    def draw(self):
        for i in range(GAME_ROWS):
            for j in range(GAME_COLS):
                if self.player_turn and i == self.cursor[0]:
                    self.tiles[i][j].highlight()
                elif not self.player_turn and j == self.cursor[1]:
                    self.tiles[i][j].highlight()
                else:
                    self.tiles[i][j].clear_highlight()
                
                self.tiles[i][j].draw()

    def randomize(self):
        one_list = []
        for i in range(GAME_ROWS):
            for j in range(GAME_COLS):
                one_list.append(self.tiles[i][j])
        
        self.tiles.clear()

        shuffle(one_list)

        self.tiles = [[0] * GAME_COLS for _ in range(GAME_ROWS)]

        item_index = 0
        for row in range(GAME_ROWS):
            for col in range(GAME_COLS):
                if item_index < len(one_list):
                    self.tiles[row][col] = one_list[item_index]
                    self.tiles[row][col].location = (row * TILE_SIZE, col * TILE_SIZE)
                    if self.tiles[row][col].is_cursor:
                        self.cursor = (row,col)
                    item_index += 1

