import pygame

class Ship():
    def __init__(self, screen):
        """intialize the ship image and get its rect"""
        self.screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = ship.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at its curremt location."""
        self.screen.blit(self.image, self.rect)