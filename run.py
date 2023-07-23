"""
run_game
create_board
validate_input
check_if_empty
check_for_winner
computer_random_move

"""


board = [' ' for i in range(9)]


def create_board():
    print('   |   |   ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |   ')


def run_game():
    """
    Runs the game tic-tac-toe displaying the board,
    receiving input from player and taking the computers turns

    """
    create_board()


run_game()
