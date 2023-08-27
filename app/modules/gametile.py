import pygame
import random

from config.files import get_full_path
from config.constants import *

class Tile():
    def __init__(self, coordinates, face_value='?'):
        # Initializing a Tile requires you to provide its value.
        # If you don't, it will classify itself as a "Mystery Box"

        self.face_value = face_value
        self.active = True                                # Boolean, whether this space has been played yet or not
        self.coordinates = coordinates                    # Grid coordinate for the tile (ex 3,5)
        self.location = coordinates * TILE_SIZE           # Tuple, x and y pixel coordinates used to draw the square
        self.is_cursor = False
        self.is_highlighted = False
        
        # Drawing properties
        self.display_surface = pygame.display.get_surface()
        pygame.font.init()
        self.font = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), FONT_SIZE)

    # Returns the value of the space played.
    def play(self):
        self.active = False
        if '?' in str(self.face_value):
            # randomize a value between -20 and 20 to 'play' the mystery box
            rval = random.randint(GAME_MINIMUM_TILE_VALUE, GAME_MAXIMUM_TILE_VALUE)
        else:
            rval = int(self.face_value)

        self.set_cursor()
        return rval
    
    def set_cursor(self):
        self.face_value = '@'
        self.is_cursor = True
        self.active = False

    def set_blank(self):
        self.face_value = ' '
        self.active = False

    def highlight(self):
        self.is_highlighted = True

    def clear_highlight(self):
        self.is_highlighted = False

    def draw(self):
        self.tile_rect = pygame.Rect(self.location[0], self.location[1],TILE_SIZE,TILE_SIZE).inflate(-5,-5)
        value_surf = self.font.render(str(self.face_value), False, COLORS_TILE_TEXT)
        value_rect = value_surf.get_rect(center = self.tile_rect.center)

        if self.is_cursor:
            pygame.draw.rect(self.display_surface, COLORS_CURSOR,self.tile_rect)
        elif self.is_highlighted:
            pygame.draw.rect(self.display_surface, COLORS_TILE_HIGHLIGHT,self.tile_rect)
        else:
            pygame.draw.rect(self.display_surface, COLORS_TILE_BACKGROUND,self.tile_rect)
        self.display_surface.blit(value_surf, value_rect)
