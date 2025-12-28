import pygame
from src.utils import get_neighbors, get_neighbors_infinity
from src.config import TILE_SIZE, BLACK, BLUE, GREEN, RED, GRID_HEIGHT, GRID_WIDTH, WIDTH, HEIGHT


def draw_grid(positions, born, died, use_colors, screen):
    for col, row in positions:
        if use_colors and (col, row) in born:
            color = BLUE
        else:
            color = GREEN

        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, color, (*top_left, TILE_SIZE, TILE_SIZE))

    if use_colors:
        for col, row in died:
            top_left = (col * TILE_SIZE, row * TILE_SIZE)
            pygame.draw.rect(screen, RED, (*top_left, TILE_SIZE, TILE_SIZE))

    # Генерируем сетку
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors_infinity(position)
        all_neighbors.update(neighbors)

        neighbors =  list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors_infinity(position)
        neighbors =  list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions
