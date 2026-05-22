from ClassObject import HEIGHT, WHITE, WIDTH, GameObject, BROWN, RED
import pygame

class animal(GameObject):
    def __init__(self, x, y, animal_type="chicken"):
        super().__init__(x, y, 40, 40, WHITE)
        self.type = animal_type
        self.speed = 1
        self.direction = [1, 1]
        self.hunger = 0

    def moverandom(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.direction[0] *= -1
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.direction[1] *= -1

    def draw(self, surface):
        if self.type == "chicken":

            pygame.draw.rect(
                surface,
                (255, 255, 200),
                (self.x, self.y, self.width, self.height))
            pygame.draw.circle(
                surface,
                RED,
                (int(self.x + self.width - 5), int(self.y + 5)),
                3)
        else:
            pygame.draw.rect(
                surface,
                BROWN,
                (self.x, self.y, self.width, self.height))