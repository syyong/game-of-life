import random
import time


def dead_state(width, height):
    """
    :param width: int
    :param height: int
    :return: a matrix of dead_state
    """
    return ([[0 for _ in range(width)] for _ in range(height)])


def random_cell_state():
    """
    :return: cell_state: int
    """
    random_number = random.random()
    if random_number >= 0.5:
        cell_state = 0
    else:
        cell_state = 1
    return cell_state


def random_state(width, height):
    """
    :param width: int
    :param height: int
    :return: a matrix of random state
    """
    return [[random_cell_state() for _ in range(width)] for _ in range(height)]


def render(state):
    """
    :param state: a matrix of cell states
    """
    border = '-' * (len(state[0]))
    side_border = '|'
    print(f'sy{border}')
    for i in state:
        line = []
        for j in i:
            if j == 1:
                line.append('*')
            else:
                line.append(' ')
        output = [side_border] + line + [side_border]
        print(''.join(output))
    print(f'  {border}')


def next_board_state(current_state):
    """
    :param current_state:
    :return: next_board_state: a matrix of cell states
    """
    height = len(current_state)
    width = len(current_state[0])
    next_state = dead_state(width, height)

    for y in range(height):
        for x in range(width):
            cell_states = []
            if x == 0:
                if y == 0:
                    cell_states = [
                        current_state[y + 1][x],
                        current_state[y + 1][x + 1],
                        current_state[y][x + 1],
                    ]
                elif y == height - 1:
                    cell_states = [
                        current_state[y - 1][x],
                        current_state[y - 1][x + 1],
                        current_state[y][x + 1],
                    ]
                else:
                    cell_states = [
                        current_state[y - 1][x],
                        current_state[y - 1][x + 1],
                        current_state[y][x + 1],
                        current_state[y + 1][x],
                        current_state[y + 1][x + 1],
                    ]
            elif x == width - 1:
                if y == 0:
                    cell_states = [
                        current_state[y + 1][x],
                        current_state[y + 1][x - 1],
                        current_state[y][x - 1],
                    ]
                elif y == height - 1:
                    cell_states = [
                        current_state[y - 1][x],
                        current_state[y - 1][x - 1],
                        current_state[y][x - 1],
                    ]
                else:
                    cell_states = [
                        current_state[y - 1][x],
                        current_state[y - 1][x - 1],
                        current_state[y][x - 1],
                        current_state[y + 1][x],
                        current_state[y + 1][x - 1],
                    ]
            elif y == 0:
                if 0 < x < width - 1:
                    cell_states = [
                        current_state[y][x - 1],
                        current_state[y + 1][x - 1],
                        current_state[y + 1][x],
                        current_state[y + 1][x + 1],
                        current_state[y][x + 1],
                    ]
            elif y == height - 1:
                if 0 < x < width - 1:
                    cell_states = [
                        current_state[y][x - 1],
                        current_state[y - 1][x - 1],
                        current_state[y - 1][x],
                        current_state[y - 1][x + 1],
                        current_state[y][x + 1],
                    ]
            else:
                cell_states = [
                    current_state[y][x - 1],
                    current_state[y - 1][x - 1],
                    current_state[y - 1][x],
                    current_state[y - 1][x + 1],
                    current_state[y][x + 1],
                    current_state[y + 1][x - 1],
                    current_state[y + 1][x],
                    current_state[y + 1][x + 1],
                ]
            sum_neighbour = sum(cell_states)
            if current_state[y][x] == 1:
                if sum_neighbour <= 1:
                    next_state[y][x] = 0
                if 2 <= sum_neighbour <= 3:
                    next_state[y][x] = 1
                if sum_neighbour > 3:
                    next_state[y][x] = 0
            else:
                if sum_neighbour == 3:
                    next_state[y][x] = 1
    return next_state


if __name__ == '__main__':
    width = input('Please specify the width of your game of life: ')
    height = input('Please specify the height of your game of life: ')
    print(f'The size of your game of life is {width} x {height}. Enjoy')
    time.sleep(1)

    if not width:
        width = 3
    if not height:
        height = 3

    current_state = random_state(int(width), int(height))

    try:
        while True:
            render(current_state)
            time.sleep(0.5)
            current_state = next_board_state(current_state)
    except KeyboardInterrupt:
        print('Thanks for playing!')
