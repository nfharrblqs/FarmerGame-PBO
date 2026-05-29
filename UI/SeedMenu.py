import pygame

class SeedMenu:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
        self.available_seeds = []
        self.hover_index = -1
        
    def show(self, inventory):
        """Tampilkan menu"""
        self.available_seeds = [item for item in inventory.items if "seed" in item]
        if self.available_seeds:
            self.visible = True
            return True
        else:
            print("Tidak ada seed di inventory!")
            return False
        
    def hide(self):
        self.visible = False
        
    def handle_click(self, mouse_pos):
        """Handle mouse click, return seed yang dipilih"""
        if not self.visible:
            return None
            
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            y_offset = self.y + 70
            for i, seed in enumerate(self.available_seeds):
                item_rect = pygame.Rect(self.x + 10, y_offset - 5, self.width - 20, 40)
                if item_rect.collidepoint(mouse_pos):
                    self.hide()
                    return seed
                y_offset += 45
        else:
            self.hide()
            
        return None
        
    def update_hover(self, mouse_pos):
        """Update hover effect"""
        if not self.visible:
            return
            
        self.hover_index = -1
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            y_offset = self.y + 70
            for i in range(len(self.available_seeds)):
                item_rect = pygame.Rect(self.x + 10, y_offset - 5, self.width - 20, 40)
                if item_rect.collidepoint(mouse_pos):
                    self.hover_index = i
                    break
                y_offset += 45
        
    def draw(self, surface, inventory, mouse_pos):
        if not self.visible:
            return
            
        self.update_hover(mouse_pos)
            
        self.available_seeds = [item for item in inventory.items if "seed" in item]
        
        if not self.available_seeds:
            self.hide()
            return

        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(230)
        overlay.fill((30, 30, 40))
        surface.blit(overlay, (self.x, self.y))
        
        pygame.draw.rect(surface, (255, 215, 0), (self.x, self.y, self.width, self.height), 3)
        
        title_font = pygame.font.Font(None, 48)
        title = title_font.render("PILIH SEED", True, (255, 215, 0))
        surface.blit(title, (self.x + self.width//2 - title.get_width()//2, self.y + 15))
        
        y_offset = self.y + 70
        font = pygame.font.Font(None, 36)
        
        for i, seed in enumerate(self.available_seeds):
            if i == self.hover_index:
                pygame.draw.rect(surface, (255, 215, 0, 80), 
                               (self.x + 10, y_offset - 5, self.width - 20, 40))
                color = (255, 215, 0)
            else:
                color = (255, 255, 255)
                
            seed_name = seed.replace("_", " ").title()
            text = font.render(seed_name, True, color)
            surface.blit(text, (self.x + 30, y_offset))
            
            jumlah_text = font.render(f"x{inventory.items[seed]}", True, (150, 150, 150))
            surface.blit(jumlah_text, (self.x + self.width - 70, y_offset))
            
            y_offset += 45
            
        small_font = pygame.font.Font(None, 24)
        hint = small_font.render("Klik seed untuk menanam | Klik di luar untuk batal", True, (200, 200, 200))
        surface.blit(hint, (self.x + 20, self.y + self.height - 30))