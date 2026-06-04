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

try:
    pygame.mixer.music.load("musicBG/BGmusicfarmer.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading background music: {e}")

buying_sound  = None
selling_sound = None    
planting_sound = None
harvesting_sound = None
cow_sound = None
chicken_sound = None
bull_sound = None
decor_sound = None
watering_sound = None

try:
    buying_sound  = pygame.mixer.Sound("PartialSound/SoundMethode/BuySell.mp3") 
    selling_sound = pygame.mixer.Sound("PartialSound/SoundMethode/BuySell.mp3")
    planting_sound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")
    harvesting_sound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")
    decor_sound = pygame.mixer.Sound("PartialSound/SoundMethode/PlantHarvest.mp3")

    cow_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/coworbull.mp3")
    chicken_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/chicken.mp3")
    bull_sound = pygame.mixer.Sound("PartialSound/SoundAnimal/coworbull.mp3")
    watering_sound = pygame.mixer.Sound("PartialSound/SoundMethode/Watering.mp3")

except pygame.error as e:

    print(f"Error loading sound: {e}")
    buying_sound = None
    selling_sound = None
    planting_sound = None
    harvesting_sound = None
    cow_sound = None
    chicken_sound = None
    bull_sound = None
    watering_sound = None

def main():
    clock = pygame.time.Clock()

    loading_screen = LoadingScreen()  
    
    game = None
    running = True 
    in_game = False
    game_won = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not in_game:
                result = loading_screen.handle_input(event)
                if result == "start":
                    print("Starting game...")
                    choice_chara = loading_screen.characters[loading_screen.selected_char_index]
                    game = Game(char_name=choice_chara)
                    game.buying_sound = buying_sound
                    game.selling_sound = selling_sound
                    game.planting_sound = planting_sound
                    game.harvesting_sound = harvesting_sound
                    game.watering_sound = watering_sound
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
                        game.water_mode = not game.water_mode
                        #game.water_nearest_plant()
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

                        clicked_animal = None
                        if game: 
                            for hewan in game.animals:
                                if hewan.get_rect().collidepoint(mouse_pos):
                                    clicked_animal = hewan
                                    break

                        if clicked_animal:
                       
                            if "chicken" in clicked_animal.tipe and chicken_sound:
                                chicken_sound.play()
                                print("Cluck! Cluck!")
                            elif "cow" in clicked_animal.tipe and cow_sound:
                                cow_sound.play()
                                print("Mooooo!")
                            elif "bull" in clicked_animal.tipe and bull_sound:
                                bull_sound.play()
                                print("MOOOO!")

                        if game.water_mode:
                            game.water_nearest_plant()
                            if game.watering_sound:
                                game.watering_sound.play()

                        elif game.shop_open:
                            game.handle_shop_click(mouse_pos)

                        elif game.inventory_menu.visible:
                            game.handle_inventory_click(mouse_pos)
                        else:
                            if game.held_item:
                                game.handle_world_click(mouse_pos)
                                if "scarecrow" in str(game.held_item).lower() or "bench" in str(game.held_item).lower() or "fence" in str(game.held_item).lower():
                                    if decor_sound:
                                        decor_sound.play()
                                elif "watering_can" in str(game.held_item).lower():
                                    if game.watering_sound:  # Suara watering
                                        game.watering_sound.play()
                                elif "seed" in str(game.held_item).lower():
                                    if planting_sound: 
                                        planting_sound.play()

                    elif event.button==3:
                        if game.held_item:
                            print(f"Dropped {game.held_item}")
                            game.held_item = None

        if in_game and game:
            keys = pygame.key.get_pressed()
            game.player.move(keys)

            result = game.update()
            if result == "win":
                game_won = True
           
            screen.fill(COLOR)
            game.draw(screen)

            if game_won:
           
                overlay = pygame.Surface((WIDTH, HEIGHT))
                overlay.set_alpha(180)
                overlay.fill((0, 0, 0))
                screen.blit(overlay, (0, 0))
                
                font_big = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 60)
                win_text = font_big.render(" YOU WIN! ", True, (255, 215, 0))
                screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - 80))
                
                font_med = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 40)
                gold_text = font_med.render(f"Gold: {game.player.money}", True, (255,255,255))
                screen.blit(gold_text, (WIDTH//2 - gold_text.get_width()//2, HEIGHT//2 - 20))
                
                font_small = pygame.font.Font("Font/pixelFont-7-8x14-sproutLands.ttf", 32)
                continue_text = font_small.render("Press SPACE to play again or ESC to quit", True, (255,255,255))
                screen.blit(continue_text, (WIDTH//2 - continue_text.get_width()//2, HEIGHT//2 + 50))
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:

                            game_won = False
                            game = None
                            in_game = False
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                    elif event.type == pygame.QUIT:
                        running = False
                        
        else:
            loading_screen.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
