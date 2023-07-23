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
    print('1  |2  |3  ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |   ')
    print('-----------')
    print('4  |5  |6  ')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |   ')
    print('-----------')
    print('7  |8  |9  ')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |   ')


def run_game():
    """
    Runs the game tic-tac-toe displaying the board,
    receiving input from player and taking the computers turns

    """
    create_board()


def get_welcome_message(file):
    data = open(file)
    file_data = data.read()
    data.close()
    return file_data

    
welcome_message = get_welcome_message('welcome.txt')
print(welcome_message)
run_game()
