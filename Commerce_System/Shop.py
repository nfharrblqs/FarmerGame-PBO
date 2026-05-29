import pygame
from ClassObject import GameObject, YELLOW

class Shop(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, YELLOW)
        self.shopItems = {
            "corn_seed": 50,
            "tomato_seed": 50,
            "carrot_seed": 40,
            "beans_seed": 45,
            "cabbage_seed": 35,
            "grape_seed": 30
        }

    def buy(self, player, item_name):
        if item_name in self.shopItems:
            price = self.shopItems[item_name]
            if player.money >= price:
                player.money -= price
                player.gold = player.money
                player.inventory.addItem(item_name)
                print(f"{item_name} bought for {price} gold!")
                return True
            else:
                print("Money is not enough!")
                return False
        else:
            print("Item not available in shop")
            return False

    def sell_item(self, player, item_name):
        if player.inventory.hasItem(item_name):
            sell_price = self.shopItems.get(item_name, 0) // 2
            player.money += sell_price
            player.gold = player.money
            player.inventory.removeItem(item_name)
            print(f"{item_name} sold for {sell_price} gold!")
            return True
        else:
            print("Item not found in inventory!")
            return False
    
    def draw(self, surface):
        super().draw(surface)
        # Gambar tanda tanya di shop
        font = pygame.font.Font(None, 30)
        text = font.render("?", True, (0, 0, 0))
        surface.blit(text, (self.x + 20, self.y + 10))