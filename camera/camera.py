import pygame
from ClassObject import WIDTH, HEIGHT
from pygame.math import Vector2

class CameraYSort(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = Vector2()

    def camera_draw(self, player):
        offset_x = self.screen.get_width() // 2 - player.rect.centerx
        offset_y = self.screen.get_height() // 2 - player.rect.centery

        self.offset = Vector2(offset_x, offset_y)
        
        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            self.screen.blit(sprite.image, sprite.rect.topleft + self.offset)