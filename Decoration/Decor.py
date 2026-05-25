from ClassObject import RED, GameObject, GREEN, BROWN
from abc import ABC, abstractmethod
import pygame

class Decoration(GameObject, ABC):
    def __init__(self, x: int, y: int, name: str, price: int, durability: int):
        super().__init__(x, y, 50, 50, GREEN)
        
        self._name = name
        self._price = price
        self._durability = durability
        self._positionx = x 
        self._positiony = y 

    def placement(self):
        print(f"{self._name} placed at ({self._positionx}, {self._positiony}).")
    
    def remove(self):
        print(f"{self._name} removed from ({self._positionx}, {self._positiony}).")
    
    @abstractmethod
    def draw(self, surface):
        pass

class Scarecrow(Decoration):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, name="Scarecrow", price=150, durability=100)
    
        self.__scareRadius = 100
        self.effectiveness = 85
    
    def scareBirds(Self):
        print("Scarecrow is scaring away birds within its radius.")

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, (self.x + 22, self.y + 10, 6, 40))
        pygame.draw.rect(surface, BROWN, (self.x + 10, self.y + 20, 30, 6))
        pygame.draw.circle(surface, BROWN, (self.x + 25, self.y + 12), 10)

class Flowerpot(Decoration):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, name="Flowerpot", price=50, durability=50)
        self.__plantType = "Flower"
        self.__waterLevel = 20
        self.__flowerBloomed = False
    
    def waterPlant(self):
        self.__waterLevel += 10
        print("Flowers in the flowerpot have been watered.")

    def growFlower(self):
        if self.__waterLevel >= 40:
            self.__flowerBloomed = True
            print("The flower in the flowerpot has bloomed!")
    
    def draw(self, surface):
        pygame.draw.rect(surface, (139, 69, 19), (self.x + 15, self.y + 25, 20, 25))
        pygame.draw.circle(surface, RED, (self.x + 25, self.y + 15), 8)

class GardenBench(Decoration):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, name="Garden Bench", price=200, durability=150)
        self.__seatingCapacity = 2
        self.__comfortLevel = 80

        def sit(self):
            print("Sitting on the garden bench.")

        def rest(self):
            print("Resting on the garden bench, restoring energy.")
        
        def draw(self, surface):
            pygame.draw.rect(surface, (100, 50, 10), (self.x + 5, self.y + 15, 40, 10)) #sandaran
            pygame.draw.rect(surface, (120, 60, 15), (self.x + 5, self.y + 25, 40, 8)) #dudukan 
            pygame.draw.rect(surface, (50, 25, 5), (self.x + 8, self.y + 33, 4, 12)) #kaki kiri
            pygame.draw.rect(surface, (50, 25, 5), (self.x + 38, self.y + 33, 4, 12))# kaki kanan
            
