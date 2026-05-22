import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertanian (Harvest Game)")
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
            
class dekorasi(GameObject):
    def __init__(self, x, y, decor_type="tree"):
        super().__init__(x, y, 50, 50, GREEN)
        self.type = decor_type

    def draw(self, surface):
        if self.type == "tree":
            pygame.draw.rect(
                surface,
                BROWN,
                (
                    self.x + self.width // 3,
                    self.y + self.height // 2,
                    self.width // 3,
                    self.height // 2
                )
            )
            pygame.draw.circle(
                surface,
                GREEN,
                (
                    int(self.x + self.width // 2),
                    int(self.y + self.height // 3)
                ),
                20
            )
        elif self.type == "fence":

            pygame.draw.rect(
                surface,
                BROWN,
                (self.x, self.y, self.width, 10)
            )
            pygame.draw.rect(
                surface,
                BROWN,
                (
                    self.x,
                    self.y + self.height - 10,
                    self.width,
                    10
                )
            )

class Game:
    def __init__(self):

        #self.player = Player(WIDTH // 2, HEIGHT // 2)

        self.seeds = []
        self.animals = []
        self.decors = []

        self.font = pygame.font.Font(None, 36)

        self.decors.append(
            dekorasi(100, 100, "tree")
        )

        self.decors.append(
            dekorasi(650, 450, "tree")
        )

        self.decors.append(
            dekorasi(50, 500, "fence")
        )

        self.animals.append(
            animal(200, 300, "chicken")
        )

    def update(self):
        for tanaman in self.seeds:
            tanaman.grow()
        for hewan in self.animals:
            hewan.moverandom()

    def draw(self, surface):
        for decor in self.decors:
            decor.draw(surface)
        for tanaman in self.seeds:
            tanaman.draw(surface)
        for hewan in self.animals:
            hewan.draw(surface)
        self.player.draw(surface)

        gold_text = self.font.render(
            f"Gold: {self.player.gold}",
            True,
            WHITE
        )

        seeds_text = self.font.render(
            f"Seeds: {self.player.punyabrpseed}",
            True,
            WHITE
        )

        surface.blit(gold_text, (10, 10))
        surface.blit(seeds_text, (10, 50))

        inst_font = pygame.font.Font(None, 24)

        plant_text = inst_font.render(
            "SPACE = Plant | H = Harvest",
            True,
            WHITE
        )

        surface.blit(
            plant_text,
            (10, HEIGHT - 30)
        )

    def handle_planting(self):
        new_seed = self.player.plantseed()
        if new_seed:
            self.seeds.append(new_seed)

    def handle_harvest(self):
        for tanaman in self.seeds[:]:
            if tanaman.get_rect().colliderect(
                self.player.get_rect()
            ):

                gold_earned = tanaman.harvest()
                if gold_earned > 0:
                    self.player.gold += gold_earned
                    self.seeds.remove(tanaman)

def main():

    clock = pygame.time.Clock()
    game = Game()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.handle_planting()
                elif event.key == pygame.K_h:
                    game.handle_harvest()

        keys = pygame.key.get_pressed()
        game.player.move(keys)
        game.update()
        screen.fill(COLOR)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
