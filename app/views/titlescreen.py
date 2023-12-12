import pygame
import pygame_gui
from pygame.rect import Rect
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu
from pygame_gui.elements.ui_label import UILabel
from config.files import get_full_path
from config.constants import *

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        #self.background = pygame.image.load(get_full_path("static", "TitleScreen.png"))
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Create labels for Player 1 & Player 2
        self.p1label = UILabel(relative_rect=Rect(50,200,150,30),text="Player 1:")
        self.p2label = UILabel(relative_rect=Rect(50,250,150,30),text="Player 2:")

        # Create text entry lines for player names
        self.player_1_name = UITextEntryLine(relative_rect=Rect(200, 200, 200, 30), manager=self.manager)
        self.player_2_name = UITextEntryLine(relative_rect=Rect(200, 250, 200, 30), manager=self.manager)

        self.clock = pygame.time.Clock()

    def handle_events(self):
        retval = "TITLE_SCREEN"
        time_delta = self.clock.tick(60) / 1000.0

        for event in pygame.event.get():
            # If the user presses q or ESC, we want to quit the game.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    retval = "QUIT"
                    break

            # Otherwise, we just want to wait until they've finished entering their text
            # We detect this as an enter key press.
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    retval = "SETUP"
            
            self.manager.process_events(event)

        self.manager.update(time_delta)

        # Redraw the screen after processing events
        self.render()

        return retval
    
    def get_player_info(self):
        return {
            'player1': {
                'name': self.player_1_name.get_text(),
                #'type': self.player_1_type_menu.get_single_selection()
            },
            'player2': {
                'name': self.player_2_name.get_text(),
                #'type': self.player_2_type_menu.get_single_selection()
            }
        }

    def render(self):
        # self.screen.blit(self.background, (0, 0))
        self.manager.draw_ui(self.screen)
        pygame.display.update()