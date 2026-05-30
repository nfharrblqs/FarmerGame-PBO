from ClassObject import GREEN, YELLOW, GameObject
from Seed.Plant import PlantBeans, PlantCabbage, PlantCarrot, PlantCorn, PlantGrape, PlantTomato

class Seed(GameObject):
    def __init__(self, seed_name, plant_class, x, y):
        super().__init__(x, y, 15, 15, YELLOW)
        self.seedName = seed_name
        self.plantClass = plant_class
        self.isPlanted = False
        self.watered = False  

    def planted(self):
        self.isPlanted = True
        return self.plantClass(self.x, self.y)


class CarrotSeed(Seed):
    def __init__(self, x, y):
        super().__init__("carrot_seed", PlantCarrot, x, y)
    
    def planted(self):
        self.isPlanted = True
        return PlantCarrot(self.x, self.y)
    

class CornSeed(Seed):
    def __init__(self, x, y):
        super().__init__("corn_seed", PlantCorn, x, y)

    def planted(self):
        self.isPlanted = True
        return PlantCorn(self.x, self.y)


class BeansSeed(Seed):
    def __init__(self, x, y):
        super().__init__("beans_seed", PlantBeans, x, y)


    def planted(self):
        self.isPlanted = True
        return PlantBeans(self.x, self.y)
    

class CabbageSeed(Seed):
    def __init__(self, x, y):
        super().__init__("cabbage_seed", PlantCabbage, x, y)

    def planted(self):
        self.isPlanted = True
        return PlantCabbage(self.x, self.y)


class GrapeSeed(Seed):
    def __init__(self, x, y):
        super().__init__("grape_seed", PlantGrape, x, y)

    def planted(self):
        self.isPlanted = True
        return PlantGrape(self.x, self.y)


class TomatoSeed(Seed):
    def __init__(self, x, y):
        super().__init__("tomato_seed", PlantTomato, x, y)

    def planted(self):
        self.isPlanted = True
        return PlantTomato(self.x, self.y)
