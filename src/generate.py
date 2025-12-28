import random
from src.config import GRID_HEIGHT, GRID_WIDTH


def generate(num):
    """
    Создаем клетки в рандомных местах
    """
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])


def generate_density(density=0.2):
    """
    Создаем клетки в виде плотности

    Чем выше значение 'density', тем карта будет более набита жизнью
    """
    position = set()

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if random.random() < density:
                position.add((x, y))
                
    return position
