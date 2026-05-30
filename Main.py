import pygame
import sys
from ClassObject import WIDTH, HEIGHT, COLOR
from Field.Field import Game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertanian (Harvest Game)")

pygame.mouse.set_visible(True)  

pygame.mixer.music.load("musicBG/BGmusicfarmer.mp3")  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)

def main():
    clock = pygame.time.Clock()
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.open_seed_menu()  
                elif event.key == pygame.K_h:
                    game.handle_harvest()
                elif event.key == pygame.K_b:
                    game.shop.buy(game.player, "corn_seed")
                elif event.key == pygame.K_d:
                    game.shop.buy(game.player, "tomato_seed")

                elif event.key == pygame.K_7:  
                    game.shop.buy_animal(game.player, "chicken", game)
                elif event.key == pygame.K_8:  
                    game.shop.buy_animal(game.player, "cow", game)
                elif event.key == pygame.K_9:  
                    game.shop.buy_animal(game.player, "bull", game)

                elif event.key == pygame.K_c:
                    game.shop.sell_item(game.player, "corn_seed")

                elif event.key == pygame.K_j:
                    game.sell_nearest_animal()
                

                elif event.key == pygame.K_ESCAPE:
                    if game.seed_menu.visible:
                        game.seed_menu.hide()
                    else:
                        running = False
                elif event.key == pygame.K_s:

                    game.inventory_menu.show()
                    game.inventory_menu.mode = "sell"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                if game.shop.get_rect().collidepoint(mouse_pos):
                   game.toggle_shop()


                if event.button == 1: 
                    mouse_pos = pygame.mouse.get_pos()
                    if game.seed_menu.visible:
                        game.handle_planting_with_menu(mouse_pos)

        keys = pygame.key.get_pressed()
        game.player.move(keys)
        game.update()
        screen.fill(COLOR)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
