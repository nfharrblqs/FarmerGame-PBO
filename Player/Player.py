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
        super().__init__(x, y, "Steve", 100)
        self.FavoriteSeed = "corn_seed"

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
       
class PlayerLuna(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Luna", 100)
        self.FavoriteSeed = "Tomato"

    def plantseed(self, seed)-> str:
        if seed in self.inventory.items:
            self.inventory.removeItem(seed)
            self.energy -= 10
            if self.FavoriteSeed == seed.seed_name:
                print(f"{self.name} planted {self.FavoriteSeed} with extra care because it's her favorite!")
            else:
                print(f"{self.name} planted {seed.seed_name}.")
        else : 
            return "Seed not found in inventory."
