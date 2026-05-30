from ClassObject import HEIGHT, WHITE, WIDTH, GameObject, BROWN, RED
import pygame
import random
from abc import ABC, abstractmethod

class Animal(GameObject, ABC):
    def __init__(self, x, y, name: str, age: int, weight: float, hunger: int = 100):
        super().__init__(x, y, 40, 40, WHITE)
        self.name = name
        self.age = age
        self.weight = weight
        self.hunger = hunger
        self.__last_feeding_time = 0
        self.speed = 1
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    def get_name(self) -> str:
        return self.name

    def get_weight(self) -> float:
        return self.weight
    
    def move(self, direction: list = None):
        if direction:
            self.direction = direction
        
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.direction[0] *= -1 
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.direction[1] *= -1
    
    def eating(self, eat_amount: int):
        self.hunger += eat_amount
        if self.hunger > 100:
            self.hunger = 100
    
    def hunger_decrease(self):
        self.hunger -= 0.1
        if self.hunger < 0:
            self.hunger = 0
    
    @abstractmethod
    def soundorspeak(self) -> str:
        pass 

    @abstractmethod
    def sell(self) -> int:
        pass


class Cow(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, name="cow", age=1, weight=150.0, hunger=100)
        self.speed = 1
        self.milkamount = 0.0
        self.pregnant = False

    def soundorspeak(self) -> str:
        return "Moo!"
    
    def sell(self) -> int:  
        return 500  
    
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, BROWN, (self.x + self.width // 2, self.y + self.height // 2), 20)


class Chicken(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, name="Red Chicken", age=1, weight=2.0, hunger=50)
        self.speed = 2
        self.eggs_count = 0
        self.laying_egg_status = False  

    def soundorspeak(self) -> str:
        return "Cluck!"
    
    def sell(self) -> int:
        return 100
    
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, RED, (self.x + self.width // 2, self.y + self.height // 2), 15)


class Bull(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, name="bull", age=1, weight=500.0, hunger=100)
        self.speed = 1
        self.horn_length = 15.5
        self.strength = 80
    
    def soundorspeak(self) -> str:
        return "MOOOO!"
    
    def changeToMeat(self):
        pass

    def sell(self) -> int:
        return 800
    
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, BROWN, (self.x + self.width // 2, self.y + self.height // 2), 25)

class animal(Animal):
    def __init__(self, x, y, tipe):
        if tipe == "chicken":
            super().__init__(x, y, "Chicken", 1, 2.0, 50)
            self.tipe = tipe
            self.color = RED
        else:
            super().__init__(x, y, "Cow", 2, 150.0, 100)
            self.tipe = tipe
            self.color = BROWN
    
    def soundorspeak(self) -> str:
        return "Animal sound!"
    
    def sell(self) -> int:
        return 100
    
    def moverandom(self):  
        """random move animal"""
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.direction[0] *= -1 
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.direction[1] *= -1
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x + 20, self.y + 20), 18)
        pygame.draw.circle(surface, WHITE, (self.x + 12, self.y + 15), 4)
        pygame.draw.circle(surface, WHITE, (self.x + 28, self.y + 15), 4)
