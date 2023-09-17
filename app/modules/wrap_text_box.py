import pygame

from config.files import get_full_path

class Wrap_textbox():
    def __init__(self, left, top, width, height, bgcolor = 'white', fgcolor = 'black', font_name = "TwilioSansMono-Regular.otf", font_size = 14):
        self.display_surface = pygame.display.get_surface()
        self.text = " "
        self.rect = pygame.Rect(left, top, width, height)
        self.font_name = font_name
        self.font_size = font_size
        
        self.set_font(font_name, font_size)

    def set_bg_color(self, color):
        self.bg_color = color
    
    def set_fg_color(self, color):
        self.fg_color = color

    def set_font(self, font, size):
        self.font = pygame.font.Font(get_full_path("static", font), size)

    def draw(self):
        text_surf = self.font.render(str(self.text), False, self.fg_color)
        text_rect = text_surf.get_rect(topleft = self.rect.topleft)

        pygame.draw.rect(self.display_surface, self.bg_color, self.rect)
        self.display_surface.blit(text_surf, text_rect)

