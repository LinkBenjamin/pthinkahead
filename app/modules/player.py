import pygame

from config.files import get_full_path
from config.constants import *

class Player():
    def __init__(self, player_name):
        self.name = player_name

         # Drawing properties
        self.display_surface = pygame.display.get_surface()
        pygame.font.init()
        self.font = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), FONT_SIZE)
        self.font_big = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), FONT_SIZE * 2)
        self.font_tiny = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), int(FONT_SIZE / 2))

        self.reset()

    def reset(self):
        self.score = 0
        self.has_scramble = True 
        
    def score(self, points):
        self.score += points

    def scramble(self):
        self.has_scramble = False

    def display(self, player_number, my_turn, color):
        # Figure out where this should go (whether it's player 1 or 2)
        if player_number == 1:
            location = (620,60)
            direction = '^' # Player 1 is always the vertical player
        else:
            location = (620,120)
            direction = '>' # Player 2 is always the horizontal player

        # Create the player display box
        player_rect = pygame.Rect(location[0], location[1],160,60)
        pygame.draw.rect(self.display_surface, color,player_rect)

        # - Shows my name
        # - Shows whether it's my turn or not (my_turn)
        if my_turn:
            name_surf = self.font.render(" * " + direction + str(self.name), False, COLORS_WINDOW_TEXT)
        else:
            name_surf = self.font.render("   " + direction + str(self.name), False, COLORS_WINDOW_TEXT)
        
        name_rect = name_surf.get_rect(top = player_rect.top + 8, left = player_rect.left + 8)
        self.display_surface.blit(name_surf, name_rect)

        # - Shows my score
        score_box = pygame.Rect(location[0]+100, location[1],TILE_SIZE,TILE_SIZE)
        score_text = self.font_big.render(str(self.score), False, COLORS_TILE_TEXT)
        score_rect = score_text.get_rect(center = score_box.center)
        pygame.draw.rect(self.display_surface, 'gray', score_box)
        self.display_surface.blit(score_text, score_rect)

        # - Shows whether I have a scramble left (has_scramble)
        if self.has_scramble and my_turn:
            scramble_button = pygame.Rect(location[0] + 10, location[1] + 30, 80, 30)
            scramble_text = self.font_tiny.render("Scramble", False, COLORS_TILE_TEXT)
            scramble_rect = scramble_text.get_rect(center = scramble_button.center).inflate(3,3)
            scramble_rect_ol = scramble_text.get_rect(center = scramble_button.center).inflate(8,8)
            pygame.draw.rect(self.display_surface, 'black', scramble_rect_ol)
            pygame.draw.rect(self.display_surface, 'gray', scramble_rect)
            self.display_surface.blit(scramble_text, scramble_rect)