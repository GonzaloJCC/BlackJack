import pygame
import os

class Button:

    def __init__(self, pos_x, pos_y, width=100, height=100, button_color=(255, 255, 255), text="Default", text_color=(0, 0, 0), font="./assets/fonts/Cascadia.ttf", font_size=60, sound=None, callback=None):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.button_color = button_color
        self.text = text
        self.text_color = text_color
        # If to check if the font is a default one or a file
        if os.path.isfile(font):
            self.font = pygame.font.Font(font, font_size)
        else:
            self.font = pygame.font.SysFont(font, font_size)

        self.callback = callback
        self.sound = pygame.mixer.Sound(sound) if sound else None
        self.callback = callback
        
    # Function to draw the button
    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    # What wil happen when the button is clicked
    def clicked(self, event):                   
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.sound:
                self.sound.play()
            if self.callback:
                self.callback()  # Execute the callback function
            return True
        return False
