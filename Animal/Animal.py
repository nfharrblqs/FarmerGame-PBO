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

    def __del__(self):
        print(f"{self.name} has been removed from the game.")


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
        self.tipe = tipe.lower()
        if "chicken" in self.tipe:
            super().__init__(x, y, "Chicken", 1, 2.0, 100)
            self.color = RED
        elif "cow" in self.tipe:
            super().__init__(x, y, "Cow", 2, 150.0, 100)
            self.color = BROWN
        else:
            super().__init__(x, y, "Bull", 3, 200.0, 100)
            self.color = BROWN

        self.last_update_time = pygame.time.get_ticks()
        self.last_production_time = pygame.time.get_ticks()

    def __del__(self):
        print(f"Destructor: Object {self.name} has been removed from the game.")

    def soundorspeak(self) -> str:
        if "chicken" in self.tipe:
            return "cluck"
        elif "cow" in self.tipe:
            return "MOOOO!"
        elif "bull" in self.tipe:
            return "BULLRUSH!"
    
    def sell(self) -> int:
        if "chicken" in self.tipe:
            return 100
        if "cow" in self.tipe:
            return 500
        if "bull" in self.tipe:
            return 800
        return 400
    
    def update_hunger(self, player_inventory, game_animals_list):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > 8000:  
            self.hunger -= 10
            self.last_update_time = current_time
            print(f"{self.name} hunger decreased to {self.hunger}%")
            if self.hunger < 0:
                print(f"[{self.name}] has died of hunger!")
                if self in game_animals_list:
                    game_animals_list.remove(self)
                return
    
    def give_food(self, player_inventory):
        if player_inventory.hasItem("animal_feed") and self.hunger < 100:
            player_inventory.removeItem("animal_feed")
            self.hunger = min(100, self.hunger + 40)
            print(f"{self.name} has been fed. Current hunger: {self.hunger}%")
            return True
        else:
            print(f"Cannot feed {self.name}. You don't have enough animal food.")
            return False
        
    def produce_goods(self, player_inventory):
        if self.hunger > 40:
            current_time = pygame.time.get.ticks()

            if current_time - self.last_production_time > 15000:
                self.last_production_time = current_time
                
                if "chicken" in self.tipe:
                    player_inventory.addItem("egg")
                    print("The chicken has laid an egg! Egg +1")
                elif "cow" in self.tipe:
                    player_inventory.addItem("milk")
                    print("The cow has produced milk! Milk +1")
                elif "bull" in self.tipe:
                    player_inventory.addItem("meat")
                    print("The bull has produced meat! Meat +1")