from app.config import GRID_HEIGHT, GRID_WIDTH


def get_neighbors(pos):
    """
    Обычное получение списка соседий
    """
    x, y = pos

    neighbors = []

    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))

    return neighbors


def get_neighbors_infinity(pos):
    """
    Обычное получение соседий, но края карты не учитываются. И получается
    'бесконечная' карта
    """
    x, y = pos
    neighbors = []

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue

            nx = (x + dx) % GRID_WIDTH
            ny = (y + dy) % GRID_HEIGHT

            neighbors.append((nx, ny))

    return neighbors
