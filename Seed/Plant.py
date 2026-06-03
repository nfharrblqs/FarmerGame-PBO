import pygame
from ClassObject import GameObject
from abc import ABC, abstractmethod

class AbstractPlant(GameObject, ABC):
    def __init__(self, x, y, plant_type, maxGrowth):
        super().__init__(x, y, 30, 30, (0, 255, 0))
        self._plant_type = plant_type
        self._growth_time = 0
        self._maxGrowth = maxGrowth
        self._growth_stage = 0
        self.isWatered = False

    def draw(self, surface):
        if self._growth_stage == 0:
            image = self.stage0
        elif self._growth_stage == 1:
            image = self.stage1
        elif self._growth_stage == 2:
            image = self.stage2
        elif self._growth_stage == 3:
            image = self.stage3
        else:
            image = self.stage4

        surface.blit(image, (self.x, self.y))

    def waterPlant(self):
        self.isWatered = True
    
    @abstractmethod
    def abstractGrow(self):
        pass

    @abstractmethod
    def abstractHarvest(self):
        pass

    def __del__(self): #destruktor
        print(f"{self._plant_type} plant removed from this field.")



class PlantCorn(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="corn", maxGrowth=220)

        self.stage0 = pygame.image.load("AssetPNG/corn/cornstage1.png").convert_alpha()
        self.stage1 = pygame.image.load("AssetPNG/corn/cornstage2.png").convert_alpha()
        self.stage2 = pygame.image.load("AssetPNG/corn/cornstage3.png").convert_alpha()
        self.stage3 = pygame.image.load("AssetPNG/corn/cornstage4.png").convert_alpha()
        self.stage4 = pygame.image.load("AssetPNG/corn/harvestcorn.png").convert_alpha()


        self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        self.stage3 = pygame.transform.scale(self.stage3, (16,16))
        self.stage4 = pygame.transform.scale(self.stage4, (16,16))

    def abstractGrow(self):
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "corn"
        return None
    


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
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "carrot"
        return None

class PlantTomato(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="tomato", maxGrowth=180)

        self.stage0 = pygame.image.load("AssetPNG/tomato/tomatostage1.png").convert_alpha()
        self.stage1 = pygame.image.load("AssetPNG/tomato/tomatostage2.png").convert_alpha()
        self.stage2 = pygame.image.load("AssetPNG/tomato/tomatostage3.png").convert_alpha()
        self.stage3 = pygame.image.load("AssetPNG/tomato/tomatostage4.png").convert_alpha()
        self.stage4 = pygame.image.load("AssetPNG/tomato/harvesttomato.png").convert_alpha()

        self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        self.stage3 = pygame.transform.scale(self.stage3, (16,16))
        self.stage4 = pygame.transform.scale(self.stage4, (16,16))

    def abstractGrow(self):
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "tomato"
        return None

class PlantBeans(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="beans", maxGrowth=200)
        
        #self.stage0 = pygame.image.load("AssetPNG/corn/cornstage1.png").convert_alpha()
        #self.stage1 = pygame.image.load("AssetPNG/corn/cornstage2.png").convert_alpha()
        #self.stage2 = pygame.image.load("AssetPNG/corn/cornstage3.png").convert_alpha()
        #self.stage3 = pygame.image.load("AssetPNG/corn/cornstage4.png").convert_alpha()

        #self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        #self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        #self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        #self.stage3 = pygame.transform.scale(self.stage3, (16,16))

    def abstractGrow(self):
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "beans"
        return None

class PlantCabbage(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="cabbage", maxGrowth=170)

        #self.stage0 = pygame.image.load("AssetPNG/tomato/cornstage1.png").convert_alpha()
        #self.stage1 = pygame.image.load("AssetPNG/corn/cornstage2.png").convert_alpha()
        #self.stage2 = pygame.image.load("AssetPNG/corn/cornstage3.png").convert_alpha()
        #self.stage3 = pygame.image.load("AssetPNG/corn/cornstage4.png").convert_alpha()

        #self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        #self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        #self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        #self.stage3 = pygame.transform.scale(self.stage3, (16,16))

    def abstractGrow(self):
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "cabbage"
        return None

class PlantGrape(AbstractPlant):
    def __init__(self, x, y):
        super().__init__(x, y, plant_type="grape", maxGrowth=190)

        #self.stage0 = pygame.image.load("AssetPNG/corn/cornstage1.png").convert_alpha()
        #self.stage1 = pygame.image.load("AssetPNG/corn/cornstage2.png").convert_alpha()
        #self.stage2 = pygame.image.load("AssetPNG/corn/cornstage3.png").convert_alpha()
        #self.stage3 = pygame.image.load("AssetPNG/corn/cornstage4.png").convert_alpha()

        #self.stage0 = pygame.transform.scale(self.stage0, (16,16))
        #self.stage1 = pygame.transform.scale(self.stage1, (16,16))
        #self.stage2 = pygame.transform.scale(self.stage2,(16,16))
        #self.stage3 = pygame.transform.scale(self.stage3, (16,16))


    def abstractGrow(self):
        if not self.isWatered:
            self._growth_time += 1
        else:
            self._growth_time += 2

        if self._growth_time < 50:
            self._growth_stage = 0
        elif self._growth_time < 100:
            self._growth_stage = 1
        elif self._growth_time < 150:
            self._growth_stage = 2
        elif self._growth_time < self._maxGrowth:
            self._growth_stage = 3
        else:
            self._growth_stage = 4
    
    def abstractHarvest(self) -> bool:
        if self._growth_stage == 4:
            return "grape"
        return None

