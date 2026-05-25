from ClassObject import GREEN, YELLOW, GameObject
from Seed.Plant import PlantBeans, PlantCabbage, PlantCarrot, PlantCorn, PlantGrape, PlantTomato

class Seed(GameObject):
    def __init__(self, seed_name, plant_class, x, y):
        super().__init__(x, y, 15, 15, YELLOW)
        self.seedName = seed_name
        self.plantClass = plant_class
        self.isPlanted = False
    
    def planted(self):
        self.isPlanted = True
        return self.plantClass(self.x, self.y)

class Carrot(Seed):
    def __init__(self, x, y):
        super().__init__("carrot", Carrot, x, y)
    
    def planted(self):
        self.isPlanted = True
        return PlantCarrot(self.x, self.y)
    
class Corn(Seed):
    def __init__(self, x, y):
        super().__init__("corn", Corn, x, y)
        self.watered = False

    def planted(self):
        self.isPlanted = True
        return PlantCorn(self.x, self.y)
class Beans(Seed):
    def __init__(self, x, y):
        super().__init__("beans", Beans, x, y)
        self.watered = False

    def planted(self):
        self.isPlanted = True
        return PlantBeans(self.x, self.y)
    
class Cabbage(Seed):
    def __init__(self, x, y):
        super().__init__("cabbage", Cabbage, x, y)
        self.watered = False

    def planted(self):
        self.isPlanted = True
        return PlantCabbage(self.x, self.y)

class Grape(Seed):
    def __init__(self, x, y):
        super().__init__("grape", Grape, x, y)
        self.watered = False

    def planted(self):
        self.isPlanted = True
        return PlantGrape(self.x, self.y)


class Tomato(Seed):
    def __init__(self, x, y):
        super().__init__("tomato", Tomato, x, y)
        self.watered = False

    def planted(self):
        self.isPlanted = True
        return PlantTomato(self.x, self.y)