from ClassObject import GREEN, HEIGHT, RED, WIDTH, YELLOW, GameObject
import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, RED)
        self.speed = 5
        self.gold = 100
        self.punyabrpseed = 5

    def move(self, keys):
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        if 0 <= self.x + dx <= WIDTH - self.width:
            self.x += dx
        if 0 <= self.y + dy <= HEIGHT - self.height:
            self.y += dy

    def plantseed(self):
        if self.punyabrpseed > 0:
            self.punyabrpseed -= 1

            return seed(
                self.x + self.width // 2,
                self.y + self.height // 2
            )

        return None

class PlayerSteve(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5
        self.gold = 100
        self.punyabrpseed = 5

    def move(self, keys):
        x = 0
        y = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y = self.speed

        if 0 <= self.x + x <= WIDTH - self.width:
            self.x += x
        if 0 <= self.y + y <= HEIGHT - self.height:
            self.y += y

    def plantseed(self):
        return super().plantseed()
        