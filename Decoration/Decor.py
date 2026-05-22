from ClassObject import GameObject, GREEN, BROWN

class dekorasi(GameObject):
    def __init__(self, x, y, decor_type="tree"):
        super().__init__(x, y, 50, 50, GREEN)
        self.type = decor_type

    def draw(self, surface):
        if self.type == "tree":
            pygame.draw.rect(
                surface,
                BROWN,
                (
                    self.x + self.width // 3,
                    self.y + self.height // 2,
                    self.width // 3,
                    self.height // 2
                )
            )
            pygame.draw.circle(
                surface,
                GREEN,
                (
                    int(self.x + self.width // 2),
                    int(self.y + self.height // 3)
                ),
                20
            )
        elif self.type == "fence":

            pygame.draw.rect(
                surface,
                BROWN,
                (self.x, self.y, self.width, 10)
            )
            pygame.draw.rect(
                surface,
                BROWN,
                (
                    self.x,
                    self.y + self.height - 10,
                    self.width,
                    10
                )
            )