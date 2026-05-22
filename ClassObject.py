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
