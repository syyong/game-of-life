import random


def dead_state(width, height):
    return ([[0 for _ in range(width)] for _ in range(height)])

def random_cell_state():
    random_number = random.random()
    if random_number >= 0.5:
        cell_state = 0
    else:
        cell_state = 1
    return cell_state

def random_state(width,height):
    return [[random_cell_state() for _ in range(width)] for _ in range(height)]


if __name__ == '__main__':
    width = 5
    height = 5
    print(random_state(width, height))