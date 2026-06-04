from ClassObject import WIDTH, HEIGHT, RED, GameObject
from abc import ABC, abstractmethod
import pygame

class Inventory:
    def __init__(self):
        self.items = {}  
    
    def addItem(self, item, amount=1):
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount
    
    def removeItem(self, item, amount=1):
        if item in self.items:
            self.items[item] -= amount
            if self.items[item] <= 0:
                del self.items[item]
    
    def hasItem(self, item):
        return item in self.items

class PlayerParent(GameObject, ABC):
    def __init__(self, x, y, name: str, energy: int = 100):
        super().__init__(x, y, 50, 50, RED)
        self.name = name
        self._energy = energy
        self._money = 100
        self.speed = 5
        self._inventory = Inventory()
        self._inventory.addItem("corn_seed", 3)  
        self._inventory.addItem("watering_can", 1)

    def getName(self) -> str:
        return self.name
    
    def setName(self, name: str):
        self.name = name

    @property
    def money(self):
        return self._money
    
    @property
    def energy(self):
        return self._energy

    @property
    def inventory(self):
        return self._inventory

    @energy.setter
    def energy(self, value):
        if value < 0:
            self._energy = 0
        else:
            self._energy = value
    
    @money.setter
    def money(self, value):
        if value < 0:
         self._money = 0
        else:
          self._money = value

    def move(self, keys):
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT] : #or keys[pygame.K_w]:
            dx = -self.speed
            self.direction = "left"
        if keys[pygame.K_RIGHT] : # or keys[pygame.K_a]:
            dx = self.speed
            self.direction = "right"
        if keys[pygame.K_UP] : # or keys[pygame.K_s]:
            dy = -self.speed
            self.direction = "up"
        if keys[pygame.K_DOWN] : # or keys[pygame.K_d]:
            dy = self.speed
            self.direction = "down"

        self.is_moving = (dx != 0 or dy != 0)


        if 0 <= self.x + dx <= WIDTH - self.width:
            self.x += dx
        if 0 <= self.y + dy <= HEIGHT - self.height:
            self.y += dy

    def waterPlant(self, plant):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} watered the plant.")
    
    def buyItem(self, item, price):
        if self._money >= price:
            self._money -= price
            self._inventory.addItem(item)
            print(f"{self.name} bought {item}.")
            return True
        
        print("not enough money")
        return False

