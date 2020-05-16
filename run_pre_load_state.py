import sys

from setup_game import run, load_board_state


try:
    file_name = sys.argv[1]
    current_state = load_board_state(file_name)
    run(current_state)
except IOError:
    print("File not found")
