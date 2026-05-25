from ClassObject import GameObject
from abc import ABC, abstractmethod

class AbstractPlant(GameObject, ABC):
    def __init__(self, x, y, plant_type, maxGrowth):
        super().__init__(x, y, 30, 30, (0, 255, 0))
        self.plant_type  = plant_type
        self.growth_time = 0
        self.maxGrowth = maxGrowth
        self.growth_stage = 0
        self.isWatered = False

    def waterPlant(self):
        self.isWatered = True
    
    @abstractmethod
    def abstractGrow(self):
        pass

    @abstractmethod
    def abstractHarvest(self):
        pass

class PlantCorn(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="corn", maxGrowth=220)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 3
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (0, 200, 0)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (0, 150, 0)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2

class PlantCarrot(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="carrot", maxGrowth=150)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (255, 165, 0)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (255, 140, 0)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2

class PlantTomato(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="tomato", maxGrowth=180)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (255, 99, 71)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (255, 69, 0)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2

class PlantBeans(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="beans", maxGrowth=200)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (34, 139, 34)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (0, 128, 0)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2

class PlantCabbage(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="cabbage", maxGrowth=170)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (144, 238, 144)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (0, 255, 127)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2

class PlantGrape(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="grape", maxGrowth=190)

    def abstractGrow(self):
        if not self.isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2
        
        if self.growth_time >= 100 and self.growth_stage == 0:
            self.growth_stage = 1
            self.color = (138, 43, 226)
        if self.growth_time >= self.maxGrowth and self.growth_stage == 1:
            self.growth_stage = 2
            self.color = (75, 0, 130)
    
    def abstractHarvest(self) -> bool:
        return self.growth_stage == 2