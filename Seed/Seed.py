from ClassObject import GREEN, YELLOW, GameObject

class Seed(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30, YELLOW)
        self.growthtime = 0
        self.isplanted = True
        self.growthstage = 0

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
    def __init__()