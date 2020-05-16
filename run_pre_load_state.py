from setup_game import run, load_board_state

file_name = input('Please enter your file name: ')
try:
    run(load_board_state(file_name))
except IOError:
    print("File not found")
