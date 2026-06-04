import pygame
from ClassObject import WHITE, WIDTH, HEIGHT

class LoadingScreen:
    def __init__(self):
        self.visible = True
        self.selected_option = 0  
        self.options = ["START", "EXIT"]

        self.characters = ["Steve", "Luna"]
        self.selected_char_index = 0

        self.font_input = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 18)
        self.font_title = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 18)

        self.steve_rect = pygame.Rect(WIDTH // 2 - 92, 450, 100, 40) 
        self.luna_rect = pygame.Rect(WIDTH // 2 + 28, 450, 100, 40)

        try:
            self.background = pygame.image.load("AssetPNG/Startpage/barugamestart.png").convert_alpha()
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
            print("Loading screen background loaded")
        except:
            print("Background tidak ditemukan, pakai warna default")
            self.background = None

        self.button_width = 140
        self.button_height = 38

        self.start_center = (420, 320)
        self.exit_center = (420, 380)

        try:
            self.start_button = pygame.image.load("AssetPNG/Startpage/StartButton.png").convert_alpha()
            self.start_button = pygame.transform.scale(self.start_button, (140, 38))
            self.exit_button = pygame.image.load("AssetPNG/Startpage/ExitButton.png").convert_alpha()
            self.exit_button = pygame.transform.scale(self.exit_button, (140, 38))
            print("Button image loaded")
        except:
            print("Button image not found")
            self.start_button = None
            self.exit_button = None

        if self.start_button:
            self.start_rect = self.start_button.get_rect(center=self.start_center)
            self.exit_rect = self.exit_button.get_rect(center=self.exit_center)
        else:
            self.start_rect = pygame.Rect(self.start_center[0]-70, self.start_center[1]-19, 140, 38)
            self.exit_rect = pygame.Rect(self.exit_center[0]-70, self.exit_center[1]-19, 140, 38)

    def handle_input(self, event):
        """Handle keyboard dan mouse input di loading screen"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                mouse_pos = pygame.mouse.get_pos()
                if self.steve_rect.collidepoint(mouse_pos):
                    self.selected_char_index = 0
                    print("Selected Steve")
                elif self.luna_rect.collidepoint(mouse_pos):
                    self.selected_char_index = 1
                    print("Selected Luna")

                if self.start_rect and self.start_rect.collidepoint(mouse_pos):
                    print(f"Starting game with character: {self.characters[self.selected_char_index]}")
                    return "start"
                elif self.exit_rect and self.exit_rect.collidepoint(mouse_pos):
                    print("Klik EXIT!")
                    return "exit"
        
        elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if self.start_rect and self.start_rect.collidepoint(mouse_pos):
                    self.selected_option = 0
                elif self.exit_rect and self.exit_rect.collidepoint(mouse_pos):
                    self.selected_option = 1

        return None

    def draw(self, surface):
        if self.background:
            surface.blit(self.background, (0, 0))
        else:
            surface.fill((30, 30, 50))

        mouse_pos = pygame.mouse.get_pos()

        if self.start_button:
            if self.start_rect.collidepoint(mouse_pos):
                start_img = pygame.transform.scale(self.start_button, (130, 35))
            else:
                start_img = pygame.transform.scale(self.start_button, (140, 38))
            self.start_rect = start_img.get_rect(center=self.start_center)
            surface.blit(start_img, self.start_rect)
        else:
            pygame.draw.rect(surface, (0, 200, 0), self.start_rect)

        if self.exit_button:
            if self.exit_rect.collidepoint(mouse_pos):
                exit_img = pygame.transform.scale(self.exit_button, (130, 35))
            else:
                exit_img = pygame.transform.scale(self.exit_button, (140, 38))
            self.exit_rect = exit_img.get_rect(center=self.exit_center)
            surface.blit(exit_img, self.exit_rect)
        else:
            pygame.draw.rect(surface, (200, 0, 0), self.exit_rect)
            

        title_surf = self.font_title.render("CHOOSE YOUR CHARACTER:", True, WHITE)
        surface.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2 + 18, 420))

        steve_border = (0, 255, 0) if self.selected_char_index == 0 else (100, 100, 100)
        pygame.draw.rect(surface, (101, 67, 33), self.steve_rect)
        pygame.draw.rect(surface, steve_border, self.steve_rect, 3 if self.selected_char_index == 0 else 1)
        steve_text = self.font_input.render("Steve", True, WHITE)
        surface.blit(steve_text, (self.steve_rect.centerx - steve_text.get_width() // 2, self.steve_rect.centery - steve_text.get_height() // 2))

        luna_border = (0, 255, 0) if self.selected_char_index == 1 else (100, 100, 100)
        pygame.draw.rect(surface, (101, 67, 33), self.luna_rect)
        pygame.draw.rect(surface, luna_border, self.luna_rect, 3 if self.selected_char_index == 1 else 1)
        luna_text = self.font_input.render("Luna", True, WHITE)
        surface.blit(luna_text, (self.luna_rect.centerx - luna_text.get_width() // 2, self.luna_rect.centery - luna_text.get_height() // 2))
