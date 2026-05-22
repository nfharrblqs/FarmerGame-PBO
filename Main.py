import pygame
import sys
from ClassObject import WIDTH, HEIGHT, COLOR
from Field.Field import Game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertanian (Harvest Game)")

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
                    game.handle_planting()
                elif event.key == pygame.K_h:
                    game.handle_harvest()

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
