import pygame
import random

from config.files import get_full_path
from config.constants import *

class Tile():
    def __init__(self, location, face_value='?'):
        # Initializing a Tile requires you to provide its value.
        # If you don't, it will classify itself as a "Mystery Box"
        self.face_value = face_value
        self.active = True          # Boolean, whether this space has been played yet or not
        self.location = location    # Tuple, x and y pixel coordinates used to draw the square
        
        # Drawing properties
        self.display_surface = pygame.display.get_surface()
        pygame.font.init()
        self.font = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), FONT_SIZE)

    # Returns the value of the space played.
    def play(self):
        self.active = False
        if '?' in self.face_value:
            # randomize a value between -20 and 20 to 'play' the mystery box
            rval = random.randint(GAME_MINIMUM_TILE_VALUE, GAME_MAXIMUM_TILE_VALUE)
        else:
            rval = int(self.face_value)

        return rval
    
    def draw(self):
        tile_rect = pygame.Rect(self.location[0], self.location[1],TILE_SIZE,TILE_SIZE).inflate(-5,-5)
        value_surf = self.font.render(str(self.face_value), False, COLORS_TILE_TEXT)
        value_rect = value_surf.get_rect(center = tile_rect.center)

        pygame.draw.rect(self.display_surface, COLORS_TILE_BACKGROUND,tile_rect)
        self.display_surface.blit(value_surf, value_rect)
