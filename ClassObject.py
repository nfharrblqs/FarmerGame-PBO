import pygame
import sys

pygame.init()

WIDTH = 1040
HEIGHT = 800

BLACK = (0, 0, 0)
COLOR = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
