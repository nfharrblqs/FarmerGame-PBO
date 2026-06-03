import pygame
from ClassObject import GameObject, GREEN, BROWN, RED
from abc import ABC, abstractmethod

class Decoration(GameObject, ABC):
    def __init__(self, x, y, width, height, color, name, price, durability):
        super().__init__(x, y, width, height, color)
        self._name = name
        self._price = price
        self._durability = durability
        self._max_durability = durability  
        self._positionx = x 
        self._positiony = y 

    def placement(self):
        print(f"{self._name} placed at ({self._positionx}, {self._positiony}).")
    
    def remove(self):
        print(f"{self._name} removed from ({self._positionx}, {self._positiony}).")
    
    def get_damage(self, amount):  
        self._durability -= amount
        if self._durability <= 0:
            print(f"{self._name} is broken!")
            return True
        return False
    
    def repair(self):  
        self._durability = self._max_durability
        print(f"{self._name} repaired!")
    
    @abstractmethod
    def draw(self, surface):
        pass


class Scarecrow(Decoration):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, BROWN, "Scarecrow", 150, 100)
        self._scareRadius = 100  
        self.effectiveness = 85
    
    def scareBirds(self):
        print("Scarecrow is scaring away birds within its radius.")
    
    def draw(self, surface):
  
        pygame.draw.rect(surface, BROWN, (self.x + 20, self.y + 15, 10, 30))

        pygame.draw.rect(surface, BROWN, (self.x + 8, self.y + 25, 34, 6))

        pygame.draw.circle(surface, (200, 200, 100), (self.x + 25, self.y + 12), 12)

        pygame.draw.rect(surface, (100, 50, 0), (self.x + 15, self.y + 3, 20, 8))
        pygame.draw.rect(surface, (100, 50, 0), (self.x + 10, self.y + 8, 30, 5))


class Flowerpot(Decoration):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, GREEN, "Flowerpot", 50, 50)
        self._plantType = "Flower"  
        self._waterLevel = 20
        self._growth = 0 
        self._flowerBloomed = False
    
    def waterPlant(self):
        self._waterLevel += 10
        if self._waterLevel > 100:
            self._waterLevel = 100
        print("Flowers in the flowerpot have been watered.")

    def growFlower(self):
        if self._waterLevel >= 40 and not self._flowerBloomed:
            self._growth += 1
            if self._growth >= 30:
                self._flowerBloomed = True
                print("The flower in the flowerpot has bloomed!")
    
    def update(self): 
        if self._waterLevel > 0:
            self._waterLevel -= 0.05
        self.growFlower()
    
    def draw(self, surface):
   
        pygame.draw.rect(surface, (139, 69, 19), (self.x + 15, self.y + 25, 20, 25))
        pygame.draw.rect(surface, (100, 50, 10), (self.x + 13, self.y + 22, 24, 5))
        

        pygame.draw.ellipse(surface, (101, 67, 33), (self.x + 17, self.y + 27, 16, 8))    
  
        if self._flowerBloomed:
  
            pygame.draw.line(surface, GREEN, (self.x + 25, self.y + 27), (self.x + 25, self.y + 10), 3)
            pygame.draw.circle(surface, RED, (self.x + 25, self.y + 8), 6)
            pygame.draw.circle(surface, (255, 165, 0), (self.x + 25, self.y + 8), 3)
        elif self._growth > 0:
            pygame.draw.line(surface, GREEN, (self.x + 25, self.y + 27), (self.x + 25, self.y + 18), 2)
            pygame.draw.circle(surface, GREEN, (self.x + 25, self.y + 17), 3)


class GardenBench(Decoration):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, (100, 50, 10), "Garden Bench", 200, 150)
        self._seatingCapacity = 2
        self._comfortLevel = 80
        self._occupied = False  

    def sit(self):
        if not self._occupied:
            self._occupied = True
            print("Sitting on the garden bench. Energy restored!")
            return 20
        return 0

    def stand(self): 
        self._occupied = False
        print("Stand up from the bench.")
    
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 50, 10), (self.x + 5, self.y + 15, 40, 10))
        pygame.draw.rect(surface, (120, 60, 15), (self.x + 5, self.y + 25, 40, 8))
        pygame.draw.rect(surface, (50, 25, 5), (self.x + 8, self.y + 33, 4, 12))
        pygame.draw.rect(surface, (50, 25, 5), (self.x + 38, self.y + 33, 4, 12))
