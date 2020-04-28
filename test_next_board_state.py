from setup_game import next_board_state


def test_initial_state():
    initial_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert expected_state == next_board_state(initial_state)


def test_live_cell_w_0_neighbours_turn_dead():
    initial_state = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert expected_state == next_board_state(initial_state)


def test_live_cell_w_1_neighbours_turn_dead():
    initial_state = [
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert expected_state == next_board_state(initial_state)


def test_dead_cell_w_3_neighbours_come_alive():
    # This also test a live cell with 2 neighbours stay alive
    initial_state = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0],
    ]
    expected_state = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0],
    ]
    assert expected_state == next_board_state(initial_state)


def test_live_cell_w_4_neighbours_turn_dead():
    initial_state = [
        [0, 1, 1],
        [1, 1, 1],
        [0, 0, 0],
    ]
    expected_state = [
        [1, 0, 1],
        [1, 0, 1],
        [0, 1, 0],
    ]
    assert expected_state == next_board_state(initial_state)
