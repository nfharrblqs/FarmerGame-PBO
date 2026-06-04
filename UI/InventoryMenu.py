import pygame
from ClassObject import WIDTH, HEIGHT

class InventoryMenu:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
        self.selected_index = 0
        self.hover_index = -1
        self.mode = "view" 
        
    def show(self):
        self.visible = True
        self.selected_index = 0
        self.mode = "view"
        print("Inventory Menu - Klik benih untuk tanam")
        
    def hide(self):
        self.visible = False
        
    def handle_click(self, mouse_pos, player, game):
        """Handle click in inventory menu"""
        if not self.visible:
            return None, None
            
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            y_offset = self.y + 70
            items = list(player._inventory.items.items())
            
            for i, (item_name, amount) in enumerate(items):
                item_rect = pygame.Rect(self.x + 10, y_offset - 5, self.width - 20, 40)

                if item_rect.collidepoint(mouse_pos):
                    
                    if self.mode == "sell":
                        success = game.shop.buyFromPlayer(player, item=item_name)
                        if success:
                           if hasattr(game, 'selling_sound') and game.selling_sound:
                            game.selling_sound.play()
                            return item_name, "sell"
                        return None, None
                    elif self.mode == "view":
                        if "seed" in item_name:
                            self.hide()
                            return item_name, "plant"
                        elif item_name in ["chicken", "cow", "bull"]:
                            self.hide()
                            return item_name, "place_animal"
                        elif item_name ==  "watering_can":
                            self.hide()
                            return item_name, "tool"
                        else:
                            print(f"{item_name} tidak bisa ditanam (bukan benih atau hewan)")
                            return None, None
                y_offset += 45
        else:
            self.hide()
            
        return None, None
        
    def update_hover(self, mouse_pos, inventory):
        if not self.visible:
            return
        self.hover_index = -1
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            y_offset = self.y + 70
            items = list(inventory.items.items())
            for i in range(len(items)):
                item_rect = pygame.Rect(self.x + 10, y_offset - 5, self.width - 20, 40)
                if item_rect.collidepoint(mouse_pos):
                    self.hover_index = i
                    break
                y_offset += 45
        
    def draw(self, surface, player, mouse_pos):
        if not self.visible:
            return
        
        inventory = player._inventory    
        items = list(inventory.items.items())
        self.update_hover(mouse_pos, inventory)
        

        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(230)
        overlay.fill((30, 30, 40))
        surface.blit(overlay, (self.x, self.y))
        
        if self.mode == "view":
            border_color = (0, 255, 255)  
        elif self.mode == "sell":
            border_color = (255, 0, 0)   
        else:
            border_color = (255, 255, 0)   
        pygame.draw.rect(surface, border_color, (self.x, self.y, self.width, self.height), 3)
        

        title_font = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 30) #48)
        if self.mode == "view":
            title = title_font.render("INVENTORY", True, (0, 255, 255))
        elif self.mode == "sell":
            title = title_font.render("SELL SOMETHING", True, (255, 0, 0))
        else:
            title = title_font.render("MOVE SOMETHING", True, (255, 255, 0))
        surface.blit(title, (self.x + self.width//2 - title.get_width()//2, self.y + 15))
        
        y_offset = self.y + 80
        font = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 18)
        
        if not items:
            empty_text = font.render("Inventory kosong!", True, (150, 150, 150))
            surface.blit(empty_text, (self.x + self.width//2 - empty_text.get_width()//2, y_offset))
        else:
            for i, (item_name, amount) in enumerate(items):
   
                if i == self.hover_index:
                    pygame.draw.rect(surface, border_color + (80,), 
                                   (self.x + 10, y_offset - 5, self.width - 20, 38))
                    color = border_color
                else:
                    color = (255, 255, 255)
                
                if "seed" in item_name:
                    icon = "Seed "
                    display_name = item_name.replace("_", " ").title().replace("Seed", "")
                elif item_name == "chicken":
                    icon = ""
                    display_name = "Chicken"
                elif item_name == "cow":
                    icon = ""
                    display_name = "cow"
                elif item_name == "bull":
                    icon = ""
                    display_name = "Bull"
                elif "corn" in item_name and "seed" not in item_name:
                    icon = ""
                    display_name = "corn"
                elif "carrot" in item_name and "seed" not in item_name:
                    icon = ""
                    display_name = "carrot"
                elif "tomato" in item_name and "seed" not in item_name:
                    icon = ""
                    display_name = "tomato"
                elif item_name == "watering_can":
                    icon = ""
                    display_name = "Watering Can"
                elif item_name == "egg":
                    icon = ""
                    display_name = "Egg"
                else:
                    icon = "inventory"
                    display_name = item_name.replace("_", " ").title()
                
                text = font.render(f"{icon}{display_name}", True, color)
                surface.blit(text, (self.x + 30, y_offset))
                
                amount_text = font.render(f"x{amount}", True, (150, 150, 150))
                surface.blit(amount_text, (self.x + self.width - 70, y_offset))
                
                y_offset += 48
        
        mode_font = pygame.font.Font(None, 18)
        if self.mode == "view":
            mode_text = mode_font.render("Tekan S untuk mode JUAL | Tekan M untuk mode PINDAH", True, (100, 100, 100))
        elif self.mode == "sell":
            mode_text = mode_font.render("Klik item untuk jual | Tekan V untuk kembali ke VIEW", True, (100, 100, 100))
        else:
            mode_text = mode_font.render("Klik item untuk pindah | Tekan V untuk kembali ke VIEW", True, (100, 100, 100))
        surface.blit(mode_text, (self.x + 20, self.y + self.height - 25))
