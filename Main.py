import pygame
import sys
from ClassObject import WIDTH, HEIGHT, COLOR
from Field.Field import Game
from UI.LoadScreen import LoadingScreen

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertanian (Harvest Game)")

pygame.mouse.set_visible(True)  

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
                        game.plantingSound.play()
                    elif event.key == pygame.K_w:
                        game.water_nearest_plant()
                    elif event.key == pygame.K_t:
                        game.toggle_shop()
                    elif event.key == pygame.K_b:
                        game.shop.buy(game.player, "corn_seed", "tomato_seed", "carrot_seed", "cabbage_seed", "beans_seed", "grape_seed")
                        game.buyingSound.play()
                    elif event.key == pygame.K_v:  
                        game.shop.buy_animal(game.player, "chicken", "cow", "bull")
                        game.buyingSound.play()
                    elif event.key == pygame.K_c:
                        game.shop.sell_item(game.player, "corn_seed", "tomato_seed", "carrot_seed", "cabbage_seed", "beans_seed", "grape_seed")
                    elif event.key == pygame.K_8:
                        game.shop.sell_item(game.plants, "corn", "tomato", "carrot", "cabbage", "beans", "grape")
                    elif event.key == pygame.K_j:
                        game.sell_nearest_animal()
                    elif event.key == pygame.K_s:
                        game.inventory_menu.show()
                        game.inventory_menu.mode = "sell"
                    elif event.key == pygame.K_ESCAPE:
                        if game.inventory_menu.visible:
                            game.inventory_menu.hide()
                        else:
                            in_game = False
                            game = None
                            print("Kembali ke menu utama")
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if game.shop.get_rect().collidepoint(mouse_pos):
                            print("click at shop!")
                        
                        if game.inventory_menu.visible:
                            game.handle_inventory_click(mouse_pos)
                            game.plantingSound.play()

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