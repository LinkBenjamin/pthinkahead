import pygame 

from app.modules.gametile import Tile
from app.modules.player import Player
from app.modules.wrap_text_box import Wrap_textbox

from config.constants import *

from random import randint
from random import shuffle

from config.files import get_full_path

class Gameboard:
    def __init__(self, player_1_name, player_2_name):
        self.display_surface = pygame.display.get_surface()
        self.cursor = (0,0)      # This is the current location from which the game is being played.
        self.player_turn = True  # Player 1's turn is True, Player 2's turn is False
        self.game_over = False

        self.player1 = Player(player_1_name)  # Create a player for p1
        self.player2 = Player(player_2_name)  # Create a player for p2

        self.gamelog = Wrap_textbox(620, 200, 260, 380)
        self.gamelog.set_bg_color("gray")
        self.gamelog.set_fg_color("black")
        
        # Initialize the tile matrix.
        self.tiles = [[Tile((i, j),randint(-15, 15)) for j in range(GAME_COLS)] for i in range(GAME_ROWS)]
        # Eliminate the (0,0) entry and replace it with the cursor so that we have a starting point
        # I got 99 tiles but this ain't one ;)
        self.tiles[0][0].set_cursor()
        # We're adding 3 mystery boxes to the mix.  Replace some of the randomly-generated tiles with
        # new Mystery-box tiles
        self.tiles[0][1] = Tile((0,1))
        self.tiles[0][2] = Tile((0,2))
        self.tiles[0][3] = Tile((0,3))
        # Now that we've edited the starting cursor and the 3 mystery boxes, we need to shuffle 
        # the board so that they're distributed.
        self.randomize()
        
    def play(self, tile):
        # Only one type of action is considered "playing your turn":
        # Choosing a Tile.
        p = ' '
        if self.player_turn:
            p = self.player1
        else:
            p = self.player2

        # To "Play" a tile,
        # 1) change the current cursor's tile to blank/inactive
        self.tiles[self.cursor[0]][self.cursor[1]].set_blank()
        # 2) update the player's score with the value of the tile they chose
        score_value = tile.play()
        p.score(score_value)
        # 3) Add the move to the game log
        self.prepend_game_log(p.name + " > " + str(tile.coordinates) + " (" + str(score_value) + " pts)\n")
        # 4) change this tile to be the new cursor
        self.cursor = tile.coordinates
        # 5) change to the other player's turn
        self.player_turn = not self.player_turn

        self.game_over = self.check_game_over()

    def scramble(self):
        # Each player can only scramble once per game.  So before we do it, we have to check whether it's allowed.
        # The UI *should* prevent this from ever being called if they don't have one... but always double-check ;)
        p = ' '
        if self.player_turn:
            p = self.player1
        else:
            p = self.player2
        if p.has_scramble:
            p.scramble() # This removes the player's ability to scramble in the future
            self.randomize()
            self.prepend_game_log(p.name + " scrambles!\n")

        self.game_over = self.check_game_over()


    def draw(self):
        # if the game is over, just draw a big box with who won
        if self.game_over:
            self.draw_winner()
        else:

            # When you need to draw the game board, you're going to do the following:
            # 1) Display every tile
            #    A) If it's player 1's turn, highlight all the active tiles in the same column
            #    B) If it's player 2's turn, highlight all the active tiles in the same row
            # 2) Display Player 1's status box
            # 3) Display Player 2's status box
            # 4) Display the game log textbox

            for i in range(GAME_ROWS):
                for j in range(GAME_COLS):
                    if self.player_turn and self.tiles[i][j].active and i == self.cursor[0]:
                        self.tiles[i][j].highlight()
                    elif not self.player_turn and self.tiles[i][j].active and j == self.cursor[1]:
                        self.tiles[i][j].highlight()
                    else:
                        self.tiles[i][j].clear_highlight()
                    
                    self.tiles[i][j].draw()

            self.player1.display(1, self.player_turn, COLORS_PLAYER_1)
            self.player2.display(2, not self.player_turn, COLORS_PLAYER_2)

            self.gamelog.draw()

    def randomize(self):
        # Shuffling is a little involved.  We're using a list-of-lists to hold the tiles,
        # So the random lib's shuffle() can only rearrange on a single row and then rearrange the rows.
        # To allow for complete shuffling (any tile can end up anywhere), we have to push the whole shebang
        # into a single list, perform the shuffle, and then extract again to a list-of-lists.  
        one_list = []

        # Make a single-dimensional list.
        for i in range(GAME_ROWS):
            for j in range(GAME_COLS):
                one_list.append(self.tiles[i][j])
        
        self.tiles.clear()

        # Shuffle the single-dimensional list.
        shuffle(one_list)

        # Push the tiles back into the 2-d list.
        self.tiles = [[0] * GAME_COLS for _ in range(GAME_ROWS)]

        # That leaves us with a problem - each tile tracks its own location!
        # So now we have to update the location of every tile with its new place in the list.
        # We also have to re-identify the cursor because we shuffled it too.
        item_index = 0
        for row in range(GAME_ROWS):
            for col in range(GAME_COLS):
                if item_index < len(one_list):
                    self.tiles[row][col] = one_list[item_index]
                    self.tiles[row][col].coordinates = (row,col)
                    self.tiles[row][col].location = (row * TILE_SIZE, col * TILE_SIZE)
                    if self.tiles[row][col].is_cursor:
                        self.cursor = (row,col)
                    item_index += 1

    def check_game_over(self):
        # if the player is vertical (p1)
        if self.player_turn:
            for row in range(GAME_ROWS):
                if self.tiles[self.cursor[0]][row].active:
                    return False

        # if the player is horizontal (p2)
        else:
            for col in range(GAME_COLS):
                if self.tiles[col][self.cursor[1]].active:
                    return False

        return True
        
    def draw_winner(self):

        if self.player1.points > self.player2.points:
            winner = "No moves remain: " + self.player1.name + " wins!"
        elif self.player2.points > self.player1.points:
            winner = "No moves remain: " + self.player2.name + " wins!"
        else:
            winner = "No moves remain: It's a TIE!"
        rect = pygame.Rect(0, 0,SCREEN_WIDTH,SCREEN_HEIGHT).inflate(-50,-50)
        pygame.draw.rect(self.display_surface, 'black', rect)
        
        font = pygame.font.Font(get_full_path("static", "TwilioSansMono-Regular.otf"), FONT_SIZE)
        value_surf = font.render(winner, False, COLORS_CURSOR)
        value_rect = value_surf.get_rect(center = rect.center)

        self.display_surface.blit(value_surf, value_rect)
        

    def prepend_game_log(self, new_log):
        self.gamelog.text = new_log + self.gamelog.text