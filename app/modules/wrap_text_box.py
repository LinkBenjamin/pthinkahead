import pygame

from config.files import get_full_path

class Wrap_textbox():
    def __init__(self, left, top, width, height, bgcolor='white', fgcolor='black',
                 font_name="TwilioSansMono-Regular.otf", font_size=14):
        self.display_surface = pygame.display.get_surface()
        self.text = " "
        self.rect = pygame.Rect(left, top, width, height)
        self.font_name = font_name
        self.font_size = font_size
        self.line_height = None
        self.cached_wrapped_text = None  # Store wrapped text for caching

        self.set_font(font_name, font_size)

    def set_bg_color(self, color):
        self.bg_color = color

    def set_fg_color(self, color):
        self.fg_color = color

    def set_font(self, font, size):
        self.font = pygame.font.Font(get_full_path("static", font), size)
        self.line_height = self.font.get_linesize()
        self.cached_wrapped_text = None  # Reset cached text

    def draw(self):
        # Strip trailing newline characters before comparing
        text_without_newline = self.text.rstrip("\n")

        # Check if the text has changed (without newline characters)
        if text_without_newline != self.cached_wrapped_text:
            self.cached_wrapped_text = self.wrap_text(text_without_newline)  # Wrap and cache

        # Draw at the original position
        draw_rect = pygame.Rect(self.rect.topleft, self.rect.size)

        # Render and draw each line of text
        for line in self.cached_wrapped_text.splitlines():
            text_surf = self.font.render(line, False, self.fg_color)
            text_rect = text_surf.get_rect(topleft=draw_rect.topleft)
            pygame.draw.rect(self.display_surface, self.bg_color, draw_rect)
            self.display_surface.blit(text_surf, text_rect)
            draw_rect.move_ip(0, self.line_height)  # Move down for the next line

    def wrap_text(self, text):
        lines = []
        current_line = ""

        for char in text:
            if char == '\n':
                # If a newline character is encountered, start a new line
                lines.append(current_line)
                current_line = ""
            else:
                current_line += char

                # If the current line exceeds the specified width, start a new line
                if self.font.size(current_line)[0] > self.rect.width:
                    lines.append(current_line)
                    current_line = ""

        # Add the remaining content
        if current_line:
            lines.append(current_line)

        wrapped_text = '\n'.join(lines)
        return wrapped_text