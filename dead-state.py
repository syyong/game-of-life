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

def render(state):
    top_border = '-' * (len(state[0]) + 2)
    side_border = '|'
    print(top_border)
    for i in state:
        line = []
        for j in i:
            if j ==1:
                line.append('#')
            else:
                line.append(' ')
        output = [side_border] + line + [side_border]
        print(''.join(output))
    print(top_border)

if __name__ == '__main__':
    render(random_state(5, 5))
    render(dead_state(5, 5))