class PlayerSteve(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Steve", 1000)
        self.FavoriteSeed = "corn_seed"



        self.direction = "down"

        # Load idle spritesheet
        self.idle_spritesheet = pygame.image.load("AssetPNG/Character/Steve/Idle.png").convert_alpha()
        print("Idle size:", self.idle_spritesheet.get_size())  # lihat ukuran aslinya
        self.idle_frames = []

        self.walk_spritesheet = pygame.image.load("AssetPNG/Character/Steve/Walk.png").convert_alpha()
        self.frame_width = 32
        self.frame_height = 48

        #walk
        self.walk_down = []
        self.walk_up = []
        self.walk_right = []
        self.walk_left = []

        #idle
        self.idle_down = []
        self.idle_up = []
        self.idle_right = []
        self.idle_left = []


        for i in range(4):
           frame = self.idle_spritesheet.subsurface((i * 32, 0, 32, 32))
           frame = pygame.transform.scale(frame, (50, 50))
           self.idle_frames.append(frame) 

           down = self.idle_spritesheet.subsurface((i * 32, 0, 32, 32))
           up = self.idle_spritesheet.subsurface((i * 32, 32, 32, 32))
           right = self.idle_spritesheet.subsurface((i * 32, 64, 32, 32))

           down = pygame.transform.scale(down, (50, 50))
           up = pygame.transform.scale(up, (50, 50))
           right = pygame.transform.scale(right, (50, 50))

           left = pygame.transform.flip(right, True, False)

           self.idle_down.append(down)
           self.idle_up.append(up)
           self.idle_right.append(right)
           self.idle_left.append(left)

        for i in range(4):
           
           down = self.walk_spritesheet.subsurface((i * 32, 0, 32, 32))
           up = self.walk_spritesheet.subsurface((i * 32, 32, 32, 32))
           right = self.walk_spritesheet.subsurface((i * 32, 64, 32, 32))

           down = pygame.transform.scale(down, (50, 50))
           up = pygame.transform.scale(up, (50, 50))
           right = pygame.transform.scale(right, (50, 50))

           left = pygame.transform.flip(right, True, False)

           self.walk_down.append(down)
           self.walk_up.append(up)
           self.walk_right.append(right)
           self.walk_left.append(left)
          
        self.idle_frame = 0
        self.walk_frame = 0
        self.animation_timer = 0
        self.animation_speed = 8  # makin kecil makin cepat
        self.is_moving = False

    def plantseed(self, seed_obj):
       """Tanam seed (seed_obj adalah object Seed seperti CornSeed, dll)"""
       seed_name = seed_obj.seedName
       if self._inventory.hasItem(seed_name):
        self._inventory.removeItem(seed_name)
        self._energy -= 10
        if self.FavoriteSeed == seed_name:
            print(f"{self.name} planted {self.FavoriteSeed} with extra care!")
        else:
            print(f"{self.name} planted {seed_name}.")
        return seed_obj.planted()
       else:
        print(f" No {seed_name} in inventory!")
        return None
       
    def draw(self, surface):

        if self.direction == "down":
            frame = self.walk_down[self.walk_frame]

        elif self.direction == "up":
            frame = self.walk_up[self.walk_frame]

        elif self.direction == "right":
            frame = self.walk_right[self.walk_frame]

        elif self.direction == "left":
            frame = self.walk_left[self.walk_frame]

        self.animation_timer += 1

        if self.animation_timer >= self.animation_speed:
           self.animation_timer = 0

           if self.is_moving:
              self.walk_frame = (self.walk_frame + 1) % len(self.walk_down)
           else:
              self.idle_frame = (self.idle_frame + 1) % len(self.idle_frames)

        if self.is_moving:
          surface.blit(frame, (self.x, self.y))
        else:
          if self.direction == "down":
             idle_frame = self.idle_down[self.idle_frame]

          elif self.direction == "up":
               idle_frame = self.idle_up[self.idle_frame]

          elif self.direction == "right":
               idle_frame = self.idle_right[self.idle_frame]

          else:
              idle_frame = self.idle_left[self.idle_frame]

          surface.blit(idle_frame, (self.x, self.y))


class PlayerLuna(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Luna", 100)
        self.FavoriteSeed = "Tomato"

        self.direction = "down"

        self.spritesheet = pygame.image.load(
            "AssetPNG/Character/Luna/Luna.png"
        ).convert_alpha()

        self.frame_width = 32
        self.frame_height = 32

        # WALK
        self.walk_down = []
        self.walk_up = []
        self.walk_right = []
        self.walk_left = []

        # IDLE
        self.idle_down = []
        self.idle_up = []
        self.idle_right = []
        self.idle_left = []

        for i in range(4):

            down = self.spritesheet.subsurface((i * 32, 0, 32, 32))
            up = self.spritesheet.subsurface((i * 32, 32, 32, 32))
            right = self.spritesheet.subsurface((i * 32, 64, 32, 32))

            down = pygame.transform.scale(down, (50, 50))
            up = pygame.transform.scale(up, (50, 50))
            right = pygame.transform.scale(right, (50, 50))

            left = pygame.transform.flip(right, True, False)

            self.walk_down.append(down)
            self.walk_up.append(up)
            self.walk_right.append(right)
            self.walk_left.append(left)

        for i in range(4):

            down = self.spritesheet.subsurface((i * 32, 96, 32, 32))
            up = self.spritesheet.subsurface((i * 32, 128, 32, 32))
            right = self.spritesheet.subsurface((i * 32, 160, 32, 32))

            down = pygame.transform.scale(down, (50, 50))
            up = pygame.transform.scale(up, (50, 50))
            right = pygame.transform.scale(right, (50, 50))

            left = pygame.transform.flip(right, True, False)

            self.idle_down.append(down)
            self.idle_up.append(up)
            self.idle_right.append(right)
            self.idle_left.append(left)

        self.idle_frame = 0
        self.walk_frame = 0
        self.animation_timer = 0
        self.animation_speed = 8
        self.is_moving = False

    def plantseed(self, seed_obj):
        seed_name = seed_obj.seedName

        if self._inventory.hasItem(seed_name):
            self._inventory.removeItem(seed_name)
            self._energy -= 10

            if self.FavoriteSeed == seed_name:
                print(f"{self.name} planted {self.FavoriteSeed} with extra care!")
            else:
                print(f"{self.name} planted {seed_name}.")

            return seed_obj.planted()

        else:
            print(f"No {seed_name} in inventory!")
            return None

    def draw(self, surface):

        if self.direction == "down":
            frame = self.walk_down[self.walk_frame]

        elif self.direction == "up":
            frame = self.walk_up[self.walk_frame]

        elif self.direction == "right":
            frame = self.walk_right[self.walk_frame]

        elif self.direction == "left":
            frame = self.walk_left[self.walk_frame]

        self.animation_timer += 1

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0

            if self.is_moving:
                self.walk_frame = (self.walk_frame + 1) % len(self.walk_down)
            else:
                self.idle_frame = (self.idle_frame + 1) % len(self.idle_down)

        if self.is_moving:

            surface.blit(frame, (self.x, self.y))

        else:

            if self.direction == "down":
                idle_frame = self.idle_down[self.idle_frame]

            elif self.direction == "up":
                idle_frame = self.idle_up[self.idle_frame]

            elif self.direction == "right":
                idle_frame = self.idle_right[self.idle_frame]

            else:
                idle_frame = self.idle_left[self.idle_frame]

            surface.blit(idle_frame, (self.x, self.y))