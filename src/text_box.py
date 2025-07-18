from src.const import *
import pygame
import os

class Text_box:

    def __init__(self, pos_x, pos_y, width=100, height=100, text_color=COLOR_WHITE, font="./assets/fonts/Cascadia.ttf", font_size=50, max_length=8):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.text_color = text_color
        self.active = True
        self.input = ""

        # Check if the font is a file or a default system font
        if os.path.isfile(font):
            self.font = pygame.font.Font(font, font_size)
        else:
            self.font = pygame.font.SysFont(font, font_size)
        self.max_length = max_length

    def draw(self, surface):
        """
        Draws the text box and the current input text.
        """
        # Draw the text box border
        pygame.draw.rect(surface, COLOR_WHITE if self.active else COLOR_LIGHT_GRAY, self.rect, 4 if self.active else 1)

        # Render the input text
        text_surface = self.font.render(self.input, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event) -> str:
        """
        Handles events for the text box, including mouse clicks and keyboard input.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the text box was clicked
            if self.rect.collidepoint(event.pos):
                self.active = True  # Activate the text box
            else:
                self.active = False  # Deactivate the text box

        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Remove the last character from the input
                self.input = self.input[:-1]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # If enter key is pressed return the string
                return self.input
            elif event.key in [pygame.K_ESCAPE, pygame.K_INSERT, pygame.K_DELETE, pygame.K_HOME,
                                pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN, pygame.K_PRINT,
                                  pygame.K_CAPSLOCK, pygame.K_NUMLOCK, pygame.K_SCROLLLOCK,
                                    pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4,
                                      pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8,
                                        pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12]:
                # esc and other characters are not valid
                pass
            else:
                if len(self.input) >= self.max_length:
                    # Text can only be max_length characters long
                    pass
                else:
                    # Add the typed character to the input (all the letters, numbers, etc.)
                    self.input += event.unicode
        return None
    
    def clear(self) -> None:
        self.input = ""