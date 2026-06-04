import pygame
import sys
from ClassObject import GREEN, WHITE, WIDTH, HEIGHT, COLOR
from Player.Player import PlayerSteve, PlayerLuna
from Seed.Seed import CornSeed, CarrotSeed, TomatoSeed, BeansSeed, CabbageSeed, GrapeSeed
from Commerce_System.Shop import Shop
from Decoration.Decor import Decoration, Scarecrow
from Animal.Animal import animal
from UI.InventoryMenu import InventoryMenu
from camera.camera import CameraYSort

class Game:
    def __init__(self, char_name="Steve"):
        pygame.mixer.init()
        if char_name == "Steve":
            self.player = PlayerSteve(WIDTH // 2, HEIGHT // 2)
        elif char_name == "Luna":
            self.player = PlayerLuna(WIDTH // 2, HEIGHT // 2)
        self.shop = Shop(WIDTH - 80, 50)
        self.plants = []
        self.animals = []
        self.decors = []
        self.font = pygame.font.Font(None, 36)
        self.held_item = None

        self.background = None
        self.load_background("Assetpng/tanah.png")
        
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

        self.decors.append(Scarecrow(100, 100))
        self.decors.append(Scarecrow(650, 450))

        self.animals.append(animal(200, 300, "chicken"))

        self.camera = CameraYSort()
        self.camera.add(self.player, *self.animals, *self.decors)
        self.camera.camera_draw(self.player)

    def load_background(self, image_path):
        """Load bg full screen"""
        try:
            bg_image = pygame.image.load(image_path).convert()
            self.background = pygame.image.load(image_path).convert()
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
            hewan.update_hunger(self.player.inventory, self.animals)
            hewan.produce_goods(self.player.inventory)
        
        keys = pygame.key.get_pressed()
        self.check_energy_and_sleep(keys)


    def draw(self, surface):  
        self.player.draw(surface)
        
        if self.background:
            surface.blit(
                self.background,
                (0, 0)
    )
        else:
            surface.fill((34, 139, 34))
        
        self.shop.draw(surface)
        for decor in self.decors:
            surface.blit(decor.image, self.camera.apply(decor.rect))
        for tanaman in self.plants:
            surface.blit(tanaman.image, self.camera.apply(tanaman.rect))
        for hewan in self.animals:
            surface.blit(hewan.image, self.camera.apply(hewan.rect))
            

        seed_count = sum(self.player._inventory.items.values())
        
        gold_text = self.font.render(f"Money: {self.player._money} gold", True, WHITE)
        seeds_text = self.font.render(f"Total Seeds: {seed_count}", True, WHITE)
        energy_text = self.font.render(f"Energy: {self.player._energy}", True, WHITE)

        surface.blit(gold_text, (10, 10))
        surface.blit(seeds_text, (10, 50))
        surface.blit(energy_text, (10, 90))

        inst_font = pygame.font.Font(None, 24)
        plant_text = inst_font.render("SPACE / I = Inventory | H = Harvest | B = Buy | C = Sell | ESC = Exit", True, WHITE)
        surface.blit(plant_text, (10, HEIGHT - 60))
        
        mouse_text = inst_font.render("Click item at the menu to use/plant/place", True, (0, 0, 0))
        surface.blit(mouse_text, (10, HEIGHT - 35))
        
        mouse_pos = pygame.mouse.get_pos()
        self.inventory_menu.draw(surface, self.player, mouse_pos)  

        if self.shop_open:
           self.draw_shop_menu(surface)
        
        if self.player.x < 100 and self.player.y < 100:
            bed_text = self.font.render("Press z to sleep.", True, WHITE)
            surface.blit(bed_text, (120, 20))

        if self.held_item:
            mouse_pos = pygame.mouse.get_pos()
            hold_font = pygame.font.Font(None, 20)
            hold_text = hold_font.render(f"Held: {self.held_item} (Click to use, right click to escape)", True, (255, 0, 0))
            surface.blit(hold_text, (mouse_pos[0] + 15, mouse_pos[1]+ 15))

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
                if action in ["plant", "place_animal"] and item_name:
                    if self.player.inventory.hasItem(item_name):
                        self.held_item = item_name
                        print(f"Held item: {self.held_item} (Click on field to use)")
                        self.inventory_menu.hide()
                    
    def handle_world_click(self, mouse_pos):
        """Mengeksekusi aksi klik di dunia (field) berdasarkan held_item"""

        if not self.held_item:
            return

        if "seed" in self.held_item:
            seed_classes = {
                "corn_seed": CornSeed,
                "carrot_seed": CarrotSeed,
                "tomato_seed": TomatoSeed,
                "beans_seed": BeansSeed,
                "cabbage_seed": CabbageSeed,
                "grape_seed": GrapeSeed
            }

            if not (200 <= mouse_pos[0] <= 600 and 200 <= mouse_pos[1] <= 500): #ganti sesuai bataas koordinat field tanaman
                print("You need to be in the field area to plant seeds! (come close to field and click seed in inventory)")
                return
        
        if self.held_item in seed_classes and self.player.inventory.hasItem(self.held_item):
            if self.player.energy >= 10:
                seed_class = seed_classes[self.held_item]
                new_seed = seed_class(mouse_pos[0], mouse_pos[1])

                self.player.inventory.removeItem(self.held_item)
                self.player.energy -= 10
                planted_plant = new_seed.planted()

                if planted_plant:
                    self.plants.append(planted_plant)
                    import Main
                    if hasattr(Main, 'planting_sound') and Main.planting_sound:
                        Main.planting_sound.play()
                    print(f"Planted {self.held_item} at {mouse_pos}!")
                    self.held_item = None
            else:
                print("Not enough energy to plant! (Energy must be at least 10)")
        elif self.held_item in ["chicken", "cow", "bull"]:
            if self.player.inventory.hasItem(self.held_item):
                self.player.inventory.removeItem(self.held_item)
                new_animal = animal(mouse_pos[0], mouse_pos[1], self.held_item)
                self.animals.append(new_animal)

                print(f"Placed {self.held_item} at {mouse_pos}!")
                self.held_item = None
                

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

        if not (200 <= self.player.x <= 600 and 200 <= self.player.y <= 500): #angka itu ganti sama koordinat field tanaman
            print("You need to be in the field area to plant seeds! (come close to field and click seed in inventory)")
            return
        
        if seed_name in seed_classes and self.player._inventory.hasItem(seed_name):
            seed_class = seed_classes[seed_name]
            new_seed = seed_class(self.player.x, self.player.y)
            planted_plant = self.player.plantseed(new_seed)
            if planted_plant:
                self.plants.append(planted_plant)
                print(f"Planting {seed_name}!")
                self.inventory_menu.hide()

    def place_animal_from_inventory(self, animal_name):
        if self.player._inventory.hasItem(animal_name):
            self.player.inventory.removeItem(animal_name)
            new_animal = animal(self.player.x, self.player.y, animal_name)
            self.animals.append(new_animal)
            print(f"Placing {animal_name}!")
            self.inventory_menu.hide()

    def handle_planting_with_menu(self, mouse_pos):
        """Handle planting via seed menu (kompatibilitas)"""
        self.handle_inventory_click(mouse_pos)
    
    def handle_harvest(self):
        for tanaman in self.plants[:]:
            if tanaman.get_rect().colliderect(self.player.get_rect()):
                hasil_panen = tanaman.abstractHarvest()
                if hasil_panen is not None:
                    self.player.inventory.addItem(hasil_panen)
                    self.plants.remove(tanaman)
                    print(f"Harvested {hasil_panen} and added to inventory!")
                else:
                    print("Plant not ready to harvest yet!")
                return
        print("No plant nearby to harvest!")

    def water_nearest_plant(self):
        for tanaman in self.plants:
            if tanaman.get_rect().colliderect(self.player.get_rect()):
                tanaman.waterPlant()
                print("Watered the plant!")
                return
        print("No plant nearby to water!")

    def feed_nearest_animal(self):
        """Mencari hewan terdekat dan memberinya makan"""
        for hewan in self.animals:
            if hewan.get_rect().colliderect(self.player.get_rect()):
                hewan.give_food(self.player.inventory)
                return
        print("No animal nearby to feed!")

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
          success = self.shop.buyFromPlayer(player=self.player, animal=nearest_animal, game_animals_list=self.animals)
          if success:
                print(f"Sold {nearest_animal.name}!!")
      else:
          print("No animal nearby you! (come close to animal and click J)")

    def draw_shop_menu(self, surface):
      menu_rect = pygame.Rect(200, 100, 400, 500)
      pygame.draw.rect(surface, (40, 40, 40), menu_rect)
      pygame.draw.rect(surface, (255,255,255), menu_rect, 3)

      font = pygame.font.Font(None, 28)

      items = [
            ("corn_seed", 50),
            ("carrot_seed", 40),
            ("tomato_seed", 50),
            ("beans_seed", 45),
            ("cabbage_seed", 55),
            ("grape_seed", 60),
            ("chicken", 200),
            ("cow", 500),
            ("bull", 800)
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
          surface.blit(text, (230, y+10))
          y += 48

    def handle_shop_click(self, mouse_pos):
        if not self.shop_open:
            return

        items = [
            ("corn_seed", 50),
            ("carrot_seed", 40),
            ("tomato_seed", 50),
            ("beans_seed", 45),
            ("cabbage_seed", 55),
            ("grape_seed", 60),
            ("chicken", 200),
            ("cow", 500),
            ("bull", 800)
        ]

        y= 150
        for item_name, price in items:
            item_rect = pygame.Rect(220, y, 350, 40)
            if item_rect.collidepoint(mouse_pos):
                success = self.shop.sellToPlayer(player=self.player, item_name=item_name)
                if success:
                    import Main
                    if hasattr(Main, 'buying_sound') and Main.buying_sound:
                        Main.buying_sound.play()
                break
            y += 50

    def check_energy_and_sleep(self, keys):
        if self.player.energy <= 0:
            self.player.speed=1
        else:
            self.player.speed=5

        if self.player.x < 100 and self.player.y < 100: #angka ganti sama koordint bed
            if keys[pygame.K_z]:
                self.player.energy = 100
                print("Sleeping... Energy restored to 100!")

                for tanaman in self.plants:
                    tanaman.isWatered = False

