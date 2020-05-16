from setup_game import load_board_state

def test_load_file_to_create_initial_state():
    expected = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
    assert load_board_state("./toad.txt") == expected