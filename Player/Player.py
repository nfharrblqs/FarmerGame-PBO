from ClassObject import GREEN, HEIGHT, RED, WIDTH, YELLOW, GameObject
from abc import ABC, abstractmethod
import pygame
from Seed.Seed import Seed
class Inventory:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def moveItem(self, item):
        pass

class PlayerParent(GameObject, ABC):
    def __init__(self, x, y, name: str, energy: int = 100):
        super().__init__(x, y, 50, 50, RED)
        self.name = name
        self.energy = energy
        self.money = 100
        self.speed = 5
        self.inventory = Inventory()

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

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
        if self.money >= price:
            self.money -= price
            self.inventory.addItem(item)
            print(f"{self.name} bought {item}.")
        else:
            print(f"{self.name} does not have enough money to buy {item}.")

class PlayerSteve(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Steve", 100)
        self.FavoriteSeed = "corn"

    def plantseed(self, seed)-> str:
        if seed in self.inventory.items:
            self.inventory.removeItem(seed)
            self.energy -= 10
            if self.FavoriteSeed == seed.seed_name:
                print(f"{self.name} planted {self.FavoriteSeed} with extra care because it's his favorite!")
            else:
                print(f"{self.name} planted {seed.seed_name}.")
        else: 
            return "Seed not found in inventory."


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
