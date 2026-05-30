from ClassObject import WIDTH, HEIGHT, RED, GameObject
from abc import ABC, abstractmethod
import pygame

class Inventory:
    def __init__(self):
        self.__items = {}  
    
    def addItem(self, item, amount=1):
        if item in self.__items:
            self.__items[item] += amount
        else:
            self.__items[item] = amount
    
    def removeItem(self, item, amount=1):
        if item in self.__items:
            self.__items[item] -= amount
            if self.__items[item] <= 0:
                del self.__items[item]
    
    def hasItem(self, item):
        return item in self.__items
    
    def getItems(self):
        return self.__items

class PlayerParent(GameObject, ABC):
    def __init__(self, x, y, name: str, energy: int = 100):
        super().__init__(x, y, 50, 50, RED)
        self.name = name
        self.__energy = energy
        self.__money = 100
        self.speed = 5
        self.inventory = Inventory()
        self.inventory.addItem("corn_seed", 3) 

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getEnergy(self) -> int:
        return self.__self.energy
    
    def reduceEnergy(self, amount: int):
        """Mengurangi energi dengan aman dan  return True jika berhasil"""
        if self.__energy >= amount:
            self.__energy -= amount
            return True
        return False
    
    def getMoney(self) -> int:
        return self.__money

    def move(self, keys):
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP ] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        if 0 <= self.x + dx <= WIDTH - self.width:
            self.x += dx
        if 0 <= self.y + dy <= HEIGHT - self.height:
            self.y += dy

    def waterPlant(self, plant):
        if self.reduceEnergy(10):
            print(f"{self.name} watered the {plant.name}. Energy left: {self.__energy}")
        else:
            print(f"{self.name} is too tired to water the {plant.name}.")
    
    def buyItem(self, item, price):
        if self.__money >= price:
            self.__money -= price
            self.inventory.addItem(item)
            print(f"{self.name} bought {item}.")
        else:
            print(f"{self.name} does not have enough money to buy {item}.")
    
    @abstractmethod
    def plantSeed(self, seed_obj) -> str:
        pass

class PlayerSteve(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Steve", 100)
        self.__FavoritePlant = "corn_seed"

    def plantseed(self, seed_obj):
        """Tanam seed_obj (seed_obj adalah object Seed seperti CornSeed, dll)"""
        seed_name = seed_obj.seedName

        if self.inventory.hasItem(seed_name):
            if self.reduceEnergy(10):
                self.inventory.removeItem(seed_name)

                if self.__FavoritePlant == seed_name:
                    print(f"{self.name} planted {self.__FavoritePlant} with extra care because it's his favorite!")
                else:
                    print(f"{self.name} planted {seed_name}.")
                return seed_obj.planted()
            else:
                return "Not enough energy!"
        else:
            print(f"{seed_name} not found in inventory.")
            return None

class PlayerLuna(PlayerParent):
    def __init__(self, x, y):
        super().__init__(x, y, "Luna", 100)
        self.__FavoritePlant = "Tomato"
        self.__BonusHarvest = 2

    def plantseed(self, seed_obj)-> str:
        seed_name = seed_obj.seedName

        if self.inventory.hasItem(seed_name):
            if self.reduceEnergy(10):
                self.inventory.removeItem(seed_name)
            
                if self.__FavoritePlant == seed_name:
                    print(f"{self.name} planted {self.__FavoritePlant} with extra care because it's her favorite!")
                else:
                    print(f"{self.name} planted {seed_name}.")
                return seed_obj.planted()
            else:
                return "Not enough energy!"
        else:
            print(f"{seed_name} not found in inventory.")
            return None
