import pygame
from ClassObject import WIDTH, HEIGHT

class LoadingScreen:
    def __init__(self):
        self.visible = True
        self.selected_option = 0  
        self.options = ["START", "EXIT"]
        
        try:
            self.background = pygame.image.load("AssetPNG/Startpage/barugamestart.png").convert_alpha()
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
            print("Loading screen background loaded")
        except:
            print("Background tidak ditemukan, pakai warna default")
            self.background = None

        self.start_button = None
        self.exit_button = None

        self.button_width = 140
        self.button_height = 38

        self.start_rect = None
        self.exit_rect = None

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

    def handle_input(self, event):
        """Handle keyboard dan mouse input di loading screen"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                mouse_pos = pygame.mouse.get_pos()

                if self.start_rect and self.start_rect.collidepoint(mouse_pos):
                    print("Klik START!")
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

       start_x = 350
       start_y = 290

       exit_x = 350
       exit_y = 340

       start_center = (420,309)
       exit_center = (420, 359)

       self.start_rect = pygame.Rect(start_x, start_y,self.button_width, self.button_height)

       self.exit_rect = pygame.Rect(exit_x, exit_y,self.button_width, self.button_height)

       mouse_pos = pygame.mouse.get_pos()

       if self.start_rect.collidepoint(mouse_pos):
           start_img = pygame.transform.scale(self.start_button, (130,35))

       else:
           start_img = pygame.transform.scale(self.start_button,(140, 38))

       self.start_rect = start_img.get_rect(center = start_center)
       surface.blit(start_img, self.start_rect)

       if self.exit_rect.collidepoint(mouse_pos):
           exit_img = pygame.transform.scale(self.exit_button, (130,35))

       else:
            exit_img = pygame.transform.scale(self.exit_button,(140, 38))
           
       self.exit_rect = exit_img.get_rect(center = exit_center)
       surface.blit(exit_img, self.exit_rect)