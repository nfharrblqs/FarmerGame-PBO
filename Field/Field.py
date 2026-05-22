import pygame
import sys
from ClassObject import GameObject, GREEN, WHITE, WIDTH, HEIGHT
from Player.Player import Player
from Seed.Seed import Seed
from Decoration.Decor import dekorasi
from Animal.Animal import animal

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