import pygame
import random
from src.config import WIDTH, HEIGHT, GRID_WIDTH, GRID_HEIGHT, TILE_SIZE, GREEN, RED, BLUE, BLACK, GREY, FPS
from src.grid import adjust_grid, draw_grid
from src.generate import generate_density

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    running = True
    playing = False
    use_colors = False

    count = 0
    update_freq = 10

    positions = set()
    born = set()
    died = set()

    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            prev = positions
            positions = adjust_grid(positions)

            born = positions - prev
            died = prev - positions

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            # Закрытие игры
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                elif event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                
                elif event.key == pygame.K_g:
                    # positions = gen(random.randrange(4, 10) * GRID_WIDTH)
                    positions = generate_density(0.2)

                elif event.key == pygame.K_EQUALS:
                    update_freq = max(1, update_freq - 1)
                
                elif event.key == pygame.K_MINUS:
                    update_freq += 1
                
                elif event.key == pygame.K_n and not playing:
                    prev = positions.copy()
                    positions = adjust_grid(positions)
                    born = positions - prev
                    died = prev - positions
                
                elif event.key == pygame.K_v:
                    use_colors = not use_colors

        screen.fill(GREY)
        draw_grid(positions, born, died, use_colors, screen)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()
