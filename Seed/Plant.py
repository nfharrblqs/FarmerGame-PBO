import pygame
from ClassObject import GameObject
from abc import ABC, abstractmethod

class AbstractPlant(GameObject, ABC):
    def __init__(self, x, y, plant_type, maxGrowth):
        super().__init__(x, y, 30, 30, (0, 255, 0))

        self.plant_type = plant_type
        self.growth_time = 0

        self._growth_stage = 0
        self._isWatered = False

        self.stages = []

    def draw(self, surface):
        """Menggambar tanaman sesuai dengan stage pertumbuhannya"""
        if self.stages:
            stage_index = min(self._growth_stage, len(self.stages) - 1)
            surface.blit(self.stages[stage_index], (self.x, self.y))

    def waterPlant(self):
        """Mengubah status siram menjadi True"""
        self._isWatered = True

    @abstractmethod
    def abstractGrow(self):
        pass

    @abstractmethod
    def abstractHarvest(self):
        pass

class PlantCorn(AbstractPlant):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, plant_type="corn")

        self.__seedName = "corn_seed"
        self.__growthTime9 = 220

        paths = [
            "AssetPNG/corn/cornstage1.png",
            "AssetPNG/corn/cornstage2.png",
            "AssetPNG/corn/cornstage3.png",
            "AssetPNG/corn/cornstage4.png",
            "AssetPNG/corn/harvestcorn.png",
        ]

        self.stages = [
            pygame.transform.scale(
                pygame.image.load(p).convert_alpha(), (16,16)
            )
            for p in paths
        ]

    def plantCorn(self, seed) -> str:
        return f"Corn planted from {seed}"

    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.__growthTime9:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4

class PlantCarrot(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="carrot", maxGrowth=150)

        #self.stage0 = pygame.image.load("AssetPNG/corn/cornstage1.png").convert_alpha()
        #self.stage1 = pygame.image.load("AssetPNG/corn/cornstage2.png").convert_alpha()
        #self.stage2 = pygame.image.load("AssetPNG/corn/cornstage3.png").convert_alpha()
        #self.stage3 = pygame.image.load("AssetPNG/corn/cornstage4.png").convert_alpha()

        #self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        #self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        #self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        #self.stage3 = pygame.transform.scale(self.stage3, (16,16))


    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4

class PlantTomato(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="tomato")

        self.__seedName = "tomato_seed"
        self.__growthTime3 = 180

        paths = [
            "AssetPNG/tomato/tomatostage1.png",
            "AssetPNG/tomato/tomatostage2.png",
            "AssetPNG/tomato/tomatostage3.png",
            "AssetPNG/tomato/tomatostage4.png",
            "AssetPNG/tomato/harvesttomato.png",
        ]

        self.stages = [
            pygame.transform.scale(
                pygame.image.load(p).convert_alpha(), (16,16)
            )
            for p in paths
        ]
    
    def plantTomato(self, seed) -> str:
        return f"Tomato planted from {seed}"

    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.__growthTime3:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4

class PlantBeans(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="beans")

        self.__seedName = "beans_seed"
        self.__growthTime10 = 200
        
        paths = [

        ]

        self.stages = [
            pygame.transform.scale(
                pygame.image.load(p).convert_alpha(), (16,16)
            )
            for p in paths
        ]

    def plantBeans(self, seed) -> str:
        return f"Beans planted from {seed}"

    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.__growthTime10:
            self._growth_stage = 3
        else:
            self._growth_stage = 4

    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4

class PlantCabbage(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="cabbage")

        self.__seedName = "cabbage_seed"
        self.__growthTime2 = 130

        paths = [

        ]

        self.stages = [

        ]

    def plantCabbage(self, seed) -> str:
        return f"Cabbage planted from {seed}"

    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.__growthTime2:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4

class PlantGrape(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="grape")

        self.__seedName = "grape_seed"
        self.__growthTime7 = 190

        paths = [

        ]

        self.stages = [

        ]

    def plantGrape(self, seed) -> str:
        return f"Grape planted from {seed}"


    def abstractGrow(self):
        if not self._isWatered:
            self.growth_time += 1
        else:
            self.growth_time += 2

        if self.growth_time < 50:
            self._growth_stage = 0
        elif self.growth_time < 100:
            self._growth_stage = 1
        elif self.growth_time < 150:
            self._growth_stage = 2
        elif self.growth_time < self.__growthTime7:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        return self._growth_stage == 4
