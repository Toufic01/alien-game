import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect attribute:
        self.image = pygame.image.load('./resources/images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top lest of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)

