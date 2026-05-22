from ClassObject import GREEN, YELLOW, GameObject

class Seed(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30, YELLOW)
        self.growthtime = 0
        self.isplanted = True
        self.growthstage = 0

    def Planted(self):
        return self.isplanted

    def grow(self):
        self.growthtime += 1
        if self.growthtime >= 100 and self.growthstage == 0:
            self.growthstage = 1
            self.color = GREEN
        elif self.growthtime >= 200 and self.growthstage == 1:
            self.growthstage = 2
            self.color = (0, 200, 0)

    def harvest(self):
        if self.growthstage == 2:
            return 50
        return 0
class SeedWatered(Seed):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.growthstage = 1

    def grow(self):
        self.growthtime += 2
        if self.growthtime >= 100 and self.growthstage == 1:
            self.growthstage = 2
        elif self.growthtime >= 200 and self.growthstage == 2:
            self.growthstage = 3

    def harvest(self):
        if self.growthstage == 3:
            return True
        return False

class Carrot(Seed):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.watered = False

    def water(self):
        self.watered = True
    
    def grow(self):
        if self.watered == False:
            self.growthtime += 1
        else: 
            self.growthtime += 2
        return super().grow()
    
    def harvest(self):
        if self.watered == False and self.growthstage == 2:
            return False
        elif self.watered == True and self.growthstage == 3:
            return True
        return False
    
class Corn(Seed):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.watered = False

    def water(self):
        self.watered = True
    
    def grow(self):
        if self.watered == False:
            self.growthtime += 1
        else: 
            self.growthtime += 3
        
        if self.growthtime >= 100 and self.growthstage == 1:
            self.growthstage = 2
        if self.growthtime >= 220 and self.growthstage == 2:
            self.growthstage = 3
    
    def harvest(self):
        if self.watered == False and self.growthstage == 2:
            return False
        elif self.watered == True and self.growthstage == 3:
            return True
        return False
