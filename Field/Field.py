import pygame
import sys
from ClassObject import GREEN, WHITE, WIDTH, HEIGHT, COLOR
from Player.Player import PlayerSteve
from Seed.Seed import CornSeed, CarrotSeed, TomatoSeed, BeansSeed, CabbageSeed, GrapeSeed
from Commerce_System.Shop import Shop
from Decoration.Decor import Decoration
from Animal.Animal import animal
from UI.InventoryMenu import InventoryMenu

class Game:
    def __init__(self):
        pygame.mixer.init()
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
        
        self.inventory_menu = InventoryMenu(  
            WIDTH // 2 - menu_width // 2,
            HEIGHT // 2 - menu_height // 2,
            menu_width,
            menu_height
        )
        
        self.seed_menu = self.inventory_menu
        self.shop_open = False

        self.plantingSound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")
        self.buyingSound = pygame.mixer.Sound("PartialSound/SoundMethode/BuySell.mp3")

        self.animals.append(animal(200, 300, "chicken"))

    def load_background(self, image_path):
        """Load bg full screen"""
        try:
            bg_image = pygame.image.load(image_path).convert()
            self.background = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
            print(f"Background loaded: {image_path}")
        except:
            print(f"Background not found: {image_path}")
            self.background = None

    def toggle_shop(self):
        self.shop_open = not self.shop_open

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

        seed_count = sum(self.player._inventory.items.values())
        
        seeds_text = self.font.render(f"Total Seeds: {seed_count}", True, WHITE)
        energy_text = self.font.render(f"Energy: {self.player._energy}", True, WHITE)

        surface.blit(seeds_text, (10, 50))
        surface.blit(energy_text, (10, 90))

        inst_font = pygame.font.Font(None, 24)
        plant_text = inst_font.render("SPACE / I = Inventory | H = Harvest | B = Buy | C = Sell | ESC = Exit", True, WHITE)
        surface.blit(plant_text, (10, HEIGHT - 60))
        
        mouse_text = inst_font.render("click seed at the menu to plant", True, (0, 0, 0))
        surface.blit(mouse_text, (10, HEIGHT - 35))
        
        mouse_pos = pygame.mouse.get_pos()
        self.inventory_menu.draw(surface, self.player, mouse_pos)  

        if self.shop_open:
           self.draw_shop_menu(surface)

    def open_inventory(self):
        """Buka inventory menu"""
        self.inventory_menu.show()
    
    def open_seed_menu(self):
        """for open inventory"""
        self.open_inventory()
    
    def handle_inventory_click(self, mouse_pos):
        """Handle click in inventory menu"""
        if self.inventory_menu.visible:
            result = self.inventory_menu.handle_click(mouse_pos, self.player, self)
            if result:
                item_name, action = result
                if action == "plant" and item_name:
                    self.plant_from_inventory(item_name)
                    if action == "place_animal":
                        self.place_animal_from_inventory(item_name)

    def plant_from_inventory(self, seed_name):
        """Tplant from inventory"""
        seed_classes = {
            "corn_seed": CornSeed,
            "carrot_seed": CarrotSeed,
            "tomato_seed": TomatoSeed,
            "beans_seed": BeansSeed,
            "cabbage_seed": CabbageSeed,
            "grape_seed": GrapeSeed
        }
        
        if seed_name in seed_classes and self.player._inventory.hasItem(seed_name):
            seed_class = seed_classes[seed_name]
            new_seed = seed_class(self.player.x, self.player.y)
            planted_plant = self.player.plantseed(new_seed)
            if planted_plant:
                self.plants.append(planted_plant)
                print(f"Menanam {seed_name}!")
                self.inventory_menu.hide()

    def handle_planting_with_menu(self, mouse_pos):
        """Handle planting via seed menu (kompatibilitas)"""
        self.handle_inventory_click(mouse_pos)
    
    def handle_harvest(self):
        for tanaman in self.plants[:]:
            if tanaman.get_rect().colliderect(self.player.get_rect()):
                if tanaman.abstractHarvest():
                    money_earned = {
                        "corn": 80,
                        "carrot": 60,
                        "tomato": 70,
                        "beans": 65,
                        "cabbage": 55,
                        "grape": 75
                    }.get(tanaman._plant_type, 50)
                    
                    self.player._money += money_earned
                    self.plants.remove(tanaman)
                    print(f"Harvested {tanaman._plant_type} for {money_earned} money!")
                else:
                    print("Plant not ready to harvest yet!")
                return
        print("No plant nearby to harvest!")

    def sell_nearest_animal(self):
      """Sell animal naerby player"""
      nearest_animal = None
      min_distance = 100  
    
      for animal in self.animals:

        dx = animal.x - self.player.x
        dy = animal.y - self.player.y
        distance = (dx**2 + dy**2) ** 0.5
        
        if distance < min_distance:
            min_distance = distance
            nearest_animal = animal
    
      if nearest_animal:
          self.shop.sell_animal(self.player, nearest_animal, self)
          print(f"Animal sold!")
      else:
          print("No animal nearby you! (come close to animal and click J)")

    def draw_shop_menu(self, surface):

      menu_rect = pygame.Rect(200, 100, 400, 300)

      pygame.draw.rect(surface, (40, 40, 40), menu_rect)
      pygame.draw.rect(surface, (255,255,255), menu_rect, 3)

      font = pygame.font.Font(None, 36)

      items = [
          ("corn_seed", 50),
          ("carrot_seed", 40),
          ("tomato_seed", 50),
      ]

      y = 150

      for item, price in items:

          item_rect = pygame.Rect(220, y, 350, 40)

          pygame.draw.rect(surface, (80,80,80), item_rect)

          text = font.render(
              f"{item} - {price} price",
              True,
              (255,255,255)
          )

          surface.blit(text, (230, y+5))

          y += 50
