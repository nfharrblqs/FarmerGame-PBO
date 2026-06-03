import pygame
import sys
from ClassObject import WIDTH, HEIGHT, COLOR
from Field.Field import Game
from UI.LoadScreen import LoadingScreen

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertanian (Harvest Game)")

pygame.mouse.set_visible(True)  

bg_music = pygame.mixer.Sound("musicBG/BGmusicfarmer.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

try:
    buying_sound  = pygame.mixer.Sound("PartialSound/SoundMethode/BuySell.mp3") 
    selling_sound = pygame.mixer.Sound("PartialSound/SoundMethode/BuySell.mp3")
    planting_sound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")
    harvesting_sound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")

    cow_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/SoundCow.mp3")
    cow_sound.set_volume(0.8)
    chicken_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/SoundChicken.mp3")
    chicken_sound.set_volume(0.8)
    bull_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/SoundBull.mp3")
    bull_sound.set_volume(0.8)
except pygame.error as e:
    print(f"Error loading sound: {e}")
    buying_sound = None
    selling_sound = None
    planting_sound = None
    harvesting_sound = None
    cow_sound = None
    chicken_sound = None
    bull_sound = None

pygame.mixer.music.load("musicBG/BGmusicfarmer.mp3")  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)

def main():
    clock = pygame.time.Clock()

    loading_screen = LoadingScreen()  
    
    game = None
    running = True 
    in_game = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not in_game:
                result = loading_screen.handle_input(event)
                if result == "start":
                    print("Starting game...")
                    game = Game()
                    in_game = True
                elif result == "exit":
                    running = False

            elif in_game and game:  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        game.open_inventory()
                    elif event.key == pygame.K_h:
                        game.handle_harvest()
                        if game.harvesting_sound:
                            game.harvesting_sound.play()
                    elif event.key == pygame.K_w:
                        game.water_nearest_plant()
                    elif event.key == pygame.K_t:
                        game.toggle_shop()
                    elif event.key == pygame.K_b:
                        game.shop.SellToPlayer(game.player, "corn_seed", "tomato_seed", "carrot_seed", "cabbage_seed", "beans_seed", "grape_seed", "chicken", "cow", "bull")
                        if game.buying_sound:
                            game.buying_sound.play()
                    elif event.key == pygame.K_c:
                        game.shop.buyFromPlayer(
                            game.player, "corn_seed", "tomato_seed", "carrot_seed", 
                            "cabbage_seed", "beans_seed", "grape_seed", 
                            "chicken", "cow", "bull","corn", 
                            "tomato", "carrot", "cabbage", "beans", "grape",
                            "meat", "milk", "egg")
                        if game.selling_sound:
                            game.selling_sound.play()
                    elif event.key == pygame.K_j:
                        game.sell_nearest_animal()
                    elif event.key == pygame.K_s:
                        game.inventory_menu.show()
                        game.inventory_menu.mode = "sell"
                    elif event.key == pygame.K_f:
                        game.feed_nearest_animal()
                    elif event.key == pygame.K_ESCAPE:
                        if game.inventory_menu.visible:
                            game.inventory_menu.hide()
                        else:
                            in_game = False
                            game = None
                            print("Kembali ke menu utama")
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos =pygame.mouse.get_pos()
                    if event.button == 1:
                        if game.shop_open:
                            game.handle_shop_click(mouse_pos)
                        elif game.inventory_menu.visible:
                            game.handle_inventory_click(mouse_pos)
                        else:
                            if game.held_item:
                                game.handle_world_click(mouse_pos)
                                if planting_sound: 
                                    planting_sound.play()
                    elif event.button==3:
                        if game.held_item:
                            print(f"Dropped {game.held_item}")
                            game.held_item = None

        if in_game and game:
            keys = pygame.key.get_pressed()
            game.player.move(keys)
            game.update()
            screen.fill(COLOR)
            game.draw(screen)
        else:
            loading_screen.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()