import pygame
import sys
from ClassObject import GREEN, WHITE, WIDTH, HEIGHT, COLOR
from Player.Player import PlayerSteve
from Seed.Seed import CornSeed, CarrotSeed, TomatoSeed, BeansSeed, CabbageSeed, GrapeSeed
from Commerce_System.Shop import Shop
from Decoration.Decor import dekorasi
from Animal.Animal import animal
from UI.SeedMenu import SeedMenu

class Game:
    def __init__(self):
        self.player = PlayerSteve(WIDTH // 2, HEIGHT // 2)
        self.shop = Shop(WIDTH - 80, 50)
        self.plants = []
        self.animals = []
        self.decors = []
        self.font = pygame.font.Font(None, 36)

        self.background = None
        self.load_background("Assetpng/map.png") 
        
        menu_width = 400
        menu_height = 500
        self.seed_menu = SeedMenu(
            WIDTH // 2 - menu_width // 2,
            HEIGHT // 2 - menu_height // 2,
            menu_width,
            menu_height
        )

        self.decors.append(dekorasi(100, 100, "tree"))
        self.decors.append(dekorasi(650, 450, "tree"))
        self.decors.append(dekorasi(50, 500, "fence"))

        self.animals.append(animal(200, 300, "chicken"))

    def load_background(self, image_path):
        """Load gambar background full screen"""
        try:
            bg_image = pygame.image.load(image_path).convert()
            self.background = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
            print(f"Background loaded: {image_path}")
        except:
            print(f"Background not found: {image_path}")
            self.background = None

    def update(self):
        for tanaman in self.plants:
            tanaman.abstractGrow()
        for hewan in self.animals:
            hewan.moverandom()

    def draw(self, surface):

        if self.background:
            surface.blit(self.background, (0, 0))
        else:
            surface.fill((34, 139, 34))
        

        self.shop.draw(surface)
        for decor in self.decors:
            decor.draw(surface)
        for tanaman in self.plants:
            tanaman.draw(surface)
        for hewan in self.animals:
            hewan.draw(surface)
        self.player.draw(surface)

        seed_count = sum(self.player.inventory.items.values())
        
        gold_text = self.font.render(f"Gold: {self.player.gold}", True, WHITE)
        seeds_text = self.font.render(f"Total Seeds: {seed_count}", True, WHITE)
        energy_text = self.font.render(f"Energy: {self.player.energy}", True, WHITE)

        surface.blit(gold_text, (10, 10))
        surface.blit(seeds_text, (10, 50))
        surface.blit(energy_text, (10, 90))

        inst_font = pygame.font.Font(None, 24)
        plant_text = inst_font.render("SPACE = Buka Menu Tanam | H = Harvest | B = Buy | C = Sell | ESC = Exit", True, WHITE)
        surface.blit(plant_text, (10, HEIGHT - 60))
        
        mouse_text = inst_font.render("Klik seed di menu untuk menanam", True, (200, 200, 200))
        surface.blit(mouse_text, (10, HEIGHT - 35))
        
        mouse_pos = pygame.mouse.get_pos()
        self.seed_menu.draw(surface, self.player.inventory, mouse_pos)

    def handle_planting_with_menu(self, mouse_pos):
        """Handle planting via seed menu"""
        selected_seed = self.seed_menu.handle_click(mouse_pos)
        
        if selected_seed:
            seed_classes = {
                "corn_seed": CornSeed,
                "carrot_seed": CarrotSeed,
                "tomato_seed": TomatoSeed,
                "beans_seed": BeansSeed,
                "cabbage_seed": CabbageSeed,
                "grape_seed": GrapeSeed
            }
            
            if selected_seed in seed_classes:
                seed_class = seed_classes[selected_seed]
                new_seed = seed_class(self.player.x, self.player.y)
                planted_plant = self.player.plantseed(new_seed)
                if planted_plant:
                    self.plants.append(planted_plant)
                    print(f"Menanam {selected_seed}!")
            return True
        return False
    
    def open_seed_menu(self):
        """Buka menu pilih benih"""
        if self.seed_menu.show(self.player.inventory):
            print("Menu seed dibuka - Klik seed untuk menanam")
        else:
            print("Tidak ada benih untuk ditanam! Beli dulu dengan B")
    
    def handle_harvest(self):
        for tanaman in self.plants[:]:
            if tanaman.get_rect().colliderect(self.player.get_rect()):
                if tanaman.abstractHarvest():
                    gold_earned = {
                        "corn": 80,
                        "carrot": 60,
                        "tomato": 70,
                        "beans": 65,
                        "cabbage": 55,
                        "grape": 75
                    }.get(tanaman.plant_type, 50)
                    
                    self.player.gold += gold_earned
                    self.player.money = self.player.gold
                    self.plants.remove(tanaman)
                    print(f"Harvested {tanaman.plant_type} for {gold_earned} gold!")
                else:
                    print("Plant not ready to harvest yet!")
                return
        print("No plant nearby to harvest!")
