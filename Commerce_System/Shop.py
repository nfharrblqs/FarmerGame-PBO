import pygame
from ClassObject import GameObject, YELLOW

class Shop(GameObject):
    def __init__(self, x, y):

        super().__init__(x, y, 50, 50, YELLOW)

        self.shopItems = {
            
            "corn_seed": 10,
            "tomato_seed": 7,
            "carrot_seed": 5,
            "beans_seed": 22,
            "cabbage_seed": 17,
            "grape_seed": 15,
            "chicken": 50,  
            "cow": 500,       
            "bull": 800  
        }
        self.__money = 6000
        
        self.SellPrices = {
            #seed
            'corn_seed': 5, 'tomato_seed': 3, 'carrot_seed': 2,
            'beans_seed': 10,'cabbage_seed': 7,'grape_seed': 6,
            
            #Live Animals
            "chicken": 25,"cow": 250,"bull": 400,

            #Animal Products
            "egg": 15,"milk": 40,"meat": 60,

            #Crops
            "corn": 90, "tomato": 80, "carrot": 70, 
            "beans": 100, "cabbage": 60, "grape": 85
        }

    def SellToPlayer(self, player, item=None, money=None, animal=None, animal_Product=None) -> bool:
        """Toko menjual sesuatu kepada player"""

        if animal_Product:
            print("[SHOP] Shop isn't selling animal products.")
            return False
        
        target_item = item or animal

        if not target_item or target_item not in self.shopItems:
            print("[SHOP] Item not available in shop.")
            return False
        
        price = self.__shopItems[target_item]

        if player.getMoney() >= price:
            player.buyItem(target_item, price)
            self.__money += price #duit toko nambah
            print(f"[SHOP] {player.getName()} bought {target_item} for {price} money.")
            return True
        else:
            print(f"[SHOP] {player.getName()} doesn't have enough money.")
            return False
    
    def buyFromPlayer(self, player, item=None, money=None, animal_product=None, animal=None, crops=None, game_animals_list=None) -> bool:
        """Toko membeli sesuatu dari player"""

        target_item = item or animal_product

        #Jual dari inventory
        if target_item:
            if player.inventory.hasItem(target_item):
                sell_price = self.__sellPrices.get(target_item, 0)
                
                if self.__money >= sell_price:
                    self.__money -= sell_price
                    player.inventory.removeItem(target_item)

                    player._PlayerParent__money += sell_price

                    print(f"[SHOP] {player.getName()} sold {target_item} for {sell_price} money.")
                    return True
                else:
                    print("[SHOP] Shop doesn't have enough money to buy this item.")
                    return False
            else:
                print(f"You don't have {target_item} in inventory.")
                return False
            
        #Jual hewan dari map
        if animal:
            animal_type = animal.type if hasattr(animal, 'type') else animal.name.lower()

            if animal_type in self.__sellPrices:
                sell_price = self.__sellPrices[animal_type]

                if self.__money >= sell_price:
                    self.__money -= sell_price
                    player._PlayerParent__money += sell_price

                    if game_animals_list is not None and animal in game_animals_list:
                        game_animals_list.remove(animal)

                    print(f"[SHOP] {player.getName()} sold {animal_type} for {sell_price} money.")
                    return True
                else:
                    print("[SHOP] Shop doesn't have enough money to buy this animal.")
                    return False
            else:
                print(f"[SHOP] {animal_type} cannot be sold to the shop.")
                return False
        return False
    
    def draw(self, surface):
        super().draw(surface)
        font = pygame.font.Font(None, 30)
        text = font.render("$", True, (0,0,0))
        surface.blit(text, (self.x + 20, self.y + 10))